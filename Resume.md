# Resume Content

<details>
  <summary>State Farm</summary>

* Backend: Develop, test, deploy, and maintain business-critical RESTful APIs using Java & Spring Boot framework that serves data and handles 100,000+ requests to our insurance policy platform, to prevent millions in monetary loss.

* Integration Layer: Design and implement a microservice integration layer utilizing Java & Spring Boot to abstract components between our core application and outbound calls to high-impact business data, which help calculate insurance rates.

* DevOps: Optimize software release efficiency up to 50% by creating CI/CD pipelines that automatically build, scan, test, and deploy software, which improves time-to-market.

* Chaos Engineering: Reduce web service unplanned downtime by implementing Chaos Engineering tools to determine potential failure points, which saves time and costs.

* Automation: Perform BDD using Agile methodology by writing automated E2E UI tests in CodeceptJS and Gherkin to quickly and effectively validate business scenarios.

* Quality: Provide guidance and leadership to implement best practices and tools for optimizing team productivity, spearhead document creation of solution architecture, and create dashboards & reports for management.

    * Java, Spring Boot, PolicyCenter, Maven, Postgres, JUnit, Git
    * Gitlab CI/CD, Jenkins, Karate Tests

---

### List of involvements:
1. Inflation Index
2. Consumer Reports
3. CI/CD Pipeline
4. Chaos Engineering
5. Automation Testing
6. Logging Framework & Best Practices

### What do these products do?
1. Inflation Index is a REST service which gets the inflated Coverage amount. That amount usually increases over time due to inflation.
2. Consumer Reports is an Integration layer and REST service which orders business-critical consumer reports.
3. CI/CD pipeline is how we integrate and deploy our code into various environments.
4. Chaos engineering tools are used to perform experiments on the system in order to adapt and build confidence to unexpected conditions.
5. Automation testing is used to automated workflows in our application with randomly generated data, so we can validate business scenarios.
6. Best practices and team improvements.

### Why is it needed?
1. Inflation Index is needed during the Renter's insurance quote process to retrieve the correct coverage amount, based on date. As a business, we don't want that amount to be static, otherwise it will lose value over time.
2. Consumer Reports are needed during the Renter's insurance quote process to see if the customer has any consumer report (auto, property, policy) history tied to their name. This is one determining factor in how their rates will be calculated.
3. CI/CD is needed because it automates the build and deploy process so that we don't have to manually do it each time. It also has checks in place, so we know we are deploying good code.
4. Chaos Engineering helps find unexpected failures before they become system outages. Since many systems are loosly coupled and follow microservice architecture, integrating them is difficult.
5. Automation testing is needed so that we don't have to manually view various workflows to see if they are passing. Instead, we can create a test that automatically flows through the user interface with generated data, so we can quickly validate scenarios. BDD helps the team work by collaborating with the team before development begins. We look at the requirements and plan out an expected automation test for the scenario. Then we develop the feature code from there. E2E testing is the process of testing an applications workflow from start to finish.
6. Best practices help ensure that our team is modernized and reaching its maximum potential.

### How do they work at a high level?
1. Inflation Index is written in Java and uses Spring Boot framework. We have 2 operations, one GET and one POST. 
    - The GET operation gets the inflation index based on the date given, which is passed in via query string parameters. Using JDBC (java database connectivity), we do a SQL query on a Postgres DB to get the inflation amount. 
    - The POST operation gets the inflation index based on the current date and a prior date, which is passed in via request body. A comparision between the two values is done, and the higher amount is returned.
2. Consumer Reports is written in Java and uses Spring Boot framework. We have two integration layers which take calls from PolicyCenter and fetches data from a downstream service. This integration layer is useful so that the data from downstream and upstream are abstracted. This helps with testablility & deployments as they can be tested & deployed independently. This is a micro service architecture.
    - Both layers, are Spring Boot projects with two POST operations. They both take in a request body which is sent from the upstream service, which is then processed and passed to a downstream service. Then the response goes the opposite direction. The downstream service is more of a black box, as we also do work on the upstream system.
3. CI Pipeline is created when developers push code into the repository. CD Pipeline is created when code is merged into main/master branch.
    - Below are details for each step. Old CD pipeline took 30 minutes, and I reduced to to 15 minutes by
    - Removing redundancy (steps and jobs), performing a shallow clone instead of a full clone (which basically just clones the changes you made rather than all of the commit history), reduce mutation testing time by implementing incremental mutation analysis that only checks for new code, running stages in parallel/asyncronously instead of step-by-step, & caching data of dependencies instead of downloading them each time.
4. Chaos Engineering for Spring Boot is a dependency that adds Spring Boot Actuator endpoints to your application. All you have to do is hit these endpoints at runtime to run assaults. The three main assaults are latency, exception, and appkiller. Latency adds a specified amount of latency to a request, so you can see how your service responds (i.e will it timeout). Exception assaults determine what happens incase of specified exceptions (i.e what happens if a database connection is down and throws an exception). AppKiller assaults shut down the application to see how it responds (i.e will it startup again).
5. We use a framework called CodeceptJS to write scenarios in Gherkin language, an easy to read language for everyone, to perform end to end user interface tests that automatically flow through a workflow to validate business scenarios.
6. Created documentation for our web services as well as other solutions. Implemented best practices for commit messages, semantic versioning, dependency updater, code formatting, logging framework (using SLF4J to log not only a message, but also metadata related to input parameters), team dashboards and metrics, etc. These dashboards identified the health of our services and downstream services and alerted us if they are down.

---

### OLD CI/CD Time:
#### CI:
- Maven Verify (Build, Compile, Unit & Mutation Tests, Code Coverage Report) 
    - 9 minutes
- Dependency Scan to check for vulternabilities with dependencies
    - 1 minute
- Static Scan to check source code for security vulnerabilities
    - 6 minutes
- Semantic versioning to increment our version number
    - 30 seconds
* Total time is 15 minutes
#### CD:
- Maven Verify (Build, Compile, Unit & Mutation Tests, Code Coverage Report) 
    - 9 minutes
- Dependency Scan to check for vulternabilities with dependencies
    - 1 minute
- Static Scan to check source code for security vulnerabilities
    - 6 minutes
- Deploy to various environments
    - 8 minutes
- Karate Integration tests
    - 3 minutes
- Upload EOT
    - 30 seconds
* There are more steps but total time is 30 minutes.

### NEW CI/CD Time:
#### CI:
- Maven Verify (Build, Compile, Unit & Mutation Tests, Code Coverage Report) 
    - 8 minutes
- Dependency Scan to check for vulternabilities with dependencies
    - 1 minute
- Static Scan to check source code for security vulnerabilities
    - 6 minutes
- Semantic versioning to increment our version number
    - 30 seconds
* Total time is 15 minutes
#### CD:
- Deploy to various environments
    - 8 minutes
- Karate Integration tests
    - 3 minutes
- Upload EOT
    - 30 seconds

---

### Renters Metrics for 2020 (yearly):
    Number of Applications: 2 million (70,000 in Ohio)
    Number of Quotes:       3.5 million (100,000 in Ohio)
    Number of Policies:     3.8 million (170,00 in Ohio)

</details>

---

<details>
  <summary>Bank of America</summary>

* Frontend: Develop a frontend web application written in TypeScript, which manages customer banking appointments and 20,000+ associate schedules.

* Troubleshooting: Collaborate with stakeholders and product teams to implement business requirements and resolve technical defects and bugs.

* Metrics: Perform analysis on internal hiring data and create weekly reports for senior management to build teams based on skillsets and experience.

    * JavaScript, CSS, HTML, SVN, MVC Architecture

---

### List of involvements:
1. Banking By Appointment
2. Defects
3. Reporting

### What do these products do?
1. Banking By Appointment was our web application under the Financial Technology Center. It is a modular administrative application for associates to manage banking appointments and schedules.
2. Fix defects and bugs that we missed during development.
3. Create metrics and reports for FTC hiring.

### Why is it needed?
1. Banking By Appointment is needed in each financial center to manage associates and customer relationships. It is used by over 20,000 associates throughout 4,600 financial centers.
2. Fix bugs so that the system works as expected.
3. Management needed a way to view hiring based on skills and job roles.
### How do they work at a high level?
1. There are 3 tabs on the application. It can be consumed by other modules, as a widget for other applications. 1st tab shows customer appointments for that day. It is a table with rows that show customers assigned to associates. 2nd tab shows upcoming appointments in the same format (for future days). 3rd tab shows appointments and walk-ins for that day. It is an overview page. The application code is written with Typescript, LESS, and Handlebars. Typescript is an extension of Javascript that adds syntax checks, auto-complete, etc. LESS is CSS but adds variables and functions. Handlebars allows expressions into your HTML so you can add javascript easily. It follows model-view-controller architecture. Model handles data, View displays the data, Controller controls flow and updates the View.
2. Get a defect from the test team. Work with them to understand the problem. Potentially speak with stakeholders to see the desired result. Then debug the issue and push the fix.
3. I would create weekly reports and do analytics on hiring data to present to management. They would use these reports to hire developers on their teams. The data came from Microsoft Access database, and I would import it and filter based on various roles.

</details>

---

<details>
  <summary>GM Financial</summary>

* ETL: Build data mapping transformations using ETL tools to extract, transform, and load data for various data warehouse projects.

* Database: Execute SQL search queries to filter data subsets needed for staging and transformation.

* Monitoring: Schedule, monitor, and configure automatic failure notifications for 700+ ETL workflows in production.

    * Informatica PowerCenter, ETL, Data Warehouse, SQL

---

### List of involvements:
1. ETL Project
2. Database
3. Monitor

### What do these products do?
1. Extract, transform, and load data between a source and target destination.
2. Write database queries to fetch and filter data.
3. Monitor workflows in production.

### Why is it needed?
1. Maybe to convert data, or to change data formats.
2. So you have the correct subset of data to transform.
3. To make sure workflows are running smoothly.

### How do they work at a high level?
1. In Informatica Powercenter, you have a source data table with a certain type of data. You then perform some type of operation on it depending on the need. This might be formatting dates, or changing data types. Then you export it to a new target source which could be a different database. Extract data from a desired subset of data, transform/convert data, create mappings from source to target tables, and load the result data into the target database.
2. Connect to a database or number of databases and write queries to filter them depending on the requirement.
3. Informatica Monitoring tool monitors CPU and memory & run-time stats of: workflows, SQL services, data objects, etc. Scheduling is a tool to make certain workflows run at a certain time. For example, maybe a source table has data that gets updated everyday, in order for the target data to be updated, the workflow needs to run. Monitoring tool looks at statistics of workflows to see if they are working properly. Failure notifications can be set up for each job, and if a failure occurs the team will get notified.

---

</details>
