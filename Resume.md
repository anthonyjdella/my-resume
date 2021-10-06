# State Farm

* Backend: Develop, test, deploy, and maintain business critical RESTful API's using Java & Spring Boot framework that serves data and handles over 100,000 requests to our insurance policy platform, to prevent millions in monetary loss.
    * Java, Spring Boot, Maven, Postgres, JUnit

* Integration Layer: Design and implement a microservice integration layer using Java & Spring Boot to abstract components between our core application and outbound calls to high-impact business data which help calculate insurance rates.
    * Java, Spring Boot, PolicyCenter, Maven, JUnit

* DevOps: Improve software release efficiency up to 50%, by creating continuous integration and deployment pipelines to automatically build, scan, test, and deploy software, which reduces the time-to-market.
    * Gitlab CI/CD, Jenkins, Karate Tests

* Automation: 


    Implement chaos engineering pipelines which introduce chaos into our environments so that we can prepare for them in production.

    Research and implement new tools and best practices within our Products so that we are cutting edge and cool.

    Set up Continuous Integration pipelines that perform scans, run unit tests, 

    Set up a logging framework which uses SLF4J to log not only a message, but also meta data related to input parameters.


### List of involvements:
1. Inflation Index
2. Consumer Reports
3. CI Pipeline
4. Chaos Engineering
5. Automation Testing
6. Logging Framework

### What do these products do?
1. Inflation Index is a REST service which gets the inflated Coverage amount. That amount usually increases over time due to inflation.
2. Consumer Reports is an Integration layer and REST service which orders business-critical consumer reports.
3. CI/CD pipeline is how we integrate and deploy our code into various environments.

### Why is it needed?
1. Inflation Index is needed during the Renter's insurance quote process to retrieve the correct coverage amount, based on date. As a business, we don't want that amount to be static, otherwise it will lose value over time.
2. Consumer Reports are needed during the Renter's insurance quote process to see if the customer has any consumer report (auto, property, policy) history tied to their name. This is one determining factor in how their rates will be calculated.
3. CI/CD is needed because it automates the build and deploy process so that we don't have to manually do it each time. It also has checks in place, so we know we are deploying good code.

### How do they work at a high level?
1. Inflation Index is written in Java and uses Spring Boot framework. We have 2 operations, one GET and one POST. 
    - The GET operation gets the inflation index based on the date given, which is passed in via query string parameters. Using JDBC (java database connectivity), we do a SQL query on a Postgres DB to get the inflation amount. 
    - The POST operation gets the inflation index based on the current date and a prior date, which is passed in via request body. A comparision between the two values is done, and the higher amount is returned.
2. Consumer Reports is written in Java and uses Spring Boot framework. We have two integration layers which take calls from PolicyCenter and fetches data from a downstream service. This integration layer is useful so that the data from downstream and upstream are abstracted. This helps with testablility & deployments as they can be tested & deployed independently. This is a micro service architecture.
    - Both layers, are Spring Boot projects with two POST operations. They both take in a request body which is sent from the upstream service, which is then processed and passed to a downstream service. Then the response goes the opposite direction. The downstream service is more of a black box, as we also do work on the upstream system.
3. CI Pipeline is created when developers push code into the repository. CD Pipeline is created when code is merged into main/master branch.
    - Below are details for each step. Old CD pipeline took 30 minutes, and I reduced to to 15 minutes by
    - Removing redundancy (steps and jobs), performing a shallow clone instead of a full clone (which basically just clones the changes you made rather than all of the commit history), reduce mutation testing time by implementing incremental mutation analysis that only checks for new code, running stages in parallel/asyncronously instead of step-by-step, & caching data of dependencies instead of downloading them each time.

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


### Renters Metrics for 2020 (yearly):
    Number of Applications: 2 million (70,000 in Ohio)
    Number of Quotes:       3.5 million (100,000 in Ohio)
    Number of Policies:     3.8 million (170,00 in Ohio)


---

# Bank of America


---

# GM Financial

---

