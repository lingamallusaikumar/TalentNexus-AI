"""
TalentNexus AI - Artificial Intelligence & Data Science Comprehensive Domain Taxonomy
Defines skills, seniority criteria, interview evaluation rubrics, and relational weights.
"""

DOMAIN_NAME = 'Artificial Intelligence & Data Science'
DOMAIN_KEY = 'ai_ml'

TAXONOMY_RECORDS = [
    {
        'id': 'ai_ml_001',
        'canonical_name': 'Machine Learning',
        'category': 'Artificial Intelligence & Data Science',
        'aliases': ['machine learning', 'machine-learning', 'machinelearning'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Machine Learning syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Machine Learning.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Machine Learning.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Machine Learning.'
        },
        'interview_rubric': [
            'How does Machine Learning handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Machine Learning and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Machine Learning?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': True
    },
    {
        'id': 'ai_ml_002',
        'canonical_name': 'Deep Learning',
        'category': 'Artificial Intelligence & Data Science',
        'aliases': ['deep learning', 'deep-learning', 'deeplearning'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Deep Learning syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Deep Learning.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Deep Learning.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Deep Learning.'
        },
        'interview_rubric': [
            'How does Deep Learning handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Deep Learning and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Deep Learning?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': True
    },
    {
        'id': 'ai_ml_003',
        'canonical_name': 'Natural Language Processing (NLP)',
        'category': 'Artificial Intelligence & Data Science',
        'aliases': ['natural language processing (nlp)', 'natural-language-processing-(nlp)', 'naturallanguageprocessing(nlp)'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Natural Language Processing (NLP) syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Natural Language Processing (NLP).',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Natural Language Processing (NLP).',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Natural Language Processing (NLP).'
        },
        'interview_rubric': [
            'How does Natural Language Processing (NLP) handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Natural Language Processing (NLP) and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Natural Language Processing (NLP)?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': True
    },
    {
        'id': 'ai_ml_004',
        'canonical_name': 'Computer Vision',
        'category': 'Artificial Intelligence & Data Science',
        'aliases': ['computer vision', 'computer-vision', 'computervision'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Computer Vision syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Computer Vision.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Computer Vision.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Computer Vision.'
        },
        'interview_rubric': [
            'How does Computer Vision handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Computer Vision and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Computer Vision?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': True
    },
    {
        'id': 'ai_ml_005',
        'canonical_name': 'Large Language Models (LLMs)',
        'category': 'Artificial Intelligence & Data Science',
        'aliases': ['large language models (llms)', 'large-language-models-(llms)', 'largelanguagemodels(llms)'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Large Language Models (LLMs) syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Large Language Models (LLMs).',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Large Language Models (LLMs).',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Large Language Models (LLMs).'
        },
        'interview_rubric': [
            'How does Large Language Models (LLMs) handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Large Language Models (LLMs) and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Large Language Models (LLMs)?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': True
    },
    {
        'id': 'ai_ml_006',
        'canonical_name': 'Transformers',
        'category': 'Artificial Intelligence & Data Science',
        'aliases': ['transformers', 'transformers', 'transformers'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Transformers syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Transformers.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Transformers.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Transformers.'
        },
        'interview_rubric': [
            'How does Transformers handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Transformers and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Transformers?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': True
    },
    {
        'id': 'ai_ml_007',
        'canonical_name': 'PyTorch',
        'category': 'Artificial Intelligence & Data Science',
        'aliases': ['pytorch', 'pytorch', 'pytorch'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of PyTorch syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with PyTorch.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using PyTorch.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing PyTorch.'
        },
        'interview_rubric': [
            'How does PyTorch handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in PyTorch and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling PyTorch?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': True
    },
    {
        'id': 'ai_ml_008',
        'canonical_name': 'TensorFlow',
        'category': 'Artificial Intelligence & Data Science',
        'aliases': ['tensorflow', 'tensorflow', 'tensorflow'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of TensorFlow syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with TensorFlow.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using TensorFlow.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing TensorFlow.'
        },
        'interview_rubric': [
            'How does TensorFlow handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in TensorFlow and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling TensorFlow?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': True
    },
    {
        'id': 'ai_ml_009',
        'canonical_name': 'Keras',
        'category': 'Artificial Intelligence & Data Science',
        'aliases': ['keras', 'keras', 'keras'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Keras syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Keras.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Keras.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Keras.'
        },
        'interview_rubric': [
            'How does Keras handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Keras and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Keras?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': True
    },
    {
        'id': 'ai_ml_010',
        'canonical_name': 'Scikit-Learn',
        'category': 'Artificial Intelligence & Data Science',
        'aliases': ['scikit-learn', 'scikit-learn', 'scikit-learn'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Scikit-Learn syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Scikit-Learn.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Scikit-Learn.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Scikit-Learn.'
        },
        'interview_rubric': [
            'How does Scikit-Learn handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Scikit-Learn and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Scikit-Learn?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': True
    },
    {
        'id': 'ai_ml_011',
        'canonical_name': 'spaCy',
        'category': 'Artificial Intelligence & Data Science',
        'aliases': ['spacy', 'spacy', 'spacy'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of spaCy syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with spaCy.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using spaCy.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing spaCy.'
        },
        'interview_rubric': [
            'How does spaCy handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in spaCy and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling spaCy?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': False
    },
    {
        'id': 'ai_ml_012',
        'canonical_name': 'Hugging Face',
        'category': 'Artificial Intelligence & Data Science',
        'aliases': ['hugging face', 'hugging-face', 'huggingface'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Hugging Face syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Hugging Face.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Hugging Face.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Hugging Face.'
        },
        'interview_rubric': [
            'How does Hugging Face handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Hugging Face and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Hugging Face?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': False
    },
    {
        'id': 'ai_ml_013',
        'canonical_name': 'LangChain',
        'category': 'Artificial Intelligence & Data Science',
        'aliases': ['langchain', 'langchain', 'langchain'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of LangChain syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with LangChain.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using LangChain.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing LangChain.'
        },
        'interview_rubric': [
            'How does LangChain handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in LangChain and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling LangChain?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': False
    },
    {
        'id': 'ai_ml_014',
        'canonical_name': 'LlamaIndex',
        'category': 'Artificial Intelligence & Data Science',
        'aliases': ['llamaindex', 'llamaindex', 'llamaindex'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of LlamaIndex syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with LlamaIndex.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using LlamaIndex.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing LlamaIndex.'
        },
        'interview_rubric': [
            'How does LlamaIndex handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in LlamaIndex and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling LlamaIndex?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': False
    },
    {
        'id': 'ai_ml_015',
        'canonical_name': 'Sentence-Transformers',
        'category': 'Artificial Intelligence & Data Science',
        'aliases': ['sentence-transformers', 'sentence-transformers', 'sentence-transformers'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Sentence-Transformers syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Sentence-Transformers.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Sentence-Transformers.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Sentence-Transformers.'
        },
        'interview_rubric': [
            'How does Sentence-Transformers handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Sentence-Transformers and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Sentence-Transformers?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': False
    },
    {
        'id': 'ai_ml_016',
        'canonical_name': 'BERT',
        'category': 'Artificial Intelligence & Data Science',
        'aliases': ['bert', 'bert', 'bert'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of BERT syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with BERT.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using BERT.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing BERT.'
        },
        'interview_rubric': [
            'How does BERT handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in BERT and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling BERT?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': False
    },
    {
        'id': 'ai_ml_017',
        'canonical_name': 'GPT Architecture',
        'category': 'Artificial Intelligence & Data Science',
        'aliases': ['gpt architecture', 'gpt-architecture', 'gptarchitecture'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of GPT Architecture syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with GPT Architecture.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using GPT Architecture.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing GPT Architecture.'
        },
        'interview_rubric': [
            'How does GPT Architecture handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in GPT Architecture and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling GPT Architecture?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': False
    },
    {
        'id': 'ai_ml_018',
        'canonical_name': 'Vector Databases',
        'category': 'Artificial Intelligence & Data Science',
        'aliases': ['vector databases', 'vector-databases', 'vectordatabases'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Vector Databases syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Vector Databases.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Vector Databases.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Vector Databases.'
        },
        'interview_rubric': [
            'How does Vector Databases handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Vector Databases and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Vector Databases?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': False
    },
    {
        'id': 'ai_ml_019',
        'canonical_name': 'Pinecone',
        'category': 'Artificial Intelligence & Data Science',
        'aliases': ['pinecone', 'pinecone', 'pinecone'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Pinecone syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Pinecone.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Pinecone.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Pinecone.'
        },
        'interview_rubric': [
            'How does Pinecone handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Pinecone and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Pinecone?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': False
    },
    {
        'id': 'ai_ml_020',
        'canonical_name': 'Milvus',
        'category': 'Artificial Intelligence & Data Science',
        'aliases': ['milvus', 'milvus', 'milvus'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Milvus syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Milvus.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Milvus.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Milvus.'
        },
        'interview_rubric': [
            'How does Milvus handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Milvus and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Milvus?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': False
    },
    {
        'id': 'ai_ml_021',
        'canonical_name': 'Qdrant',
        'category': 'Artificial Intelligence & Data Science',
        'aliases': ['qdrant', 'qdrant', 'qdrant'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Qdrant syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Qdrant.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Qdrant.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Qdrant.'
        },
        'interview_rubric': [
            'How does Qdrant handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Qdrant and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Qdrant?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': False
    },
    {
        'id': 'ai_ml_022',
        'canonical_name': 'ChromaDB',
        'category': 'Artificial Intelligence & Data Science',
        'aliases': ['chromadb', 'chromadb', 'chromadb'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of ChromaDB syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with ChromaDB.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using ChromaDB.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing ChromaDB.'
        },
        'interview_rubric': [
            'How does ChromaDB handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in ChromaDB and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling ChromaDB?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': False
    },
    {
        'id': 'ai_ml_023',
        'canonical_name': 'FAISS',
        'category': 'Artificial Intelligence & Data Science',
        'aliases': ['faiss', 'faiss', 'faiss'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of FAISS syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with FAISS.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using FAISS.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing FAISS.'
        },
        'interview_rubric': [
            'How does FAISS handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in FAISS and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling FAISS?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': False
    },
    {
        'id': 'ai_ml_024',
        'canonical_name': 'Pandas',
        'category': 'Artificial Intelligence & Data Science',
        'aliases': ['pandas', 'pandas', 'pandas'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Pandas syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Pandas.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Pandas.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Pandas.'
        },
        'interview_rubric': [
            'How does Pandas handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Pandas and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Pandas?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': False
    },
    {
        'id': 'ai_ml_025',
        'canonical_name': 'NumPy',
        'category': 'Artificial Intelligence & Data Science',
        'aliases': ['numpy', 'numpy', 'numpy'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of NumPy syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with NumPy.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using NumPy.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing NumPy.'
        },
        'interview_rubric': [
            'How does NumPy handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in NumPy and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling NumPy?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': False
    },
    {
        'id': 'ai_ml_026',
        'canonical_name': 'SciPy',
        'category': 'Artificial Intelligence & Data Science',
        'aliases': ['scipy', 'scipy', 'scipy'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of SciPy syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with SciPy.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using SciPy.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing SciPy.'
        },
        'interview_rubric': [
            'How does SciPy handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in SciPy and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling SciPy?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': False
    },
    {
        'id': 'ai_ml_027',
        'canonical_name': 'Matplotlib',
        'category': 'Artificial Intelligence & Data Science',
        'aliases': ['matplotlib', 'matplotlib', 'matplotlib'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Matplotlib syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Matplotlib.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Matplotlib.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Matplotlib.'
        },
        'interview_rubric': [
            'How does Matplotlib handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Matplotlib and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Matplotlib?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': False
    },
    {
        'id': 'ai_ml_028',
        'canonical_name': 'Seaborn',
        'category': 'Artificial Intelligence & Data Science',
        'aliases': ['seaborn', 'seaborn', 'seaborn'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Seaborn syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Seaborn.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Seaborn.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Seaborn.'
        },
        'interview_rubric': [
            'How does Seaborn handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Seaborn and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Seaborn?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': False
    },
    {
        'id': 'ai_ml_029',
        'canonical_name': 'Plotly',
        'category': 'Artificial Intelligence & Data Science',
        'aliases': ['plotly', 'plotly', 'plotly'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Plotly syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Plotly.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Plotly.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Plotly.'
        },
        'interview_rubric': [
            'How does Plotly handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Plotly and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Plotly?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': False
    },
    {
        'id': 'ai_ml_030',
        'canonical_name': 'OpenCV',
        'category': 'Artificial Intelligence & Data Science',
        'aliases': ['opencv', 'opencv', 'opencv'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of OpenCV syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with OpenCV.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using OpenCV.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing OpenCV.'
        },
        'interview_rubric': [
            'How does OpenCV handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in OpenCV and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling OpenCV?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': False
    },
    {
        'id': 'ai_ml_031',
        'canonical_name': 'NLTK',
        'category': 'Artificial Intelligence & Data Science',
        'aliases': ['nltk', 'nltk', 'nltk'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of NLTK syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with NLTK.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using NLTK.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing NLTK.'
        },
        'interview_rubric': [
            'How does NLTK handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in NLTK and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling NLTK?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': False
    },
    {
        'id': 'ai_ml_032',
        'canonical_name': 'MLflow',
        'category': 'Artificial Intelligence & Data Science',
        'aliases': ['mlflow', 'mlflow', 'mlflow'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of MLflow syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with MLflow.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using MLflow.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing MLflow.'
        },
        'interview_rubric': [
            'How does MLflow handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in MLflow and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling MLflow?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': False
    },
    {
        'id': 'ai_ml_033',
        'canonical_name': 'Weights & Biases',
        'category': 'Artificial Intelligence & Data Science',
        'aliases': ['weights & biases', 'weights-&-biases', 'weights&biases'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Weights & Biases syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Weights & Biases.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Weights & Biases.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Weights & Biases.'
        },
        'interview_rubric': [
            'How does Weights & Biases handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Weights & Biases and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Weights & Biases?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': False
    },
    {
        'id': 'ai_ml_034',
        'canonical_name': 'Kubeflow',
        'category': 'Artificial Intelligence & Data Science',
        'aliases': ['kubeflow', 'kubeflow', 'kubeflow'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Kubeflow syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Kubeflow.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Kubeflow.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Kubeflow.'
        },
        'interview_rubric': [
            'How does Kubeflow handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Kubeflow and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Kubeflow?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': False
    },
    {
        'id': 'ai_ml_035',
        'canonical_name': 'Feature Stores',
        'category': 'Artificial Intelligence & Data Science',
        'aliases': ['feature stores', 'feature-stores', 'featurestores'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Feature Stores syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Feature Stores.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Feature Stores.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Feature Stores.'
        },
        'interview_rubric': [
            'How does Feature Stores handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Feature Stores and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Feature Stores?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': False
    },
    {
        'id': 'ai_ml_036',
        'canonical_name': 'Data Pipelines',
        'category': 'Artificial Intelligence & Data Science',
        'aliases': ['data pipelines', 'data-pipelines', 'datapipelines'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Data Pipelines syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Data Pipelines.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Data Pipelines.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Data Pipelines.'
        },
        'interview_rubric': [
            'How does Data Pipelines handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Data Pipelines and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Data Pipelines?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': False
    },
    {
        'id': 'ai_ml_037',
        'canonical_name': 'Apache Spark',
        'category': 'Artificial Intelligence & Data Science',
        'aliases': ['apache spark', 'apache-spark', 'apachespark'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Apache Spark syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Apache Spark.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Apache Spark.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Apache Spark.'
        },
        'interview_rubric': [
            'How does Apache Spark handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Apache Spark and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Apache Spark?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': False
    },
    {
        'id': 'ai_ml_038',
        'canonical_name': 'Apache Flink',
        'category': 'Artificial Intelligence & Data Science',
        'aliases': ['apache flink', 'apache-flink', 'apacheflink'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Apache Flink syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Apache Flink.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Apache Flink.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Apache Flink.'
        },
        'interview_rubric': [
            'How does Apache Flink handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Apache Flink and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Apache Flink?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': False
    },
    {
        'id': 'ai_ml_039',
        'canonical_name': 'Airflow',
        'category': 'Artificial Intelligence & Data Science',
        'aliases': ['airflow', 'airflow', 'airflow'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Airflow syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Airflow.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Airflow.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Airflow.'
        },
        'interview_rubric': [
            'How does Airflow handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Airflow and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Airflow?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': False
    },
    {
        'id': 'ai_ml_040',
        'canonical_name': 'dbt',
        'category': 'Artificial Intelligence & Data Science',
        'aliases': ['dbt', 'dbt', 'dbt'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of dbt syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with dbt.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using dbt.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing dbt.'
        },
        'interview_rubric': [
            'How does dbt handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in dbt and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling dbt?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': False
    },
]


def get_ai_ml_skill_map() -> dict:
    return {item['canonical_name']: item for item in TAXONOMY_RECORDS}

def get_ai_ml_aliases_lookup() -> dict:
    lookup = {}
    for item in TAXONOMY_RECORDS:
        for alias in item['aliases']:
            lookup[alias.lower()] = item['canonical_name']
    return lookup
