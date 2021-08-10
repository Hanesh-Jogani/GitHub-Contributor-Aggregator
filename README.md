# GitHub Contributor Aggregator
An API Service to fetch the statistics of the contributors of user specified GitHub Repositories in the Amazon Web Services Environment.

## Tech Stack
- Python
  - Pandas
  - Requests
  - PyMySQL
- AWS
  - AWS API Gateway
  - AWS Secret Manager
  - AWS RDS
  - AWS Lambda

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
