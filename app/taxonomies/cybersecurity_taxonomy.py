"""
TalentNexus AI - Information Security & Compliance Comprehensive Domain Taxonomy
Defines skills, seniority criteria, interview evaluation rubrics, and relational weights.
"""

DOMAIN_NAME = 'Information Security & Compliance'
DOMAIN_KEY = 'cybersecurity'

TAXONOMY_RECORDS = [
    {
        'id': 'cybersecurity_001',
        'canonical_name': 'Application Security',
        'category': 'Information Security & Compliance',
        'aliases': ['application security', 'application-security', 'applicationsecurity'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Application Security syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Application Security.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Application Security.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Application Security.'
        },
        'interview_rubric': [
            'How does Application Security handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Application Security and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Application Security?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': True
    },
    {
        'id': 'cybersecurity_002',
        'canonical_name': 'Penetration Testing',
        'category': 'Information Security & Compliance',
        'aliases': ['penetration testing', 'penetration-testing', 'penetrationtesting'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Penetration Testing syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Penetration Testing.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Penetration Testing.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Penetration Testing.'
        },
        'interview_rubric': [
            'How does Penetration Testing handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Penetration Testing and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Penetration Testing?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': True
    },
    {
        'id': 'cybersecurity_003',
        'canonical_name': 'Vulnerability Assessment',
        'category': 'Information Security & Compliance',
        'aliases': ['vulnerability assessment', 'vulnerability-assessment', 'vulnerabilityassessment'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Vulnerability Assessment syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Vulnerability Assessment.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Vulnerability Assessment.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Vulnerability Assessment.'
        },
        'interview_rubric': [
            'How does Vulnerability Assessment handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Vulnerability Assessment and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Vulnerability Assessment?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': True
    },
    {
        'id': 'cybersecurity_004',
        'canonical_name': 'OWASP Top 10',
        'category': 'Information Security & Compliance',
        'aliases': ['owasp top 10', 'owasp-top-10', 'owasptop10'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of OWASP Top 10 syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with OWASP Top 10.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using OWASP Top 10.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing OWASP Top 10.'
        },
        'interview_rubric': [
            'How does OWASP Top 10 handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in OWASP Top 10 and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling OWASP Top 10?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': True
    },
    {
        'id': 'cybersecurity_005',
        'canonical_name': 'Network Security',
        'category': 'Information Security & Compliance',
        'aliases': ['network security', 'network-security', 'networksecurity'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Network Security syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Network Security.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Network Security.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Network Security.'
        },
        'interview_rubric': [
            'How does Network Security handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Network Security and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Network Security?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': True
    },
    {
        'id': 'cybersecurity_006',
        'canonical_name': 'Cloud Security',
        'category': 'Information Security & Compliance',
        'aliases': ['cloud security', 'cloud-security', 'cloudsecurity'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Cloud Security syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Cloud Security.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Cloud Security.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Cloud Security.'
        },
        'interview_rubric': [
            'How does Cloud Security handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Cloud Security and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Cloud Security?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': True
    },
    {
        'id': 'cybersecurity_007',
        'canonical_name': 'SIEM',
        'category': 'Information Security & Compliance',
        'aliases': ['siem', 'siem', 'siem'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of SIEM syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with SIEM.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using SIEM.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing SIEM.'
        },
        'interview_rubric': [
            'How does SIEM handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in SIEM and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling SIEM?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': True
    },
    {
        'id': 'cybersecurity_008',
        'canonical_name': 'Splunk',
        'category': 'Information Security & Compliance',
        'aliases': ['splunk', 'splunk', 'splunk'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Splunk syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Splunk.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Splunk.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Splunk.'
        },
        'interview_rubric': [
            'How does Splunk handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Splunk and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Splunk?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': True
    },
    {
        'id': 'cybersecurity_009',
        'canonical_name': 'CrowdStrike',
        'category': 'Information Security & Compliance',
        'aliases': ['crowdstrike', 'crowdstrike', 'crowdstrike'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of CrowdStrike syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with CrowdStrike.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using CrowdStrike.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing CrowdStrike.'
        },
        'interview_rubric': [
            'How does CrowdStrike handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in CrowdStrike and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling CrowdStrike?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': True
    },
    {
        'id': 'cybersecurity_010',
        'canonical_name': 'SOC 2 Compliance',
        'category': 'Information Security & Compliance',
        'aliases': ['soc 2 compliance', 'soc-2-compliance', 'soc2compliance'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of SOC 2 Compliance syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with SOC 2 Compliance.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using SOC 2 Compliance.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing SOC 2 Compliance.'
        },
        'interview_rubric': [
            'How does SOC 2 Compliance handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in SOC 2 Compliance and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling SOC 2 Compliance?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': True
    },
    {
        'id': 'cybersecurity_011',
        'canonical_name': 'ISO 27001',
        'category': 'Information Security & Compliance',
        'aliases': ['iso 27001', 'iso-27001', 'iso27001'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of ISO 27001 syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with ISO 27001.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using ISO 27001.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing ISO 27001.'
        },
        'interview_rubric': [
            'How does ISO 27001 handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in ISO 27001 and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling ISO 27001?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': False
    },
    {
        'id': 'cybersecurity_012',
        'canonical_name': 'GDPR',
        'category': 'Information Security & Compliance',
        'aliases': ['gdpr', 'gdpr', 'gdpr'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of GDPR syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with GDPR.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using GDPR.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing GDPR.'
        },
        'interview_rubric': [
            'How does GDPR handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in GDPR and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling GDPR?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': False
    },
    {
        'id': 'cybersecurity_013',
        'canonical_name': 'HIPAA',
        'category': 'Information Security & Compliance',
        'aliases': ['hipaa', 'hipaa', 'hipaa'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of HIPAA syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with HIPAA.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using HIPAA.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing HIPAA.'
        },
        'interview_rubric': [
            'How does HIPAA handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in HIPAA and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling HIPAA?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': False
    },
    {
        'id': 'cybersecurity_014',
        'canonical_name': 'PCI-DSS',
        'category': 'Information Security & Compliance',
        'aliases': ['pci-dss', 'pci-dss', 'pci-dss'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of PCI-DSS syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with PCI-DSS.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using PCI-DSS.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing PCI-DSS.'
        },
        'interview_rubric': [
            'How does PCI-DSS handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in PCI-DSS and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling PCI-DSS?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': False
    },
    {
        'id': 'cybersecurity_015',
        'canonical_name': 'Cryptography',
        'category': 'Information Security & Compliance',
        'aliases': ['cryptography', 'cryptography', 'cryptography'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Cryptography syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Cryptography.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Cryptography.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Cryptography.'
        },
        'interview_rubric': [
            'How does Cryptography handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Cryptography and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Cryptography?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': False
    },
    {
        'id': 'cybersecurity_016',
        'canonical_name': 'PKI/Certificates',
        'category': 'Information Security & Compliance',
        'aliases': ['pki/certificates', 'pki/certificates', 'pki/certificates'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of PKI/Certificates syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with PKI/Certificates.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using PKI/Certificates.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing PKI/Certificates.'
        },
        'interview_rubric': [
            'How does PKI/Certificates handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in PKI/Certificates and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling PKI/Certificates?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': False
    },
    {
        'id': 'cybersecurity_017',
        'canonical_name': 'Identity & Access Management (IAM)',
        'category': 'Information Security & Compliance',
        'aliases': ['identity & access management (iam)', 'identity-&-access-management-(iam)', 'identity&accessmanagement(iam)'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Identity & Access Management (IAM) syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Identity & Access Management (IAM).',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Identity & Access Management (IAM).',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Identity & Access Management (IAM).'
        },
        'interview_rubric': [
            'How does Identity & Access Management (IAM) handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Identity & Access Management (IAM) and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Identity & Access Management (IAM)?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': False
    },
    {
        'id': 'cybersecurity_018',
        'canonical_name': 'Privileged Access Management (PAM)',
        'category': 'Information Security & Compliance',
        'aliases': ['privileged access management (pam)', 'privileged-access-management-(pam)', 'privilegedaccessmanagement(pam)'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Privileged Access Management (PAM) syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Privileged Access Management (PAM).',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Privileged Access Management (PAM).',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Privileged Access Management (PAM).'
        },
        'interview_rubric': [
            'How does Privileged Access Management (PAM) handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Privileged Access Management (PAM) and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Privileged Access Management (PAM)?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': False
    },
    {
        'id': 'cybersecurity_019',
        'canonical_name': 'Firewalls',
        'category': 'Information Security & Compliance',
        'aliases': ['firewalls', 'firewalls', 'firewalls'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Firewalls syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Firewalls.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Firewalls.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Firewalls.'
        },
        'interview_rubric': [
            'How does Firewalls handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Firewalls and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Firewalls?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': False
    },
    {
        'id': 'cybersecurity_020',
        'canonical_name': 'IDS/IPS',
        'category': 'Information Security & Compliance',
        'aliases': ['ids/ips', 'ids/ips', 'ids/ips'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of IDS/IPS syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with IDS/IPS.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using IDS/IPS.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing IDS/IPS.'
        },
        'interview_rubric': [
            'How does IDS/IPS handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in IDS/IPS and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling IDS/IPS?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': False
    },
    {
        'id': 'cybersecurity_021',
        'canonical_name': 'Incident Response',
        'category': 'Information Security & Compliance',
        'aliases': ['incident response', 'incident-response', 'incidentresponse'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Incident Response syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Incident Response.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Incident Response.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Incident Response.'
        },
        'interview_rubric': [
            'How does Incident Response handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Incident Response and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Incident Response?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': False
    },
    {
        'id': 'cybersecurity_022',
        'canonical_name': 'Threat Modeling',
        'category': 'Information Security & Compliance',
        'aliases': ['threat modeling', 'threat-modeling', 'threatmodeling'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Threat Modeling syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Threat Modeling.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Threat Modeling.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Threat Modeling.'
        },
        'interview_rubric': [
            'How does Threat Modeling handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Threat Modeling and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Threat Modeling?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': False
    },
    {
        'id': 'cybersecurity_023',
        'canonical_name': 'Static Analysis (SAST)',
        'category': 'Information Security & Compliance',
        'aliases': ['static analysis (sast)', 'static-analysis-(sast)', 'staticanalysis(sast)'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Static Analysis (SAST) syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Static Analysis (SAST).',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Static Analysis (SAST).',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Static Analysis (SAST).'
        },
        'interview_rubric': [
            'How does Static Analysis (SAST) handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Static Analysis (SAST) and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Static Analysis (SAST)?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': False
    },
    {
        'id': 'cybersecurity_024',
        'canonical_name': 'Dynamic Analysis (DAST)',
        'category': 'Information Security & Compliance',
        'aliases': ['dynamic analysis (dast)', 'dynamic-analysis-(dast)', 'dynamicanalysis(dast)'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Dynamic Analysis (DAST) syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Dynamic Analysis (DAST).',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Dynamic Analysis (DAST).',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Dynamic Analysis (DAST).'
        },
        'interview_rubric': [
            'How does Dynamic Analysis (DAST) handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Dynamic Analysis (DAST) and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Dynamic Analysis (DAST)?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': False
    },
    {
        'id': 'cybersecurity_025',
        'canonical_name': 'Software Composition Analysis (SCA)',
        'category': 'Information Security & Compliance',
        'aliases': ['software composition analysis (sca)', 'software-composition-analysis-(sca)', 'softwarecompositionanalysis(sca)'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Software Composition Analysis (SCA) syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Software Composition Analysis (SCA).',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Software Composition Analysis (SCA).',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Software Composition Analysis (SCA).'
        },
        'interview_rubric': [
            'How does Software Composition Analysis (SCA) handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Software Composition Analysis (SCA) and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Software Composition Analysis (SCA)?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': False
    },
    {
        'id': 'cybersecurity_026',
        'canonical_name': 'Zero Trust',
        'category': 'Information Security & Compliance',
        'aliases': ['zero trust', 'zero-trust', 'zerotrust'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Zero Trust syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Zero Trust.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Zero Trust.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Zero Trust.'
        },
        'interview_rubric': [
            'How does Zero Trust handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Zero Trust and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Zero Trust?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': False
    },
    {
        'id': 'cybersecurity_027',
        'canonical_name': 'Endpoint Detection & Response (EDR)',
        'category': 'Information Security & Compliance',
        'aliases': ['endpoint detection & response (edr)', 'endpoint-detection-&-response-(edr)', 'endpointdetection&response(edr)'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Endpoint Detection & Response (EDR) syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Endpoint Detection & Response (EDR).',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Endpoint Detection & Response (EDR).',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Endpoint Detection & Response (EDR).'
        },
        'interview_rubric': [
            'How does Endpoint Detection & Response (EDR) handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Endpoint Detection & Response (EDR) and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Endpoint Detection & Response (EDR)?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': False
    },
    {
        'id': 'cybersecurity_028',
        'canonical_name': 'Security Auditing',
        'category': 'Information Security & Compliance',
        'aliases': ['security auditing', 'security-auditing', 'securityauditing'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Security Auditing syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Security Auditing.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Security Auditing.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Security Auditing.'
        },
        'interview_rubric': [
            'How does Security Auditing handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Security Auditing and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Security Auditing?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': False
    },
    {
        'id': 'cybersecurity_029',
        'canonical_name': 'Forensics',
        'category': 'Information Security & Compliance',
        'aliases': ['forensics', 'forensics', 'forensics'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Forensics syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Forensics.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Forensics.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Forensics.'
        },
        'interview_rubric': [
            'How does Forensics handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Forensics and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Forensics?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': False
    },
    {
        'id': 'cybersecurity_030',
        'canonical_name': 'Secure Code Review',
        'category': 'Information Security & Compliance',
        'aliases': ['secure code review', 'secure-code-review', 'securecodereview'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Secure Code Review syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Secure Code Review.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Secure Code Review.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Secure Code Review.'
        },
        'interview_rubric': [
            'How does Secure Code Review handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Secure Code Review and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Secure Code Review?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': False
    },
]


def get_cybersecurity_skill_map() -> dict:
    return {item['canonical_name']: item for item in TAXONOMY_RECORDS}

def get_cybersecurity_aliases_lookup() -> dict:
    lookup = {}
    for item in TAXONOMY_RECORDS:
        for alias in item['aliases']:
            lookup[alias.lower()] = item['canonical_name']
    return lookup
