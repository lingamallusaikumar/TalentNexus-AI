"""
TalentNexus AI - Big Data & Analytics Engineering Comprehensive Domain Taxonomy
Defines skills, seniority criteria, interview evaluation rubrics, and relational weights.
"""

DOMAIN_NAME = 'Big Data & Analytics Engineering'
DOMAIN_KEY = 'data_engineering'

TAXONOMY_RECORDS = [
    {
        'id': 'data_engineering_001',
        'canonical_name': 'Data Warehousing',
        'category': 'Big Data & Analytics Engineering',
        'aliases': ['data warehousing', 'data-warehousing', 'datawarehousing'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Data Warehousing syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Data Warehousing.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Data Warehousing.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Data Warehousing.'
        },
        'interview_rubric': [
            'How does Data Warehousing handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Data Warehousing and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Data Warehousing?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': True
    },
    {
        'id': 'data_engineering_002',
        'canonical_name': 'Snowflake',
        'category': 'Big Data & Analytics Engineering',
        'aliases': ['snowflake', 'snowflake', 'snowflake'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Snowflake syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Snowflake.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Snowflake.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Snowflake.'
        },
        'interview_rubric': [
            'How does Snowflake handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Snowflake and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Snowflake?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': True
    },
    {
        'id': 'data_engineering_003',
        'canonical_name': 'Google BigQuery',
        'category': 'Big Data & Analytics Engineering',
        'aliases': ['google bigquery', 'google-bigquery', 'googlebigquery'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Google BigQuery syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Google BigQuery.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Google BigQuery.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Google BigQuery.'
        },
        'interview_rubric': [
            'How does Google BigQuery handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Google BigQuery and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Google BigQuery?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': True
    },
    {
        'id': 'data_engineering_004',
        'canonical_name': 'Amazon Redshift',
        'category': 'Big Data & Analytics Engineering',
        'aliases': ['amazon redshift', 'amazon-redshift', 'amazonredshift'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Amazon Redshift syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Amazon Redshift.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Amazon Redshift.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Amazon Redshift.'
        },
        'interview_rubric': [
            'How does Amazon Redshift handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Amazon Redshift and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Amazon Redshift?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': True
    },
    {
        'id': 'data_engineering_005',
        'canonical_name': 'Databricks',
        'category': 'Big Data & Analytics Engineering',
        'aliases': ['databricks', 'databricks', 'databricks'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Databricks syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Databricks.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Databricks.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Databricks.'
        },
        'interview_rubric': [
            'How does Databricks handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Databricks and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Databricks?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': True
    },
    {
        'id': 'data_engineering_006',
        'canonical_name': 'Apache Hadoop',
        'category': 'Big Data & Analytics Engineering',
        'aliases': ['apache hadoop', 'apache-hadoop', 'apachehadoop'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Apache Hadoop syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Apache Hadoop.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Apache Hadoop.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Apache Hadoop.'
        },
        'interview_rubric': [
            'How does Apache Hadoop handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Apache Hadoop and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Apache Hadoop?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': True
    },
    {
        'id': 'data_engineering_007',
        'canonical_name': 'Hive',
        'category': 'Big Data & Analytics Engineering',
        'aliases': ['hive', 'hive', 'hive'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Hive syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Hive.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Hive.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Hive.'
        },
        'interview_rubric': [
            'How does Hive handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Hive and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Hive?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': True
    },
    {
        'id': 'data_engineering_008',
        'canonical_name': 'Apache Kafka',
        'category': 'Big Data & Analytics Engineering',
        'aliases': ['apache kafka', 'apache-kafka', 'apachekafka'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Apache Kafka syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Apache Kafka.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Apache Kafka.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Apache Kafka.'
        },
        'interview_rubric': [
            'How does Apache Kafka handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Apache Kafka and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Apache Kafka?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': True
    },
    {
        'id': 'data_engineering_009',
        'canonical_name': 'Apache Spark Streaming',
        'category': 'Big Data & Analytics Engineering',
        'aliases': ['apache spark streaming', 'apache-spark-streaming', 'apachesparkstreaming'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Apache Spark Streaming syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Apache Spark Streaming.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Apache Spark Streaming.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Apache Spark Streaming.'
        },
        'interview_rubric': [
            'How does Apache Spark Streaming handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Apache Spark Streaming and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Apache Spark Streaming?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': True
    },
    {
        'id': 'data_engineering_010',
        'canonical_name': 'Apache Beam',
        'category': 'Big Data & Analytics Engineering',
        'aliases': ['apache beam', 'apache-beam', 'apachebeam'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Apache Beam syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Apache Beam.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Apache Beam.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Apache Beam.'
        },
        'interview_rubric': [
            'How does Apache Beam handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Apache Beam and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Apache Beam?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': True
    },
    {
        'id': 'data_engineering_011',
        'canonical_name': 'Airflow',
        'category': 'Big Data & Analytics Engineering',
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
        'market_importance_weight': 1.2,
        'is_critical_skill': False
    },
    {
        'id': 'data_engineering_012',
        'canonical_name': 'Luigi',
        'category': 'Big Data & Analytics Engineering',
        'aliases': ['luigi', 'luigi', 'luigi'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Luigi syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Luigi.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Luigi.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Luigi.'
        },
        'interview_rubric': [
            'How does Luigi handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Luigi and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Luigi?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': False
    },
    {
        'id': 'data_engineering_013',
        'canonical_name': 'Prefect',
        'category': 'Big Data & Analytics Engineering',
        'aliases': ['prefect', 'prefect', 'prefect'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Prefect syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Prefect.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Prefect.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Prefect.'
        },
        'interview_rubric': [
            'How does Prefect handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Prefect and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Prefect?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': False
    },
    {
        'id': 'data_engineering_014',
        'canonical_name': 'Dagster',
        'category': 'Big Data & Analytics Engineering',
        'aliases': ['dagster', 'dagster', 'dagster'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Dagster syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Dagster.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Dagster.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Dagster.'
        },
        'interview_rubric': [
            'How does Dagster handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Dagster and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Dagster?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': False
    },
    {
        'id': 'data_engineering_015',
        'canonical_name': 'dbt (data build tool)',
        'category': 'Big Data & Analytics Engineering',
        'aliases': ['dbt (data build tool)', 'dbt-(data-build-tool)', 'dbt(databuildtool)'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of dbt (data build tool) syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with dbt (data build tool).',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using dbt (data build tool).',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing dbt (data build tool).'
        },
        'interview_rubric': [
            'How does dbt (data build tool) handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in dbt (data build tool) and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling dbt (data build tool)?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': False
    },
    {
        'id': 'data_engineering_016',
        'canonical_name': 'ETL/ELT Architecture',
        'category': 'Big Data & Analytics Engineering',
        'aliases': ['etl/elt architecture', 'etl/elt-architecture', 'etl/eltarchitecture'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of ETL/ELT Architecture syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with ETL/ELT Architecture.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using ETL/ELT Architecture.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing ETL/ELT Architecture.'
        },
        'interview_rubric': [
            'How does ETL/ELT Architecture handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in ETL/ELT Architecture and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling ETL/ELT Architecture?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': False
    },
    {
        'id': 'data_engineering_017',
        'canonical_name': 'Data Modeling',
        'category': 'Big Data & Analytics Engineering',
        'aliases': ['data modeling', 'data-modeling', 'datamodeling'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Data Modeling syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Data Modeling.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Data Modeling.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Data Modeling.'
        },
        'interview_rubric': [
            'How does Data Modeling handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Data Modeling and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Data Modeling?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': False
    },
    {
        'id': 'data_engineering_018',
        'canonical_name': 'Star Schema',
        'category': 'Big Data & Analytics Engineering',
        'aliases': ['star schema', 'star-schema', 'starschema'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Star Schema syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Star Schema.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Star Schema.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Star Schema.'
        },
        'interview_rubric': [
            'How does Star Schema handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Star Schema and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Star Schema?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': False
    },
    {
        'id': 'data_engineering_019',
        'canonical_name': 'Snowflake Schema',
        'category': 'Big Data & Analytics Engineering',
        'aliases': ['snowflake schema', 'snowflake-schema', 'snowflakeschema'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Snowflake Schema syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Snowflake Schema.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Snowflake Schema.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Snowflake Schema.'
        },
        'interview_rubric': [
            'How does Snowflake Schema handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Snowflake Schema and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Snowflake Schema?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': False
    },
    {
        'id': 'data_engineering_020',
        'canonical_name': 'Data Governance',
        'category': 'Big Data & Analytics Engineering',
        'aliases': ['data governance', 'data-governance', 'datagovernance'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Data Governance syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Data Governance.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Data Governance.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Data Governance.'
        },
        'interview_rubric': [
            'How does Data Governance handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Data Governance and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Data Governance?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': False
    },
    {
        'id': 'data_engineering_021',
        'canonical_name': 'Data Cataloging',
        'category': 'Big Data & Analytics Engineering',
        'aliases': ['data cataloging', 'data-cataloging', 'datacataloging'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Data Cataloging syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Data Cataloging.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Data Cataloging.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Data Cataloging.'
        },
        'interview_rubric': [
            'How does Data Cataloging handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Data Cataloging and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Data Cataloging?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': False
    },
    {
        'id': 'data_engineering_022',
        'canonical_name': 'Delta Lake',
        'category': 'Big Data & Analytics Engineering',
        'aliases': ['delta lake', 'delta-lake', 'deltalake'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Delta Lake syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Delta Lake.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Delta Lake.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Delta Lake.'
        },
        'interview_rubric': [
            'How does Delta Lake handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Delta Lake and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Delta Lake?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': False
    },
    {
        'id': 'data_engineering_023',
        'canonical_name': 'Apache Iceberg',
        'category': 'Big Data & Analytics Engineering',
        'aliases': ['apache iceberg', 'apache-iceberg', 'apacheiceberg'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Apache Iceberg syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Apache Iceberg.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Apache Iceberg.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Apache Iceberg.'
        },
        'interview_rubric': [
            'How does Apache Iceberg handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Apache Iceberg and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Apache Iceberg?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': False
    },
    {
        'id': 'data_engineering_024',
        'canonical_name': 'Apache Hudi',
        'category': 'Big Data & Analytics Engineering',
        'aliases': ['apache hudi', 'apache-hudi', 'apachehudi'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Apache Hudi syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Apache Hudi.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Apache Hudi.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Apache Hudi.'
        },
        'interview_rubric': [
            'How does Apache Hudi handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Apache Hudi and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Apache Hudi?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': False
    },
    {
        'id': 'data_engineering_025',
        'canonical_name': 'Presto/Trino',
        'category': 'Big Data & Analytics Engineering',
        'aliases': ['presto/trino', 'presto/trino', 'presto/trino'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Presto/Trino syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Presto/Trino.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Presto/Trino.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Presto/Trino.'
        },
        'interview_rubric': [
            'How does Presto/Trino handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Presto/Trino and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Presto/Trino?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': False
    },
    {
        'id': 'data_engineering_026',
        'canonical_name': 'ClickHouse',
        'category': 'Big Data & Analytics Engineering',
        'aliases': ['clickhouse', 'clickhouse', 'clickhouse'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of ClickHouse syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with ClickHouse.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using ClickHouse.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing ClickHouse.'
        },
        'interview_rubric': [
            'How does ClickHouse handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in ClickHouse and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling ClickHouse?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': False
    },
    {
        'id': 'data_engineering_027',
        'canonical_name': 'PostGIS',
        'category': 'Big Data & Analytics Engineering',
        'aliases': ['postgis', 'postgis', 'postgis'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of PostGIS syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with PostGIS.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using PostGIS.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing PostGIS.'
        },
        'interview_rubric': [
            'How does PostGIS handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in PostGIS and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling PostGIS?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': False
    },
    {
        'id': 'data_engineering_028',
        'canonical_name': 'Data Quality Testing',
        'category': 'Big Data & Analytics Engineering',
        'aliases': ['data quality testing', 'data-quality-testing', 'dataqualitytesting'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Data Quality Testing syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Data Quality Testing.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Data Quality Testing.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Data Quality Testing.'
        },
        'interview_rubric': [
            'How does Data Quality Testing handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Data Quality Testing and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Data Quality Testing?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': False
    },
    {
        'id': 'data_engineering_029',
        'canonical_name': 'Great Expectations',
        'category': 'Big Data & Analytics Engineering',
        'aliases': ['great expectations', 'great-expectations', 'greatexpectations'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Great Expectations syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Great Expectations.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Great Expectations.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Great Expectations.'
        },
        'interview_rubric': [
            'How does Great Expectations handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Great Expectations and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Great Expectations?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': False
    },
    {
        'id': 'data_engineering_030',
        'canonical_name': 'Parquet/ORC Storage',
        'category': 'Big Data & Analytics Engineering',
        'aliases': ['parquet/orc storage', 'parquet/orc-storage', 'parquet/orcstorage'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Parquet/ORC Storage syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Parquet/ORC Storage.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Parquet/ORC Storage.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Parquet/ORC Storage.'
        },
        'interview_rubric': [
            'How does Parquet/ORC Storage handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Parquet/ORC Storage and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Parquet/ORC Storage?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': False
    },
]


def get_data_engineering_skill_map() -> dict:
    return {item['canonical_name']: item for item in TAXONOMY_RECORDS}

def get_data_engineering_aliases_lookup() -> dict:
    lookup = {}
    for item in TAXONOMY_RECORDS:
        for alias in item['aliases']:
            lookup[alias.lower()] = item['canonical_name']
    return lookup
