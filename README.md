# GitHub Contributor Aggregator
An API Service to fetch the statistics of the contributors of user specified GitHub Repositories in the Amazon Web Services Environment.


## High Level Diagram
![image](https://user-images.githubusercontent.com/62371149/130456494-4be297f1-0dd4-43df-b4c0-8255000b9758.png)


## Tech Stack
- Python
  - Pandas
  - Requests
  - PyMySQL
- AWS
  - AWS API Gateway
  - AWS RDS
  - AWS Lambda


## Concepts
- Pagination
  - Pagination is a technique for partitioning web content into discrete pages, inorder to display the  content in a limited and absorbable way. For instance, imagine working with a API and where one has sent a request to the API and in return you get a huge data, so in order to display it on a single page you spread it among different more pages to make it look aesthetic, and also the client/user gets an idea of the total pages the data is stored over.
  - GitHub Documentation - [Click Here](https://docs.github.com/en/rest/guides/traversing-with-pagination)

- API Processing
  -  API is the abbreviation for Application Programming Interface, which is a software go-between that permits two applications to converse with one another. Each time you utilize an application like Facebook, send a text, or genuinely look at the climate on your telephone, you're utilizing an API. Processing the data received from the API inorder to get the desired data accorrding to the client/user is what is know as API Processing.
  -  GitHub REST API - [Click Here](https://docs.github.com/en/rest)

- RDS
  - Amazon RDS is an relational database help that gives you six recognizable dataset services to browse, including Amazon Aurora, MySQL, MariaDB, Oracle, Microsoft SQL Server, and PostgreSQL. This implies that the code, applications, and devices you as of now use today with your current database can be utilized with Amazon RDS.
  - AWS Documentation - [Click Here](https://aws.amazon.com/rds/)

- Execution Time
  -  The execution time of a given task is characterized as the time spent by the system/framework executing that assignment, in alternate manner one can say the time during which a program is running.
  -  In Python, one can use `time` or `datetime` for fetching the time at different stages of the code and post manipulating the differnece of time you get the Execution Time.


## Installation
### Create Virtual Environment
virtualenv is used to manage Python packages for different projects. Using virtualenv allows you to avoid installing Python packages globally which could break system tools or other projects. You can install virtualenv using pip.
* Install Virtualenv
```
pip install virtualenv
```

* Create a Virtual Environment
```
python -m venv env
```

* Activate the Virtual Environment
```
.\env\Scripts\activate
```

### Install the Packages
* [Pandas](https://pandas.pydata.org/)
```
pip install pandas
```

* [Requests](https://docs.python-requests.org/en/master/)
```
pip install requests
```

* [PyMySQL](https://pymysql.readthedocs.io/en/latest/)
```
pip install PyMySQL
```


## Getting Started
* Clone the Project
```
git clone https://github.com/Hanesh-Jogani/GitHub-Contributor-Aggregator.git
```

* Navigate to the Project Directory
```
cd GitHub-Contributor-Aggregator
``` 

* Install the Packages as shown above

* Run the main.py file
```
python main.py
```
