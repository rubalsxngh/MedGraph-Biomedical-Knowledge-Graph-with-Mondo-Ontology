"""
the function 'get_docx' scrappes the pubMed website, 
// we are only retrieving abstract of the articles, not the actual article, nothing illegal!
"""

def get_docx(keyword_to_be_searched, no_of_article):

    import requests
    from bs4 import BeautifulSoup
    from docx import Document

    keyword = keyword_to_be_searched
    articles_per_page = 10
    pages_to_scrape = (no_of_article - 1) // articles_per_page + 1

    with open(f"D:/VIISem/knowledgeGraphUsingMondo/datasets/dataset.txt", "w", encoding="utf-8") as txt_file:

        for page in range(1, pages_to_scrape + 1):
            url = f"https://pubmed.ncbi.nlm.nih.gov/?term={keyword}&page={page}"

            response = requests.get(url)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                articles = soup.find_all('a', class_='docsum-title')

                for article in articles[:min(articles_per_page, no_of_article)]:
                    article_url = "https://pubmed.ncbi.nlm.nih.gov" + article["href"]
                    article_response = requests.get(article_url)

                    if article_response.status_code == 200:
                        article_soup = BeautifulSoup(article_response.text, 'html.parser')

                        title = article_soup.find('h1', class_='heading-title').text.strip()
                        abstract_element = article_soup.find('div', class_='abstract-content')
                        if abstract_element is not None:
                            abstract = abstract_element.text.strip()
                        else:
                            abstract = "Abstract not found."

                        txt_file.write(f"{title}\n")
                        txt_file.write(f"{abstract}\n\n")
                        no_of_article -= 1
                    else:
                        print(f"Failed to retrieve article data. Status code: {article_response.status_code}")

            else:
                print(f"Failed to retrieve search results. Status code: {response.status_code}")

            if no_of_article <= 0:
                break

    print("Search results saved to a text file.")

