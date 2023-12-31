#manually extracted entities
entities_list = [
    # Abstract 1
    [
        "Non-Hodgkin lymphoma",
        "organ",
        "body",
        "symptoms",
        "physicians",
        "specialties",
        "biology",
        "genetics",
        "diagnostic methods",
        "therapies",
        "The Lancet"
    ],
    
    # Abstract 2
    [
        "Lymphomas",
        "Hodgkin",
        "Non-Hodgkin",
        "organ",
        "B cell",
        "T cell",
        "natural killer cell",
        "indolent lymphomas",
        "aggressive lymphomas",
        "chemosensitive"
    ],

    # Abstract 3
    [
        "Hodgkin lymphoma",
        "Non-Hodgkin lymphoma",
        "malignant lymphomas",
        "lymphocytes",
        "clonal proliferation",
        "natural history",
        "epidemiology",
        "pathologic characteristics",
        "clinical presentation",
        "optimal management",
        "The Lancet"
    ],

    # Abstract 4
    [
        "T-cell lymphomas",
        "Hodgkin lymphomas",
        "histiocytic/dendritic cell neoplasms",
        "World Health Organization (WHO) system",
        "pathological",
        "genetic",
        "clinical factors",
        "T-follicular helper cell-derived lymphomas",
        "indolent T-cell lymphomas",
        "lymphoproliferative disorders"
    ],

    # Abstract 5
    [
        "lymphomas",
        "normal lymphoid system",
        "B-cell",
        "T-cell",
        "natural killer-cell neoplasms",
        "multiparameter approach",
        "Revised European and American Lymphoma",
        "WHO classifications",
        "molecular alterations",
        "The Lancet"
    ]
]


#the source dataset

dataset= [
    "Lymphomas can affect any organ in the body, present with a wide range of symptoms, and be seen by primary care physicians and physicians from most specialties. They are traditionally divided into Hodgkin's lymphoma (which accounts for about 10% of all lymphomas) and non-Hodgkin lymphoma, which is the topic of this Seminar. Non-Hodgkin lymphoma represents a wide spectrum of illnesses that vary from the most indolent to the most aggressive malignancies. They arise from lymphocytes that are at various stages of development, and the characteristics of the specific lymphoma subtype reflect those of the cell from which they originated. Since this topic was last reviewed in The Lancet in 2012, advances in understanding the biology and genetics of non-Hodgkin lymphoma and the availability of new diagnostic methods and therapies have improved our ability to manage patients with this disorder.",

    "Lymphomas may be broadly divided into non-Hodgkin (90%) and Hodgkin (10%) types. Most lymphomas (90%) are of B cell origin but can also be T cell or natural killer cell. Clinical management of indolent and aggressive lymphomas is different. Aggressive lymphomas are more dangerous if left untreated yet a higher cell proliferation rate also renders them more chemosensitive, so they are managed with curative intent. Indolent lymphomas are, for the most part, incurable, such that quality of life must be balanced against toxicity of treatment in deciding when and how to treat.",

    "The malignant lymphomas, including both Hodgkin lymphoma (HL) and non-Hodgkin lymphoma (NHL), represent a diverse group of diseases that arise from a clonal proliferation of lymphocytes. Each of the more than 30 unique types of lymphoma is a disease with a distinct natural history. This biologic heterogeneity gives rise to marked differences among the lymphomas with respect to epidemiology, pathologic characteristics, clinical presentation, and optimal management. This article emphasizes the principles of diagnosis, including appropriate pathologic evaluation and staging considerations, and focuses on the clinical presentation, staging, and optimal management strategies for the most common types of lymphoma.",

    "Lymphomas are classified based on the normal counterpart, or cell of origin, from which they arise. Because lymphocytes have physiologic immune functions that vary both by lineage and by stage of differentiation, the classification of lymphomas arising from these normal lymphoid populations is complex. Recent genomic data have contributed additional depth to this complexity. Areas covered: Lymphoma classification follows the World Health Organization (WHO) system, which reflects international consensus and is based on pathological, genetic, and clinical factors. The present review focuses on the classification of T-cell lymphomas, Hodgkin lymphomas, and histiocytic and dendritic cell neoplasms, summarizing changes reflected in the 2016 revision to the WHO classification. These changes are critical to hematologists and other clinicians who care for patients with these disorders. Expert commentary: Lymphoma classification is a continually evolving field that needs to be responsive to new clinical, pathological, and molecular understanding of lymphoid neoplasia. Among the entities covered in this review, the 2016 revisions in the WHO classification particularly impact T-cell lymphomas, including a new umbrella category of T-follicular helper cell-derived lymphomas and evolving recognition of indolent T-cell lymphomas and lymphoproliferative disorders.",

    "Our current understanding of the normal lymphoid system informs the modern classification of lymphomas. B-cell, T-cell, and natural killer-cell neoplasms often recapitulate normal stages of lymphoid cell differentiation and function. Moreover, the clinical manifestations of lymphomas often reflect the normal function of lymphoid cells in vivo. The multiparameter approach to classification adopted by the Revised European and American Lymphoma and subsequent WHO classifications facilitates the interpretation of clinical and translational studies, and provides a framework for the discovery of molecular alterations that drive these tumors. An accurate and precise classification of disease entities facilitates the discovery of the molecular basis of lymphoid neoplasms in the basic science laboratory, and leads to new diagnostic tools that play a role in clinical diagnosis.",
]
