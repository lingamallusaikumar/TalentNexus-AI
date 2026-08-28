"""
TalentNexus AI - Quality Assurance & Test Automation Comprehensive Domain Taxonomy
Defines skills, seniority criteria, interview evaluation rubrics, and relational weights.
"""

DOMAIN_NAME = 'Quality Assurance & Test Automation'
DOMAIN_KEY = 'qa_testing'

TAXONOMY_RECORDS = [
    {
        'id': 'qa_testing_001',
        'canonical_name': 'Quality Assurance (QA)',
        'category': 'Quality Assurance & Test Automation',
        'aliases': ['quality assurance (qa)', 'quality-assurance-(qa)', 'qualityassurance(qa)'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Quality Assurance (QA) syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Quality Assurance (QA).',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Quality Assurance (QA).',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Quality Assurance (QA).'
        },
        'interview_rubric': [
            'How does Quality Assurance (QA) handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Quality Assurance (QA) and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Quality Assurance (QA)?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': True
    },
    {
        'id': 'qa_testing_002',
        'canonical_name': 'Test Automation',
        'category': 'Quality Assurance & Test Automation',
        'aliases': ['test automation', 'test-automation', 'testautomation'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Test Automation syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Test Automation.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Test Automation.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Test Automation.'
        },
        'interview_rubric': [
            'How does Test Automation handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Test Automation and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Test Automation?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': True
    },
    {
        'id': 'qa_testing_003',
        'canonical_name': 'Manual Testing',
        'category': 'Quality Assurance & Test Automation',
        'aliases': ['manual testing', 'manual-testing', 'manualtesting'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Manual Testing syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Manual Testing.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Manual Testing.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Manual Testing.'
        },
        'interview_rubric': [
            'How does Manual Testing handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Manual Testing and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Manual Testing?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': True
    },
    {
        'id': 'qa_testing_004',
        'canonical_name': 'Unit Testing',
        'category': 'Quality Assurance & Test Automation',
        'aliases': ['unit testing', 'unit-testing', 'unittesting'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Unit Testing syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Unit Testing.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Unit Testing.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Unit Testing.'
        },
        'interview_rubric': [
            'How does Unit Testing handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Unit Testing and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Unit Testing?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': True
    },
    {
        'id': 'qa_testing_005',
        'canonical_name': 'Integration Testing',
        'category': 'Quality Assurance & Test Automation',
        'aliases': ['integration testing', 'integration-testing', 'integrationtesting'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Integration Testing syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Integration Testing.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Integration Testing.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Integration Testing.'
        },
        'interview_rubric': [
            'How does Integration Testing handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Integration Testing and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Integration Testing?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': True
    },
    {
        'id': 'qa_testing_006',
        'canonical_name': 'End-to-End (E2E) Testing',
        'category': 'Quality Assurance & Test Automation',
        'aliases': ['end-to-end (e2e) testing', 'end-to-end-(e2e)-testing', 'end-to-end(e2e)testing'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of End-to-End (E2E) Testing syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with End-to-End (E2E) Testing.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using End-to-End (E2E) Testing.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing End-to-End (E2E) Testing.'
        },
        'interview_rubric': [
            'How does End-to-End (E2E) Testing handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in End-to-End (E2E) Testing and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling End-to-End (E2E) Testing?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': True
    },
    {
        'id': 'qa_testing_007',
        'canonical_name': 'Performance Testing',
        'category': 'Quality Assurance & Test Automation',
        'aliases': ['performance testing', 'performance-testing', 'performancetesting'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Performance Testing syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Performance Testing.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Performance Testing.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Performance Testing.'
        },
        'interview_rubric': [
            'How does Performance Testing handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Performance Testing and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Performance Testing?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': True
    },
    {
        'id': 'qa_testing_008',
        'canonical_name': 'Load Testing',
        'category': 'Quality Assurance & Test Automation',
        'aliases': ['load testing', 'load-testing', 'loadtesting'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Load Testing syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Load Testing.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Load Testing.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Load Testing.'
        },
        'interview_rubric': [
            'How does Load Testing handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Load Testing and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Load Testing?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': True
    },
    {
        'id': 'qa_testing_009',
        'canonical_name': 'Stress Testing',
        'category': 'Quality Assurance & Test Automation',
        'aliases': ['stress testing', 'stress-testing', 'stresstesting'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Stress Testing syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Stress Testing.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Stress Testing.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Stress Testing.'
        },
        'interview_rubric': [
            'How does Stress Testing handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Stress Testing and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Stress Testing?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': True
    },
    {
        'id': 'qa_testing_010',
        'canonical_name': 'Selenium WebDriver',
        'category': 'Quality Assurance & Test Automation',
        'aliases': ['selenium webdriver', 'selenium-webdriver', 'seleniumwebdriver'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Selenium WebDriver syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Selenium WebDriver.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Selenium WebDriver.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Selenium WebDriver.'
        },
        'interview_rubric': [
            'How does Selenium WebDriver handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Selenium WebDriver and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Selenium WebDriver?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': True
    },
    {
        'id': 'qa_testing_011',
        'canonical_name': 'Cypress',
        'category': 'Quality Assurance & Test Automation',
        'aliases': ['cypress', 'cypress', 'cypress'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Cypress syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Cypress.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Cypress.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Cypress.'
        },
        'interview_rubric': [
            'How does Cypress handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Cypress and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Cypress?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': False
    },
    {
        'id': 'qa_testing_012',
        'canonical_name': 'Playwright',
        'category': 'Quality Assurance & Test Automation',
        'aliases': ['playwright', 'playwright', 'playwright'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Playwright syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Playwright.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Playwright.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Playwright.'
        },
        'interview_rubric': [
            'How does Playwright handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Playwright and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Playwright?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': False
    },
    {
        'id': 'qa_testing_013',
        'canonical_name': 'Appium',
        'category': 'Quality Assurance & Test Automation',
        'aliases': ['appium', 'appium', 'appium'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Appium syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Appium.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Appium.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Appium.'
        },
        'interview_rubric': [
            'How does Appium handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Appium and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Appium?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': False
    },
    {
        'id': 'qa_testing_014',
        'canonical_name': 'Postman / Newman',
        'category': 'Quality Assurance & Test Automation',
        'aliases': ['postman / newman', 'postman-/-newman', 'postman/newman'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Postman / Newman syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Postman / Newman.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Postman / Newman.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Postman / Newman.'
        },
        'interview_rubric': [
            'How does Postman / Newman handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Postman / Newman and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Postman / Newman?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': False
    },
    {
        'id': 'qa_testing_015',
        'canonical_name': 'RestAssured',
        'category': 'Quality Assurance & Test Automation',
        'aliases': ['restassured', 'restassured', 'restassured'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of RestAssured syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with RestAssured.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using RestAssured.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing RestAssured.'
        },
        'interview_rubric': [
            'How does RestAssured handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in RestAssured and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling RestAssured?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': False
    },
    {
        'id': 'qa_testing_016',
        'canonical_name': 'JMeter',
        'category': 'Quality Assurance & Test Automation',
        'aliases': ['jmeter', 'jmeter', 'jmeter'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of JMeter syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with JMeter.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using JMeter.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing JMeter.'
        },
        'interview_rubric': [
            'How does JMeter handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in JMeter and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling JMeter?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': False
    },
    {
        'id': 'qa_testing_017',
        'canonical_name': 'k6',
        'category': 'Quality Assurance & Test Automation',
        'aliases': ['k6', 'k6', 'k6'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of k6 syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with k6.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using k6.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing k6.'
        },
        'interview_rubric': [
            'How does k6 handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in k6 and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling k6?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': False
    },
    {
        'id': 'qa_testing_018',
        'canonical_name': 'Locust',
        'category': 'Quality Assurance & Test Automation',
        'aliases': ['locust', 'locust', 'locust'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Locust syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Locust.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Locust.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Locust.'
        },
        'interview_rubric': [
            'How does Locust handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Locust and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Locust?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': False
    },
    {
        'id': 'qa_testing_019',
        'canonical_name': 'Pytest',
        'category': 'Quality Assurance & Test Automation',
        'aliases': ['pytest', 'pytest', 'pytest'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Pytest syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Pytest.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Pytest.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Pytest.'
        },
        'interview_rubric': [
            'How does Pytest handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Pytest and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Pytest?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': False
    },
    {
        'id': 'qa_testing_020',
        'canonical_name': 'JUnit',
        'category': 'Quality Assurance & Test Automation',
        'aliases': ['junit', 'junit', 'junit'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of JUnit syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with JUnit.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using JUnit.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing JUnit.'
        },
        'interview_rubric': [
            'How does JUnit handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in JUnit and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling JUnit?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': False
    },
    {
        'id': 'qa_testing_021',
        'canonical_name': 'TestNG',
        'category': 'Quality Assurance & Test Automation',
        'aliases': ['testng', 'testng', 'testng'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of TestNG syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with TestNG.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using TestNG.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing TestNG.'
        },
        'interview_rubric': [
            'How does TestNG handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in TestNG and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling TestNG?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': False
    },
    {
        'id': 'qa_testing_022',
        'canonical_name': 'Mocha/Chai',
        'category': 'Quality Assurance & Test Automation',
        'aliases': ['mocha/chai', 'mocha/chai', 'mocha/chai'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Mocha/Chai syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Mocha/Chai.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Mocha/Chai.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Mocha/Chai.'
        },
        'interview_rubric': [
            'How does Mocha/Chai handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Mocha/Chai and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Mocha/Chai?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': False
    },
    {
        'id': 'qa_testing_023',
        'canonical_name': 'Cucumber (BDD)',
        'category': 'Quality Assurance & Test Automation',
        'aliases': ['cucumber (bdd)', 'cucumber-(bdd)', 'cucumber(bdd)'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Cucumber (BDD) syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Cucumber (BDD).',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Cucumber (BDD).',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Cucumber (BDD).'
        },
        'interview_rubric': [
            'How does Cucumber (BDD) handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Cucumber (BDD) and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Cucumber (BDD)?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': False
    },
    {
        'id': 'qa_testing_024',
        'canonical_name': 'SpecFlow',
        'category': 'Quality Assurance & Test Automation',
        'aliases': ['specflow', 'specflow', 'specflow'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of SpecFlow syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with SpecFlow.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using SpecFlow.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing SpecFlow.'
        },
        'interview_rubric': [
            'How does SpecFlow handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in SpecFlow and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling SpecFlow?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': False
    },
    {
        'id': 'qa_testing_025',
        'canonical_name': 'TestRail',
        'category': 'Quality Assurance & Test Automation',
        'aliases': ['testrail', 'testrail', 'testrail'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of TestRail syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with TestRail.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using TestRail.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing TestRail.'
        },
        'interview_rubric': [
            'How does TestRail handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in TestRail and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling TestRail?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': False
    },
    {
        'id': 'qa_testing_026',
        'canonical_name': 'Zephyr',
        'category': 'Quality Assurance & Test Automation',
        'aliases': ['zephyr', 'zephyr', 'zephyr'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Zephyr syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Zephyr.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Zephyr.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Zephyr.'
        },
        'interview_rubric': [
            'How does Zephyr handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Zephyr and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Zephyr?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': False
    },
    {
        'id': 'qa_testing_027',
        'canonical_name': 'Bug Tracking',
        'category': 'Quality Assurance & Test Automation',
        'aliases': ['bug tracking', 'bug-tracking', 'bugtracking'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Bug Tracking syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Bug Tracking.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Bug Tracking.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Bug Tracking.'
        },
        'interview_rubric': [
            'How does Bug Tracking handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Bug Tracking and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Bug Tracking?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': False
    },
    {
        'id': 'qa_testing_028',
        'canonical_name': 'Continuous Testing',
        'category': 'Quality Assurance & Test Automation',
        'aliases': ['continuous testing', 'continuous-testing', 'continuoustesting'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Continuous Testing syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Continuous Testing.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Continuous Testing.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Continuous Testing.'
        },
        'interview_rubric': [
            'How does Continuous Testing handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Continuous Testing and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Continuous Testing?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': False
    },
    {
        'id': 'qa_testing_029',
        'canonical_name': 'Smoke & Sanity Testing',
        'category': 'Quality Assurance & Test Automation',
        'aliases': ['smoke & sanity testing', 'smoke-&-sanity-testing', 'smoke&sanitytesting'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Smoke & Sanity Testing syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Smoke & Sanity Testing.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Smoke & Sanity Testing.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Smoke & Sanity Testing.'
        },
        'interview_rubric': [
            'How does Smoke & Sanity Testing handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Smoke & Sanity Testing and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Smoke & Sanity Testing?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': False
    },
    {
        'id': 'qa_testing_030',
        'canonical_name': 'Regression Testing',
        'category': 'Quality Assurance & Test Automation',
        'aliases': ['regression testing', 'regression-testing', 'regressiontesting'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Regression Testing syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Regression Testing.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Regression Testing.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Regression Testing.'
        },
        'interview_rubric': [
            'How does Regression Testing handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Regression Testing and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Regression Testing?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': False
    },
]


def get_qa_testing_skill_map() -> dict:
    return {item['canonical_name']: item for item in TAXONOMY_RECORDS}

def get_qa_testing_aliases_lookup() -> dict:
    lookup = {}
    for item in TAXONOMY_RECORDS:
        for alias in item['aliases']:
            lookup[alias.lower()] = item['canonical_name']
    return lookup
