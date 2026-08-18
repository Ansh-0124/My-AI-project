"""
Job Roles Configuration
=======================
Contains comprehensive job roles with required skills,
keywords, and descriptions for resume analysis.
"""

JOB_ROLES = {
    # Software Engineering
    "Software Developer": {
        "keywords": ["python", "java", "javascript", "c++", "c#", "git", "agile", "rest api",
                     "sql", "debugging", "testing", "oop", "design patterns", "software development"],
        "skills": ["Python", "Java", "JavaScript", "C++", "Git", "SQL", "REST APIs",
                   "Agile/Scrum", "Unit Testing", "OOP", "Data Structures"],
        "description": "Develops software applications using various programming languages and frameworks."
    },
    "Full Stack Developer": {
        "keywords": ["react", "angular", "vue", "node.js", "express", "mongodb", "postgresql",
                     "html", "css", "javascript", "typescript", "rest api", "graphql", "docker"],
        "skills": ["React/Angular/Vue", "Node.js", "Express", "MongoDB", "PostgreSQL",
                   "HTML/CSS", "JavaScript", "TypeScript", "REST APIs", "Docker", "Git"],
        "description": "Builds both frontend and backend of web applications."
    },
    "Frontend Developer": {
        "keywords": ["react", "angular", "vue", "html", "css", "javascript", "typescript",
                     "responsive design", "sass", "webpack", "figma", "ui/ux", "accessibility"],
        "skills": ["React", "Angular", "Vue.js", "HTML5", "CSS3", "JavaScript", "TypeScript",
                   "Responsive Design", "SASS/LESS", "Webpack", "Figma"],
        "description": "Specializes in building user interfaces and client-side applications."
    },
    "Backend Developer": {
        "keywords": ["python", "java", "node.js", "go", "rust", "sql", "nosql", "rest api",
                     "microservices", "docker", "kubernetes", "aws", "database", "caching", "redis"],
        "skills": ["Python/Java/Node.js", "SQL", "NoSQL", "REST APIs", "Microservices",
                   "Docker", "Kubernetes", "AWS/GCP/Azure", "Redis", "Message Queues"],
        "description": "Develops server-side logic, APIs, and database management systems."
    },

    # Data & AI
    "Data Scientist": {
        "keywords": ["python", "r", "machine learning", "deep learning", "statistics",
                     "pandas", "numpy", "scikit-learn", "tensorflow", "pytorch", "sql",
                     "data visualization", "jupyter", "nlp", "computer vision"],
        "skills": ["Python", "R", "Machine Learning", "Deep Learning", "Statistics",
                   "Pandas", "NumPy", "Scikit-learn", "TensorFlow/PyTorch", "SQL",
                   "Data Visualization", "NLP"],
        "description": "Analyzes complex data to extract insights and build predictive models."
    },
    "Data Analyst": {
        "keywords": ["sql", "python", "excel", "tableau", "power bi", "statistics",
                     "data visualization", "pandas", "reporting", "dashboards", "etl"],
        "skills": ["SQL", "Python", "Excel", "Tableau/Power BI", "Statistics",
                   "Data Visualization", "Pandas", "ETL", "Reporting"],
        "description": "Interprets data to help organizations make informed decisions."
    },
    "Data Engineer": {
        "keywords": ["python", "sql", "spark", "hadoop", "airflow", "etl", "data pipeline",
                     "aws", "gcp", "kafka", "snowflake", "databricks", "data warehouse"],
        "skills": ["Python", "SQL", "Apache Spark", "Hadoop", "Airflow", "ETL",
                   "AWS/GCP/Azure", "Kafka", "Snowflake", "Data Modeling"],
        "description": "Designs and builds data pipelines and infrastructure."
    },
    "Machine Learning Engineer": {
        "keywords": ["python", "tensorflow", "pytorch", "scikit-learn", "deep learning",
                     "mlops", "docker", "kubernetes", "model deployment", "feature engineering",
                     "neural networks", "computer vision", "nlp", "aws sagemaker"],
        "skills": ["Python", "TensorFlow/PyTorch", "Scikit-learn", "Deep Learning",
                   "MLOps", "Docker", "Model Deployment", "Feature Engineering", "AWS/GCP"],
        "description": "Builds, deploys, and maintains machine learning models in production."
    },
    "AI Engineer": {
        "keywords": ["python", "deep learning", "tensorflow", "pytorch", "nlp",
                     "computer vision", "generative ai", "llm", "transformers",
                     "reinforcement learning", "gpt", "langchain", "vector databases"],
        "skills": ["Python", "Deep Learning", "NLP", "Computer Vision", "LLMs",
                   "TensorFlow/PyTorch", "Transformers", "LangChain", "Vector Databases"],
        "description": "Develops AI-powered applications and systems."
    },

    # Mobile Development
    "Android Developer": {
        "keywords": ["kotlin", "java", "android studio", "jetpack compose", "xml",
                     "firebase", "rest api", "mvvm", "room database", "material design"],
        "skills": ["Kotlin", "Java", "Android Studio", "Jetpack Compose", "Firebase",
                   "REST APIs", "MVVM", "Room Database", "Material Design"],
        "description": "Builds native Android applications."
    },
    "iOS Developer": {
        "keywords": ["swift", "objective-c", "xcode", "swiftui", "uikit", "cocoapods",
                     "core data", "firebase", "rest api", "mvvm", "combine"],
        "skills": ["Swift", "SwiftUI", "UIKit", "Xcode", "Core Data", "Firebase",
                   "REST APIs", "MVVM", "Combine"],
        "description": "Builds native iOS applications for iPhone and iPad."
    },

    # DevOps & Cloud
    "DevOps Engineer": {
        "keywords": ["docker", "kubernetes", "jenkins", "terraform", "ansible", "aws",
                     "gcp", "azure", "ci/cd", "linux", "git", "monitoring", "prometheus",
                     "grafana", "infrastructure as code"],
        "skills": ["Docker", "Kubernetes", "Jenkins", "Terraform", "AWS/GCP/Azure",
                   "CI/CD", "Linux", "Git", "Prometheus/Grafana", "Ansible"],
        "description": "Manages infrastructure, CI/CD pipelines, and deployment automation."
    },
    "Cloud Engineer": {
        "keywords": ["aws", "gcp", "azure", "terraform", "cloudformation", "docker",
                     "kubernetes", "serverless", "lambda", "vpc", "iam", "networking"],
        "skills": ["AWS/GCP/Azure", "Terraform", "Docker", "Kubernetes", "Serverless",
                   "IAM", "Networking", "CloudFormation", "Lambda"],
        "description": "Designs and manages cloud infrastructure and services."
    },

    # Security
    "Cyber Security Analyst": {
        "keywords": ["security", "penetration testing", "vulnerability", "siem", "firewall",
                     "incident response", "encryption", "compliance", "risk assessment",
                     "network security", "owasp", "soc"],
        "skills": ["Penetration Testing", "SIEM", "Firewall Management", "Incident Response",
                   "Encryption", "Risk Assessment", "Network Security", "OWASP", "Compliance"],
        "description": "Protects organizations from cyber threats and security breaches."
    },

    # Design
    "UI/UX Designer": {
        "keywords": ["figma", "sketch", "adobe xd", "user research", "wireframing",
                     "prototyping", "usability testing", "design thinking", "html", "css",
                     "user interface", "user experience", "information architecture"],
        "skills": ["Figma", "Sketch", "Adobe XD", "User Research", "Wireframing",
                   "Prototyping", "Usability Testing", "Design Thinking", "HTML/CSS"],
        "description": "Designs intuitive and visually appealing user interfaces."
    },

    # Management
    "Project Manager": {
        "keywords": ["project management", "agile", "scrum", "jira", "stakeholder",
                     "risk management", "budget", "timeline", "pmp", "waterfall",
                     "leadership", "communication", "planning"],
        "skills": ["Project Management", "Agile/Scrum", "Jira", "Stakeholder Management",
                   "Risk Management", "Budget Planning", "PMP", "Leadership"],
        "description": "Plans, executes, and oversees projects from inception to completion."
    },
    "Product Manager": {
        "keywords": ["product strategy", "roadmap", "user stories", "agile", "analytics",
                     "market research", "a/b testing", "stakeholder", "prioritization",
                     "product lifecycle", "kpis", "okrs"],
        "skills": ["Product Strategy", "Roadmap Planning", "User Stories", "Agile",
                   "Analytics", "Market Research", "A/B Testing", "Stakeholder Management"],
        "description": "Defines product vision and strategy to deliver customer value."
    },

    # Marketing & Business
    "Digital Marketer": {
        "keywords": ["seo", "sem", "google analytics", "social media", "content marketing",
                     "email marketing", "ppc", "facebook ads", "google ads", "conversion",
                     "marketing automation", "hubspot"],
        "skills": ["SEO/SEM", "Google Analytics", "Social Media Marketing", "Content Marketing",
                   "PPC/Google Ads", "Email Marketing", "Marketing Automation", "HubSpot"],
        "description": "Promotes products and brands through digital channels."
    },
    "Business Analyst": {
        "keywords": ["requirements gathering", "sql", "excel", "stakeholder management",
                     "process improvement", "data analysis", "uml", "jira", "agile",
                     "business intelligence", "reporting", "tableau"],
        "skills": ["Requirements Gathering", "SQL", "Excel", "Stakeholder Management",
                   "Process Improvement", "Data Analysis", "Jira", "Agile", "Tableau"],
        "description": "Bridges the gap between IT and business through analysis."
    },

    # Other
    "QA Engineer": {
        "keywords": ["testing", "selenium", "automation", "manual testing", "test cases",
                     "jira", "agile", "api testing", "postman", "cypress", "jest",
                     "performance testing", "regression testing"],
        "skills": ["Selenium", "Automation Testing", "Manual Testing", "API Testing",
                   "Postman", "Cypress/Jest", "Jira", "Performance Testing", "CI/CD"],
        "description": "Ensures software quality through systematic testing."
    },
    "Database Administrator": {
        "keywords": ["sql", "mysql", "postgresql", "oracle", "mongodb", "database design",
                     "backup", "recovery", "performance tuning", "indexing", "replication"],
        "skills": ["SQL", "MySQL/PostgreSQL", "Oracle", "MongoDB", "Database Design",
                   "Backup & Recovery", "Performance Tuning", "Replication"],
        "description": "Manages and maintains database systems."
    },
    "HR Manager": {
        "keywords": ["recruitment", "onboarding", "employee relations", "performance management",
                     "compensation", "training", "labor law", "hris", "talent acquisition",
                     "organizational development"],
        "skills": ["Recruitment", "Onboarding", "Employee Relations", "Performance Management",
                   "Compensation & Benefits", "Training & Development", "HRIS", "Labor Law"],
        "description": "Manages human resources operations and employee experience."
    },
}
