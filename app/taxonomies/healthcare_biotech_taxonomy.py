"""
TalentNexus AI - Healthcare, Life Sciences & BioTech Comprehensive Domain Taxonomy
Defines skills, seniority criteria, interview evaluation rubrics, and relational weights.
"""

DOMAIN_NAME = 'Healthcare, Life Sciences & BioTech'
DOMAIN_KEY = 'healthcare_biotech'

TAXONOMY_RECORDS = [
    {
        'id': 'healthcare_biotech_001',
        'canonical_name': 'Health Informatics',
        'category': 'Healthcare, Life Sciences & BioTech',
        'aliases': ['health informatics', 'health-informatics', 'healthinformatics'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Health Informatics syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Health Informatics.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Health Informatics.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Health Informatics.'
        },
        'interview_rubric': [
            'How does Health Informatics handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Health Informatics and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Health Informatics?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': True
    },
    {
        'id': 'healthcare_biotech_002',
        'canonical_name': 'Bioinformatics',
        'category': 'Healthcare, Life Sciences & BioTech',
        'aliases': ['bioinformatics', 'bioinformatics', 'bioinformatics'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Bioinformatics syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Bioinformatics.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Bioinformatics.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Bioinformatics.'
        },
        'interview_rubric': [
            'How does Bioinformatics handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Bioinformatics and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Bioinformatics?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': True
    },
    {
        'id': 'healthcare_biotech_003',
        'canonical_name': 'EHR/EMR Systems',
        'category': 'Healthcare, Life Sciences & BioTech',
        'aliases': ['ehr/emr systems', 'ehr/emr-systems', 'ehr/emrsystems'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of EHR/EMR Systems syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with EHR/EMR Systems.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using EHR/EMR Systems.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing EHR/EMR Systems.'
        },
        'interview_rubric': [
            'How does EHR/EMR Systems handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in EHR/EMR Systems and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling EHR/EMR Systems?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': True
    },
    {
        'id': 'healthcare_biotech_004',
        'canonical_name': 'Epic Systems',
        'category': 'Healthcare, Life Sciences & BioTech',
        'aliases': ['epic systems', 'epic-systems', 'epicsystems'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Epic Systems syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Epic Systems.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Epic Systems.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Epic Systems.'
        },
        'interview_rubric': [
            'How does Epic Systems handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Epic Systems and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Epic Systems?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': True
    },
    {
        'id': 'healthcare_biotech_005',
        'canonical_name': 'Cerner',
        'category': 'Healthcare, Life Sciences & BioTech',
        'aliases': ['cerner', 'cerner', 'cerner'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Cerner syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Cerner.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Cerner.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Cerner.'
        },
        'interview_rubric': [
            'How does Cerner handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Cerner and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Cerner?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': True
    },
    {
        'id': 'healthcare_biotech_006',
        'canonical_name': 'HL7 Standards',
        'category': 'Healthcare, Life Sciences & BioTech',
        'aliases': ['hl7 standards', 'hl7-standards', 'hl7standards'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of HL7 Standards syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with HL7 Standards.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using HL7 Standards.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing HL7 Standards.'
        },
        'interview_rubric': [
            'How does HL7 Standards handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in HL7 Standards and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling HL7 Standards?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': True
    },
    {
        'id': 'healthcare_biotech_007',
        'canonical_name': 'FHIR API Protocol',
        'category': 'Healthcare, Life Sciences & BioTech',
        'aliases': ['fhir api protocol', 'fhir-api-protocol', 'fhirapiprotocol'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of FHIR API Protocol syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with FHIR API Protocol.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using FHIR API Protocol.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing FHIR API Protocol.'
        },
        'interview_rubric': [
            'How does FHIR API Protocol handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in FHIR API Protocol and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling FHIR API Protocol?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': True
    },
    {
        'id': 'healthcare_biotech_008',
        'canonical_name': 'DICOM Imaging',
        'category': 'Healthcare, Life Sciences & BioTech',
        'aliases': ['dicom imaging', 'dicom-imaging', 'dicomimaging'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of DICOM Imaging syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with DICOM Imaging.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using DICOM Imaging.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing DICOM Imaging.'
        },
        'interview_rubric': [
            'How does DICOM Imaging handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in DICOM Imaging and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling DICOM Imaging?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': True
    },
    {
        'id': 'healthcare_biotech_009',
        'canonical_name': 'Clinical Data Management',
        'category': 'Healthcare, Life Sciences & BioTech',
        'aliases': ['clinical data management', 'clinical-data-management', 'clinicaldatamanagement'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Clinical Data Management syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Clinical Data Management.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Clinical Data Management.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Clinical Data Management.'
        },
        'interview_rubric': [
            'How does Clinical Data Management handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Clinical Data Management and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Clinical Data Management?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': True
    },
    {
        'id': 'healthcare_biotech_010',
        'canonical_name': 'Clinical Trials Analysis',
        'category': 'Healthcare, Life Sciences & BioTech',
        'aliases': ['clinical trials analysis', 'clinical-trials-analysis', 'clinicaltrialsanalysis'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Clinical Trials Analysis syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Clinical Trials Analysis.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Clinical Trials Analysis.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Clinical Trials Analysis.'
        },
        'interview_rubric': [
            'How does Clinical Trials Analysis handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Clinical Trials Analysis and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Clinical Trials Analysis?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': True
    },
    {
        'id': 'healthcare_biotech_011',
        'canonical_name': 'Genomic Data Processing',
        'category': 'Healthcare, Life Sciences & BioTech',
        'aliases': ['genomic data processing', 'genomic-data-processing', 'genomicdataprocessing'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Genomic Data Processing syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Genomic Data Processing.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Genomic Data Processing.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Genomic Data Processing.'
        },
        'interview_rubric': [
            'How does Genomic Data Processing handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Genomic Data Processing and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Genomic Data Processing?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': False
    },
    {
        'id': 'healthcare_biotech_012',
        'canonical_name': 'Biostatistics',
        'category': 'Healthcare, Life Sciences & BioTech',
        'aliases': ['biostatistics', 'biostatistics', 'biostatistics'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Biostatistics syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Biostatistics.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Biostatistics.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Biostatistics.'
        },
        'interview_rubric': [
            'How does Biostatistics handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Biostatistics and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Biostatistics?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': False
    },
    {
        'id': 'healthcare_biotech_013',
        'canonical_name': 'R Programming',
        'category': 'Healthcare, Life Sciences & BioTech',
        'aliases': ['r programming', 'r-programming', 'rprogramming'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of R Programming syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with R Programming.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using R Programming.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing R Programming.'
        },
        'interview_rubric': [
            'How does R Programming handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in R Programming and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling R Programming?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': False
    },
    {
        'id': 'healthcare_biotech_014',
        'canonical_name': 'SAS',
        'category': 'Healthcare, Life Sciences & BioTech',
        'aliases': ['sas', 'sas', 'sas'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of SAS syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with SAS.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using SAS.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing SAS.'
        },
        'interview_rubric': [
            'How does SAS handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in SAS and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling SAS?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': False
    },
    {
        'id': 'healthcare_biotech_015',
        'canonical_name': 'SPSS',
        'category': 'Healthcare, Life Sciences & BioTech',
        'aliases': ['spss', 'spss', 'spss'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of SPSS syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with SPSS.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using SPSS.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing SPSS.'
        },
        'interview_rubric': [
            'How does SPSS handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in SPSS and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling SPSS?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': False
    },
    {
        'id': 'healthcare_biotech_016',
        'canonical_name': 'HIPAA Security Rule',
        'category': 'Healthcare, Life Sciences & BioTech',
        'aliases': ['hipaa security rule', 'hipaa-security-rule', 'hipaasecurityrule'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of HIPAA Security Rule syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with HIPAA Security Rule.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using HIPAA Security Rule.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing HIPAA Security Rule.'
        },
        'interview_rubric': [
            'How does HIPAA Security Rule handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in HIPAA Security Rule and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling HIPAA Security Rule?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': False
    },
    {
        'id': 'healthcare_biotech_017',
        'canonical_name': 'FDA 21 CFR Part 11',
        'category': 'Healthcare, Life Sciences & BioTech',
        'aliases': ['fda 21 cfr part 11', 'fda-21-cfr-part-11', 'fda21cfrpart11'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of FDA 21 CFR Part 11 syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with FDA 21 CFR Part 11.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using FDA 21 CFR Part 11.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing FDA 21 CFR Part 11.'
        },
        'interview_rubric': [
            'How does FDA 21 CFR Part 11 handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in FDA 21 CFR Part 11 and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling FDA 21 CFR Part 11?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': False
    },
    {
        'id': 'healthcare_biotech_018',
        'canonical_name': 'Medical Device Software (SaMD)',
        'category': 'Healthcare, Life Sciences & BioTech',
        'aliases': ['medical device software (samd)', 'medical-device-software-(samd)', 'medicaldevicesoftware(samd)'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Medical Device Software (SaMD) syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Medical Device Software (SaMD).',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Medical Device Software (SaMD).',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Medical Device Software (SaMD).'
        },
        'interview_rubric': [
            'How does Medical Device Software (SaMD) handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Medical Device Software (SaMD) and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Medical Device Software (SaMD)?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': False
    },
    {
        'id': 'healthcare_biotech_019',
        'canonical_name': 'Telemedicine Platforms',
        'category': 'Healthcare, Life Sciences & BioTech',
        'aliases': ['telemedicine platforms', 'telemedicine-platforms', 'telemedicineplatforms'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Telemedicine Platforms syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Telemedicine Platforms.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Telemedicine Platforms.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Telemedicine Platforms.'
        },
        'interview_rubric': [
            'How does Telemedicine Platforms handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Telemedicine Platforms and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Telemedicine Platforms?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': False
    },
    {
        'id': 'healthcare_biotech_020',
        'canonical_name': 'Medical Coding (ICD-10, CPT)',
        'category': 'Healthcare, Life Sciences & BioTech',
        'aliases': ['medical coding (icd-10, cpt)', 'medical-coding-(icd-10,-cpt)', 'medicalcoding(icd-10,cpt)'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Medical Coding (ICD-10, CPT) syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Medical Coding (ICD-10, CPT).',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Medical Coding (ICD-10, CPT).',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Medical Coding (ICD-10, CPT).'
        },
        'interview_rubric': [
            'How does Medical Coding (ICD-10, CPT) handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Medical Coding (ICD-10, CPT) and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Medical Coding (ICD-10, CPT)?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': False
    },
    {
        'id': 'healthcare_biotech_021',
        'canonical_name': 'Public Health Analytics',
        'category': 'Healthcare, Life Sciences & BioTech',
        'aliases': ['public health analytics', 'public-health-analytics', 'publichealthanalytics'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Public Health Analytics syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Public Health Analytics.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Public Health Analytics.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Public Health Analytics.'
        },
        'interview_rubric': [
            'How does Public Health Analytics handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Public Health Analytics and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Public Health Analytics?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': False
    },
    {
        'id': 'healthcare_biotech_022',
        'canonical_name': 'Drug Discovery ML',
        'category': 'Healthcare, Life Sciences & BioTech',
        'aliases': ['drug discovery ml', 'drug-discovery-ml', 'drugdiscoveryml'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Drug Discovery ML syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Drug Discovery ML.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Drug Discovery ML.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Drug Discovery ML.'
        },
        'interview_rubric': [
            'How does Drug Discovery ML handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Drug Discovery ML and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Drug Discovery ML?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': False
    },
    {
        'id': 'healthcare_biotech_023',
        'canonical_name': 'Computational Biology',
        'category': 'Healthcare, Life Sciences & BioTech',
        'aliases': ['computational biology', 'computational-biology', 'computationalbiology'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Computational Biology syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Computational Biology.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Computational Biology.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Computational Biology.'
        },
        'interview_rubric': [
            'How does Computational Biology handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Computational Biology and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Computational Biology?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': False
    },
    {
        'id': 'healthcare_biotech_024',
        'canonical_name': 'Next-Generation Sequencing (NGS)',
        'category': 'Healthcare, Life Sciences & BioTech',
        'aliases': ['next-generation sequencing (ngs)', 'next-generation-sequencing-(ngs)', 'next-generationsequencing(ngs)'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Next-Generation Sequencing (NGS) syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Next-Generation Sequencing (NGS).',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Next-Generation Sequencing (NGS).',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Next-Generation Sequencing (NGS).'
        },
        'interview_rubric': [
            'How does Next-Generation Sequencing (NGS) handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Next-Generation Sequencing (NGS) and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Next-Generation Sequencing (NGS)?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': False
    },
    {
        'id': 'healthcare_biotech_025',
        'canonical_name': 'Pharmacovigilance',
        'category': 'Healthcare, Life Sciences & BioTech',
        'aliases': ['pharmacovigilance', 'pharmacovigilance', 'pharmacovigilance'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Pharmacovigilance syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Pharmacovigilance.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Pharmacovigilance.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Pharmacovigilance.'
        },
        'interview_rubric': [
            'How does Pharmacovigilance handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Pharmacovigilance and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Pharmacovigilance?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': False
    },
    {
        'id': 'healthcare_biotech_026',
        'canonical_name': 'Healthcare Interoperability',
        'category': 'Healthcare, Life Sciences & BioTech',
        'aliases': ['healthcare interoperability', 'healthcare-interoperability', 'healthcareinteroperability'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Healthcare Interoperability syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Healthcare Interoperability.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Healthcare Interoperability.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Healthcare Interoperability.'
        },
        'interview_rubric': [
            'How does Healthcare Interoperability handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Healthcare Interoperability and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Healthcare Interoperability?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': False
    },
    {
        'id': 'healthcare_biotech_027',
        'canonical_name': 'Life Sciences Compliance',
        'category': 'Healthcare, Life Sciences & BioTech',
        'aliases': ['life sciences compliance', 'life-sciences-compliance', 'lifesciencescompliance'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Life Sciences Compliance syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Life Sciences Compliance.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Life Sciences Compliance.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Life Sciences Compliance.'
        },
        'interview_rubric': [
            'How does Life Sciences Compliance handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Life Sciences Compliance and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Life Sciences Compliance?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': False
    },
    {
        'id': 'healthcare_biotech_028',
        'canonical_name': 'Clinical Workflow Optimization',
        'category': 'Healthcare, Life Sciences & BioTech',
        'aliases': ['clinical workflow optimization', 'clinical-workflow-optimization', 'clinicalworkflowoptimization'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Clinical Workflow Optimization syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Clinical Workflow Optimization.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Clinical Workflow Optimization.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Clinical Workflow Optimization.'
        },
        'interview_rubric': [
            'How does Clinical Workflow Optimization handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Clinical Workflow Optimization and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Clinical Workflow Optimization?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': False
    },
    {
        'id': 'healthcare_biotech_029',
        'canonical_name': 'Patient Safety Systems',
        'category': 'Healthcare, Life Sciences & BioTech',
        'aliases': ['patient safety systems', 'patient-safety-systems', 'patientsafetysystems'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Patient Safety Systems syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Patient Safety Systems.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Patient Safety Systems.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Patient Safety Systems.'
        },
        'interview_rubric': [
            'How does Patient Safety Systems handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Patient Safety Systems and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Patient Safety Systems?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': False
    },
]


def get_healthcare_biotech_skill_map() -> dict:
    return {item['canonical_name']: item for item in TAXONOMY_RECORDS}

def get_healthcare_biotech_aliases_lookup() -> dict:
    lookup = {}
    for item in TAXONOMY_RECORDS:
        for alias in item['aliases']:
            lookup[alias.lower()] = item['canonical_name']
    return lookup
