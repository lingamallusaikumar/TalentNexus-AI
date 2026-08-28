"""
TalentNexus AI - Backend Engineering Comprehensive Domain Taxonomy
Defines skills, seniority criteria, interview evaluation rubrics, and relational weights.
"""

DOMAIN_NAME = 'Backend Engineering'
DOMAIN_KEY = 'backend'

TAXONOMY_RECORDS = [
    {
        'id': 'backend_001',
        'canonical_name': 'Python',
        'category': 'Backend Engineering',
        'aliases': ['python', 'python', 'python'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Python syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Python.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Python.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Python.'
        },
        'interview_rubric': [
            'How does Python handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Python and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Python?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': True
    },
    {
        'id': 'backend_002',
        'canonical_name': 'Flask',
        'category': 'Backend Engineering',
        'aliases': ['flask', 'flask', 'flask'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Flask syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Flask.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Flask.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Flask.'
        },
        'interview_rubric': [
            'How does Flask handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Flask and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Flask?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': True
    },
    {
        'id': 'backend_003',
        'canonical_name': 'Django',
        'category': 'Backend Engineering',
        'aliases': ['django', 'django', 'django'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Django syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Django.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Django.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Django.'
        },
        'interview_rubric': [
            'How does Django handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Django and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Django?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': True
    },
    {
        'id': 'backend_004',
        'canonical_name': 'FastAPI',
        'category': 'Backend Engineering',
        'aliases': ['fastapi', 'fastapi', 'fastapi'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of FastAPI syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with FastAPI.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using FastAPI.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing FastAPI.'
        },
        'interview_rubric': [
            'How does FastAPI handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in FastAPI and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling FastAPI?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': True
    },
    {
        'id': 'backend_005',
        'canonical_name': 'Java',
        'category': 'Backend Engineering',
        'aliases': ['java', 'java', 'java'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Java syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Java.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Java.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Java.'
        },
        'interview_rubric': [
            'How does Java handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Java and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Java?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': True
    },
    {
        'id': 'backend_006',
        'canonical_name': 'Spring Boot',
        'category': 'Backend Engineering',
        'aliases': ['spring boot', 'spring-boot', 'springboot'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Spring Boot syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Spring Boot.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Spring Boot.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Spring Boot.'
        },
        'interview_rubric': [
            'How does Spring Boot handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Spring Boot and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Spring Boot?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': True
    },
    {
        'id': 'backend_007',
        'canonical_name': 'Node.js',
        'category': 'Backend Engineering',
        'aliases': ['node.js', 'node.js', 'node.js', 'Nodejs'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Node.js syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Node.js.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Node.js.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Node.js.'
        },
        'interview_rubric': [
            'How does Node.js handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Node.js and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Node.js?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': True
    },
    {
        'id': 'backend_008',
        'canonical_name': 'Express',
        'category': 'Backend Engineering',
        'aliases': ['express', 'express', 'express'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Express syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Express.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Express.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Express.'
        },
        'interview_rubric': [
            'How does Express handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Express and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Express?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': True
    },
    {
        'id': 'backend_009',
        'canonical_name': 'Go',
        'category': 'Backend Engineering',
        'aliases': ['go', 'go', 'go'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Go syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Go.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Go.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Go.'
        },
        'interview_rubric': [
            'How does Go handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Go and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Go?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': True
    },
    {
        'id': 'backend_010',
        'canonical_name': 'Rust',
        'category': 'Backend Engineering',
        'aliases': ['rust', 'rust', 'rust'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Rust syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Rust.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Rust.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Rust.'
        },
        'interview_rubric': [
            'How does Rust handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Rust and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Rust?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': True
    },
    {
        'id': 'backend_011',
        'canonical_name': 'C#',
        'category': 'Backend Engineering',
        'aliases': ['c#', 'c#', 'c#'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of C# syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with C#.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using C#.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing C#.'
        },
        'interview_rubric': [
            'How does C# handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in C# and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling C#?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': False
    },
    {
        'id': 'backend_012',
        'canonical_name': '.NET Core',
        'category': 'Backend Engineering',
        'aliases': ['.net core', '.net-core', '.netcore', 'NET Core'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of .NET Core syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with .NET Core.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using .NET Core.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing .NET Core.'
        },
        'interview_rubric': [
            'How does .NET Core handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in .NET Core and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling .NET Core?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': False
    },
    {
        'id': 'backend_013',
        'canonical_name': 'Ruby on Rails',
        'category': 'Backend Engineering',
        'aliases': ['ruby on rails', 'ruby-on-rails', 'rubyonrails'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Ruby on Rails syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Ruby on Rails.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Ruby on Rails.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Ruby on Rails.'
        },
        'interview_rubric': [
            'How does Ruby on Rails handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Ruby on Rails and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Ruby on Rails?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': False
    },
    {
        'id': 'backend_014',
        'canonical_name': 'PHP',
        'category': 'Backend Engineering',
        'aliases': ['php', 'php', 'php'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of PHP syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with PHP.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using PHP.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing PHP.'
        },
        'interview_rubric': [
            'How does PHP handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in PHP and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling PHP?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': False
    },
    {
        'id': 'backend_015',
        'canonical_name': 'Laravel',
        'category': 'Backend Engineering',
        'aliases': ['laravel', 'laravel', 'laravel'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Laravel syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Laravel.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Laravel.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Laravel.'
        },
        'interview_rubric': [
            'How does Laravel handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Laravel and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Laravel?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': False
    },
    {
        'id': 'backend_016',
        'canonical_name': 'GraphQL',
        'category': 'Backend Engineering',
        'aliases': ['graphql', 'graphql', 'graphql'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of GraphQL syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with GraphQL.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using GraphQL.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing GraphQL.'
        },
        'interview_rubric': [
            'How does GraphQL handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in GraphQL and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling GraphQL?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': False
    },
    {
        'id': 'backend_017',
        'canonical_name': 'gRPC',
        'category': 'Backend Engineering',
        'aliases': ['grpc', 'grpc', 'grpc'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of gRPC syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with gRPC.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using gRPC.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing gRPC.'
        },
        'interview_rubric': [
            'How does gRPC handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in gRPC and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling gRPC?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': False
    },
    {
        'id': 'backend_018',
        'canonical_name': 'REST APIs',
        'category': 'Backend Engineering',
        'aliases': ['rest apis', 'rest-apis', 'restapis'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of REST APIs syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with REST APIs.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using REST APIs.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing REST APIs.'
        },
        'interview_rubric': [
            'How does REST APIs handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in REST APIs and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling REST APIs?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': False
    },
    {
        'id': 'backend_019',
        'canonical_name': 'Microservices',
        'category': 'Backend Engineering',
        'aliases': ['microservices', 'microservices', 'microservices'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Microservices syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Microservices.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Microservices.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Microservices.'
        },
        'interview_rubric': [
            'How does Microservices handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Microservices and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Microservices?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': False
    },
    {
        'id': 'backend_020',
        'canonical_name': 'Kafka',
        'category': 'Backend Engineering',
        'aliases': ['kafka', 'kafka', 'kafka'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Kafka syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Kafka.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Kafka.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Kafka.'
        },
        'interview_rubric': [
            'How does Kafka handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Kafka and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Kafka?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': False
    },
    {
        'id': 'backend_021',
        'canonical_name': 'RabbitMQ',
        'category': 'Backend Engineering',
        'aliases': ['rabbitmq', 'rabbitmq', 'rabbitmq'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of RabbitMQ syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with RabbitMQ.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using RabbitMQ.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing RabbitMQ.'
        },
        'interview_rubric': [
            'How does RabbitMQ handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in RabbitMQ and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling RabbitMQ?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': False
    },
    {
        'id': 'backend_022',
        'canonical_name': 'Celery',
        'category': 'Backend Engineering',
        'aliases': ['celery', 'celery', 'celery'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Celery syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Celery.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Celery.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Celery.'
        },
        'interview_rubric': [
            'How does Celery handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Celery and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Celery?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': False
    },
    {
        'id': 'backend_023',
        'canonical_name': 'PostgreSQL',
        'category': 'Backend Engineering',
        'aliases': ['postgresql', 'postgresql', 'postgresql'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of PostgreSQL syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with PostgreSQL.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using PostgreSQL.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing PostgreSQL.'
        },
        'interview_rubric': [
            'How does PostgreSQL handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in PostgreSQL and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling PostgreSQL?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': False
    },
    {
        'id': 'backend_024',
        'canonical_name': 'MySQL',
        'category': 'Backend Engineering',
        'aliases': ['mysql', 'mysql', 'mysql'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of MySQL syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with MySQL.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using MySQL.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing MySQL.'
        },
        'interview_rubric': [
            'How does MySQL handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in MySQL and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling MySQL?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': False
    },
    {
        'id': 'backend_025',
        'canonical_name': 'MongoDB',
        'category': 'Backend Engineering',
        'aliases': ['mongodb', 'mongodb', 'mongodb'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of MongoDB syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with MongoDB.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using MongoDB.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing MongoDB.'
        },
        'interview_rubric': [
            'How does MongoDB handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in MongoDB and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling MongoDB?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': False
    },
    {
        'id': 'backend_026',
        'canonical_name': 'Redis',
        'category': 'Backend Engineering',
        'aliases': ['redis', 'redis', 'redis'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Redis syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Redis.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Redis.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Redis.'
        },
        'interview_rubric': [
            'How does Redis handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Redis and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Redis?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': False
    },
    {
        'id': 'backend_027',
        'canonical_name': 'Elasticsearch',
        'category': 'Backend Engineering',
        'aliases': ['elasticsearch', 'elasticsearch', 'elasticsearch'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Elasticsearch syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Elasticsearch.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Elasticsearch.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Elasticsearch.'
        },
        'interview_rubric': [
            'How does Elasticsearch handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Elasticsearch and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Elasticsearch?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': False
    },
    {
        'id': 'backend_028',
        'canonical_name': 'Cassandra',
        'category': 'Backend Engineering',
        'aliases': ['cassandra', 'cassandra', 'cassandra'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Cassandra syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Cassandra.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Cassandra.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Cassandra.'
        },
        'interview_rubric': [
            'How does Cassandra handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Cassandra and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Cassandra?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': False
    },
    {
        'id': 'backend_029',
        'canonical_name': 'DynamoDB',
        'category': 'Backend Engineering',
        'aliases': ['dynamodb', 'dynamodb', 'dynamodb'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of DynamoDB syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with DynamoDB.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using DynamoDB.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing DynamoDB.'
        },
        'interview_rubric': [
            'How does DynamoDB handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in DynamoDB and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling DynamoDB?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': False
    },
    {
        'id': 'backend_030',
        'canonical_name': 'Neo4j',
        'category': 'Backend Engineering',
        'aliases': ['neo4j', 'neo4j', 'neo4j'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Neo4j syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Neo4j.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Neo4j.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Neo4j.'
        },
        'interview_rubric': [
            'How does Neo4j handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Neo4j and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Neo4j?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': False
    },
    {
        'id': 'backend_031',
        'canonical_name': 'SQLAlchemy',
        'category': 'Backend Engineering',
        'aliases': ['sqlalchemy', 'sqlalchemy', 'sqlalchemy'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of SQLAlchemy syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with SQLAlchemy.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using SQLAlchemy.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing SQLAlchemy.'
        },
        'interview_rubric': [
            'How does SQLAlchemy handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in SQLAlchemy and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling SQLAlchemy?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': False
    },
    {
        'id': 'backend_032',
        'canonical_name': 'Hibernate',
        'category': 'Backend Engineering',
        'aliases': ['hibernate', 'hibernate', 'hibernate'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Hibernate syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Hibernate.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Hibernate.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Hibernate.'
        },
        'interview_rubric': [
            'How does Hibernate handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Hibernate and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Hibernate?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': False
    },
    {
        'id': 'backend_033',
        'canonical_name': 'Prisma',
        'category': 'Backend Engineering',
        'aliases': ['prisma', 'prisma', 'prisma'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Prisma syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Prisma.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Prisma.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Prisma.'
        },
        'interview_rubric': [
            'How does Prisma handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Prisma and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Prisma?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': False
    },
    {
        'id': 'backend_034',
        'canonical_name': 'Socket.io',
        'category': 'Backend Engineering',
        'aliases': ['socket.io', 'socket.io', 'socket.io', 'Socketio'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Socket.io syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Socket.io.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Socket.io.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Socket.io.'
        },
        'interview_rubric': [
            'How does Socket.io handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Socket.io and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Socket.io?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': False
    },
    {
        'id': 'backend_035',
        'canonical_name': 'WebSockets',
        'category': 'Backend Engineering',
        'aliases': ['websockets', 'websockets', 'websockets'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of WebSockets syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with WebSockets.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using WebSockets.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing WebSockets.'
        },
        'interview_rubric': [
            'How does WebSockets handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in WebSockets and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling WebSockets?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': False
    },
    {
        'id': 'backend_036',
        'canonical_name': 'OAuth2',
        'category': 'Backend Engineering',
        'aliases': ['oauth2', 'oauth2', 'oauth2'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of OAuth2 syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with OAuth2.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using OAuth2.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing OAuth2.'
        },
        'interview_rubric': [
            'How does OAuth2 handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in OAuth2 and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling OAuth2?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': False
    },
    {
        'id': 'backend_037',
        'canonical_name': 'JWT',
        'category': 'Backend Engineering',
        'aliases': ['jwt', 'jwt', 'jwt'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of JWT syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with JWT.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using JWT.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing JWT.'
        },
        'interview_rubric': [
            'How does JWT handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in JWT and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling JWT?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': False
    },
    {
        'id': 'backend_038',
        'canonical_name': 'SAML',
        'category': 'Backend Engineering',
        'aliases': ['saml', 'saml', 'saml'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of SAML syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with SAML.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using SAML.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing SAML.'
        },
        'interview_rubric': [
            'How does SAML handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in SAML and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling SAML?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': False
    },
    {
        'id': 'backend_039',
        'canonical_name': 'OpenID Connect',
        'category': 'Backend Engineering',
        'aliases': ['openid connect', 'openid-connect', 'openidconnect'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of OpenID Connect syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with OpenID Connect.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using OpenID Connect.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing OpenID Connect.'
        },
        'interview_rubric': [
            'How does OpenID Connect handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in OpenID Connect and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling OpenID Connect?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': False
    },
    {
        'id': 'backend_040',
        'canonical_name': 'Swagger/OpenAPI',
        'category': 'Backend Engineering',
        'aliases': ['swagger/openapi', 'swagger/openapi', 'swagger/openapi'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Swagger/OpenAPI syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Swagger/OpenAPI.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Swagger/OpenAPI.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Swagger/OpenAPI.'
        },
        'interview_rubric': [
            'How does Swagger/OpenAPI handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Swagger/OpenAPI and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Swagger/OpenAPI?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': False
    },
    {
        'id': 'backend_041',
        'canonical_name': 'Distributed Systems',
        'category': 'Backend Engineering',
        'aliases': ['distributed systems', 'distributed-systems', 'distributedsystems'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Distributed Systems syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Distributed Systems.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Distributed Systems.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Distributed Systems.'
        },
        'interview_rubric': [
            'How does Distributed Systems handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Distributed Systems and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Distributed Systems?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': False
    },
]


def get_backend_skill_map() -> dict:
    return {item['canonical_name']: item for item in TAXONOMY_RECORDS}

def get_backend_aliases_lookup() -> dict:
    lookup = {}
    for item in TAXONOMY_RECORDS:
        for alias in item['aliases']:
            lookup[alias.lower()] = item['canonical_name']
    return lookup
