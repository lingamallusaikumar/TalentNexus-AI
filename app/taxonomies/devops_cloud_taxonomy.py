"""
TalentNexus AI - Cloud, DevOps & Infrastructure Comprehensive Domain Taxonomy
Defines skills, seniority criteria, interview evaluation rubrics, and relational weights.
"""

DOMAIN_NAME = 'Cloud, DevOps & Infrastructure'
DOMAIN_KEY = 'devops_cloud'

TAXONOMY_RECORDS = [
    {
        'id': 'devops_cloud_001',
        'canonical_name': 'Docker',
        'category': 'Cloud, DevOps & Infrastructure',
        'aliases': ['docker', 'docker', 'docker'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Docker syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Docker.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Docker.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Docker.'
        },
        'interview_rubric': [
            'How does Docker handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Docker and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Docker?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': True
    },
    {
        'id': 'devops_cloud_002',
        'canonical_name': 'Kubernetes',
        'category': 'Cloud, DevOps & Infrastructure',
        'aliases': ['kubernetes', 'kubernetes', 'kubernetes'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Kubernetes syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Kubernetes.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Kubernetes.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Kubernetes.'
        },
        'interview_rubric': [
            'How does Kubernetes handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Kubernetes and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Kubernetes?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': True
    },
    {
        'id': 'devops_cloud_003',
        'canonical_name': 'Helm',
        'category': 'Cloud, DevOps & Infrastructure',
        'aliases': ['helm', 'helm', 'helm'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Helm syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Helm.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Helm.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Helm.'
        },
        'interview_rubric': [
            'How does Helm handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Helm and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Helm?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': True
    },
    {
        'id': 'devops_cloud_004',
        'canonical_name': 'Terraform',
        'category': 'Cloud, DevOps & Infrastructure',
        'aliases': ['terraform', 'terraform', 'terraform'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Terraform syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Terraform.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Terraform.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Terraform.'
        },
        'interview_rubric': [
            'How does Terraform handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Terraform and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Terraform?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': True
    },
    {
        'id': 'devops_cloud_005',
        'canonical_name': 'Ansible',
        'category': 'Cloud, DevOps & Infrastructure',
        'aliases': ['ansible', 'ansible', 'ansible'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Ansible syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Ansible.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Ansible.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Ansible.'
        },
        'interview_rubric': [
            'How does Ansible handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Ansible and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Ansible?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': True
    },
    {
        'id': 'devops_cloud_006',
        'canonical_name': 'Puppet',
        'category': 'Cloud, DevOps & Infrastructure',
        'aliases': ['puppet', 'puppet', 'puppet'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Puppet syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Puppet.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Puppet.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Puppet.'
        },
        'interview_rubric': [
            'How does Puppet handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Puppet and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Puppet?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': True
    },
    {
        'id': 'devops_cloud_007',
        'canonical_name': 'Chef',
        'category': 'Cloud, DevOps & Infrastructure',
        'aliases': ['chef', 'chef', 'chef'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Chef syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Chef.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Chef.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Chef.'
        },
        'interview_rubric': [
            'How does Chef handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Chef and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Chef?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': True
    },
    {
        'id': 'devops_cloud_008',
        'canonical_name': 'AWS',
        'category': 'Cloud, DevOps & Infrastructure',
        'aliases': ['aws', 'aws', 'aws'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of AWS syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with AWS.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using AWS.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing AWS.'
        },
        'interview_rubric': [
            'How does AWS handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in AWS and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling AWS?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': True
    },
    {
        'id': 'devops_cloud_009',
        'canonical_name': 'Google Cloud Platform (GCP)',
        'category': 'Cloud, DevOps & Infrastructure',
        'aliases': ['google cloud platform (gcp)', 'google-cloud-platform-(gcp)', 'googlecloudplatform(gcp)'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Google Cloud Platform (GCP) syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Google Cloud Platform (GCP).',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Google Cloud Platform (GCP).',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Google Cloud Platform (GCP).'
        },
        'interview_rubric': [
            'How does Google Cloud Platform (GCP) handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Google Cloud Platform (GCP) and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Google Cloud Platform (GCP)?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': True
    },
    {
        'id': 'devops_cloud_010',
        'canonical_name': 'Microsoft Azure',
        'category': 'Cloud, DevOps & Infrastructure',
        'aliases': ['microsoft azure', 'microsoft-azure', 'microsoftazure'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Microsoft Azure syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Microsoft Azure.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Microsoft Azure.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Microsoft Azure.'
        },
        'interview_rubric': [
            'How does Microsoft Azure handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Microsoft Azure and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Microsoft Azure?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': True
    },
    {
        'id': 'devops_cloud_011',
        'canonical_name': 'AWS Lambda',
        'category': 'Cloud, DevOps & Infrastructure',
        'aliases': ['aws lambda', 'aws-lambda', 'awslambda'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of AWS Lambda syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with AWS Lambda.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using AWS Lambda.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing AWS Lambda.'
        },
        'interview_rubric': [
            'How does AWS Lambda handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in AWS Lambda and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling AWS Lambda?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': False
    },
    {
        'id': 'devops_cloud_012',
        'canonical_name': 'Serverless Framework',
        'category': 'Cloud, DevOps & Infrastructure',
        'aliases': ['serverless framework', 'serverless-framework', 'serverlessframework'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Serverless Framework syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Serverless Framework.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Serverless Framework.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Serverless Framework.'
        },
        'interview_rubric': [
            'How does Serverless Framework handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Serverless Framework and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Serverless Framework?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': False
    },
    {
        'id': 'devops_cloud_013',
        'canonical_name': 'CI/CD Pipelines',
        'category': 'Cloud, DevOps & Infrastructure',
        'aliases': ['ci/cd pipelines', 'ci/cd-pipelines', 'ci/cdpipelines'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of CI/CD Pipelines syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with CI/CD Pipelines.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using CI/CD Pipelines.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing CI/CD Pipelines.'
        },
        'interview_rubric': [
            'How does CI/CD Pipelines handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in CI/CD Pipelines and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling CI/CD Pipelines?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': False
    },
    {
        'id': 'devops_cloud_014',
        'canonical_name': 'GitHub Actions',
        'category': 'Cloud, DevOps & Infrastructure',
        'aliases': ['github actions', 'github-actions', 'githubactions'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of GitHub Actions syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with GitHub Actions.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using GitHub Actions.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing GitHub Actions.'
        },
        'interview_rubric': [
            'How does GitHub Actions handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in GitHub Actions and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling GitHub Actions?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': False
    },
    {
        'id': 'devops_cloud_015',
        'canonical_name': 'GitLab CI',
        'category': 'Cloud, DevOps & Infrastructure',
        'aliases': ['gitlab ci', 'gitlab-ci', 'gitlabci'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of GitLab CI syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with GitLab CI.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using GitLab CI.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing GitLab CI.'
        },
        'interview_rubric': [
            'How does GitLab CI handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in GitLab CI and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling GitLab CI?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': False
    },
    {
        'id': 'devops_cloud_016',
        'canonical_name': 'Jenkins',
        'category': 'Cloud, DevOps & Infrastructure',
        'aliases': ['jenkins', 'jenkins', 'jenkins'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Jenkins syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Jenkins.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Jenkins.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Jenkins.'
        },
        'interview_rubric': [
            'How does Jenkins handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Jenkins and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Jenkins?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': False
    },
    {
        'id': 'devops_cloud_017',
        'canonical_name': 'CircleCI',
        'category': 'Cloud, DevOps & Infrastructure',
        'aliases': ['circleci', 'circleci', 'circleci'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of CircleCI syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with CircleCI.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using CircleCI.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing CircleCI.'
        },
        'interview_rubric': [
            'How does CircleCI handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in CircleCI and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling CircleCI?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': False
    },
    {
        'id': 'devops_cloud_018',
        'canonical_name': 'ArgoCD',
        'category': 'Cloud, DevOps & Infrastructure',
        'aliases': ['argocd', 'argocd', 'argocd'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of ArgoCD syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with ArgoCD.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using ArgoCD.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing ArgoCD.'
        },
        'interview_rubric': [
            'How does ArgoCD handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in ArgoCD and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling ArgoCD?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': False
    },
    {
        'id': 'devops_cloud_019',
        'canonical_name': 'Prometheus',
        'category': 'Cloud, DevOps & Infrastructure',
        'aliases': ['prometheus', 'prometheus', 'prometheus'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Prometheus syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Prometheus.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Prometheus.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Prometheus.'
        },
        'interview_rubric': [
            'How does Prometheus handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Prometheus and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Prometheus?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': False
    },
    {
        'id': 'devops_cloud_020',
        'canonical_name': 'Grafana',
        'category': 'Cloud, DevOps & Infrastructure',
        'aliases': ['grafana', 'grafana', 'grafana'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Grafana syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Grafana.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Grafana.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Grafana.'
        },
        'interview_rubric': [
            'How does Grafana handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Grafana and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Grafana?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': False
    },
    {
        'id': 'devops_cloud_021',
        'canonical_name': 'Datadog',
        'category': 'Cloud, DevOps & Infrastructure',
        'aliases': ['datadog', 'datadog', 'datadog'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Datadog syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Datadog.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Datadog.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Datadog.'
        },
        'interview_rubric': [
            'How does Datadog handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Datadog and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Datadog?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': False
    },
    {
        'id': 'devops_cloud_022',
        'canonical_name': 'New Relic',
        'category': 'Cloud, DevOps & Infrastructure',
        'aliases': ['new relic', 'new-relic', 'newrelic'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of New Relic syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with New Relic.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using New Relic.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing New Relic.'
        },
        'interview_rubric': [
            'How does New Relic handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in New Relic and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling New Relic?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': False
    },
    {
        'id': 'devops_cloud_023',
        'canonical_name': 'ELK Stack',
        'category': 'Cloud, DevOps & Infrastructure',
        'aliases': ['elk stack', 'elk-stack', 'elkstack'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of ELK Stack syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with ELK Stack.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using ELK Stack.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing ELK Stack.'
        },
        'interview_rubric': [
            'How does ELK Stack handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in ELK Stack and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling ELK Stack?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': False
    },
    {
        'id': 'devops_cloud_024',
        'canonical_name': 'Loki',
        'category': 'Cloud, DevOps & Infrastructure',
        'aliases': ['loki', 'loki', 'loki'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Loki syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Loki.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Loki.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Loki.'
        },
        'interview_rubric': [
            'How does Loki handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Loki and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Loki?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': False
    },
    {
        'id': 'devops_cloud_025',
        'canonical_name': 'OpenTelemetry',
        'category': 'Cloud, DevOps & Infrastructure',
        'aliases': ['opentelemetry', 'opentelemetry', 'opentelemetry'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of OpenTelemetry syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with OpenTelemetry.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using OpenTelemetry.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing OpenTelemetry.'
        },
        'interview_rubric': [
            'How does OpenTelemetry handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in OpenTelemetry and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling OpenTelemetry?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': False
    },
    {
        'id': 'devops_cloud_026',
        'canonical_name': 'Linux/Unix Administration',
        'category': 'Cloud, DevOps & Infrastructure',
        'aliases': ['linux/unix administration', 'linux/unix-administration', 'linux/unixadministration'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Linux/Unix Administration syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Linux/Unix Administration.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Linux/Unix Administration.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Linux/Unix Administration.'
        },
        'interview_rubric': [
            'How does Linux/Unix Administration handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Linux/Unix Administration and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Linux/Unix Administration?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': False
    },
    {
        'id': 'devops_cloud_027',
        'canonical_name': 'Bash Scripting',
        'category': 'Cloud, DevOps & Infrastructure',
        'aliases': ['bash scripting', 'bash-scripting', 'bashscripting'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Bash Scripting syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Bash Scripting.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Bash Scripting.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Bash Scripting.'
        },
        'interview_rubric': [
            'How does Bash Scripting handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Bash Scripting and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Bash Scripting?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': False
    },
    {
        'id': 'devops_cloud_028',
        'canonical_name': 'Nginx',
        'category': 'Cloud, DevOps & Infrastructure',
        'aliases': ['nginx', 'nginx', 'nginx'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Nginx syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Nginx.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Nginx.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Nginx.'
        },
        'interview_rubric': [
            'How does Nginx handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Nginx and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Nginx?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': False
    },
    {
        'id': 'devops_cloud_029',
        'canonical_name': 'Apache HTTP Server',
        'category': 'Cloud, DevOps & Infrastructure',
        'aliases': ['apache http server', 'apache-http-server', 'apachehttpserver'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Apache HTTP Server syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Apache HTTP Server.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Apache HTTP Server.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Apache HTTP Server.'
        },
        'interview_rubric': [
            'How does Apache HTTP Server handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Apache HTTP Server and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Apache HTTP Server?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': False
    },
    {
        'id': 'devops_cloud_030',
        'canonical_name': 'HAProxy',
        'category': 'Cloud, DevOps & Infrastructure',
        'aliases': ['haproxy', 'haproxy', 'haproxy'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of HAProxy syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with HAProxy.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using HAProxy.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing HAProxy.'
        },
        'interview_rubric': [
            'How does HAProxy handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in HAProxy and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling HAProxy?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': False
    },
    {
        'id': 'devops_cloud_031',
        'canonical_name': 'Envoy Proxy',
        'category': 'Cloud, DevOps & Infrastructure',
        'aliases': ['envoy proxy', 'envoy-proxy', 'envoyproxy'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Envoy Proxy syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Envoy Proxy.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Envoy Proxy.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Envoy Proxy.'
        },
        'interview_rubric': [
            'How does Envoy Proxy handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Envoy Proxy and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Envoy Proxy?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': False
    },
    {
        'id': 'devops_cloud_032',
        'canonical_name': 'Istio Service Mesh',
        'category': 'Cloud, DevOps & Infrastructure',
        'aliases': ['istio service mesh', 'istio-service-mesh', 'istioservicemesh'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Istio Service Mesh syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Istio Service Mesh.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Istio Service Mesh.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Istio Service Mesh.'
        },
        'interview_rubric': [
            'How does Istio Service Mesh handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Istio Service Mesh and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Istio Service Mesh?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': False
    },
    {
        'id': 'devops_cloud_033',
        'canonical_name': 'Cloudflare',
        'category': 'Cloud, DevOps & Infrastructure',
        'aliases': ['cloudflare', 'cloudflare', 'cloudflare'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Cloudflare syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Cloudflare.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Cloudflare.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Cloudflare.'
        },
        'interview_rubric': [
            'How does Cloudflare handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Cloudflare and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Cloudflare?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': False
    },
    {
        'id': 'devops_cloud_034',
        'canonical_name': 'CDN Management',
        'category': 'Cloud, DevOps & Infrastructure',
        'aliases': ['cdn management', 'cdn-management', 'cdnmanagement'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of CDN Management syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with CDN Management.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using CDN Management.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing CDN Management.'
        },
        'interview_rubric': [
            'How does CDN Management handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in CDN Management and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling CDN Management?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': False
    },
    {
        'id': 'devops_cloud_035',
        'canonical_name': 'DNS Configuration',
        'category': 'Cloud, DevOps & Infrastructure',
        'aliases': ['dns configuration', 'dns-configuration', 'dnsconfiguration'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of DNS Configuration syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with DNS Configuration.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using DNS Configuration.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing DNS Configuration.'
        },
        'interview_rubric': [
            'How does DNS Configuration handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in DNS Configuration and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling DNS Configuration?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': False
    },
    {
        'id': 'devops_cloud_036',
        'canonical_name': 'Infrastructure as Code (IaC)',
        'category': 'Cloud, DevOps & Infrastructure',
        'aliases': ['infrastructure as code (iac)', 'infrastructure-as-code-(iac)', 'infrastructureascode(iac)'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Infrastructure as Code (IaC) syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Infrastructure as Code (IaC).',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Infrastructure as Code (IaC).',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Infrastructure as Code (IaC).'
        },
        'interview_rubric': [
            'How does Infrastructure as Code (IaC) handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Infrastructure as Code (IaC) and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Infrastructure as Code (IaC)?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': False
    },
    {
        'id': 'devops_cloud_037',
        'canonical_name': 'Site Reliability Engineering (SRE)',
        'category': 'Cloud, DevOps & Infrastructure',
        'aliases': ['site reliability engineering (sre)', 'site-reliability-engineering-(sre)', 'sitereliabilityengineering(sre)'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Site Reliability Engineering (SRE) syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Site Reliability Engineering (SRE).',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Site Reliability Engineering (SRE).',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Site Reliability Engineering (SRE).'
        },
        'interview_rubric': [
            'How does Site Reliability Engineering (SRE) handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Site Reliability Engineering (SRE) and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Site Reliability Engineering (SRE)?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': False
    },
    {
        'id': 'devops_cloud_038',
        'canonical_name': 'Disaster Recovery',
        'category': 'Cloud, DevOps & Infrastructure',
        'aliases': ['disaster recovery', 'disaster-recovery', 'disasterrecovery'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Disaster Recovery syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Disaster Recovery.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Disaster Recovery.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Disaster Recovery.'
        },
        'interview_rubric': [
            'How does Disaster Recovery handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Disaster Recovery and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Disaster Recovery?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': False
    },
    {
        'id': 'devops_cloud_039',
        'canonical_name': 'Zero Trust Architecture',
        'category': 'Cloud, DevOps & Infrastructure',
        'aliases': ['zero trust architecture', 'zero-trust-architecture', 'zerotrustarchitecture'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Zero Trust Architecture syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Zero Trust Architecture.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Zero Trust Architecture.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Zero Trust Architecture.'
        },
        'interview_rubric': [
            'How does Zero Trust Architecture handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Zero Trust Architecture and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Zero Trust Architecture?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': False
    },
    {
        'id': 'devops_cloud_040',
        'canonical_name': 'VPC Networking',
        'category': 'Cloud, DevOps & Infrastructure',
        'aliases': ['vpc networking', 'vpc-networking', 'vpcnetworking'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of VPC Networking syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with VPC Networking.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using VPC Networking.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing VPC Networking.'
        },
        'interview_rubric': [
            'How does VPC Networking handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in VPC Networking and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling VPC Networking?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': False
    },
]


def get_devops_cloud_skill_map() -> dict:
    return {item['canonical_name']: item for item in TAXONOMY_RECORDS}

def get_devops_cloud_aliases_lookup() -> dict:
    lookup = {}
    for item in TAXONOMY_RECORDS:
        for alias in item['aliases']:
            lookup[alias.lower()] = item['canonical_name']
    return lookup
