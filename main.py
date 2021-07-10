"""
1. Requirement: Create an API Service to fetch the statistics of the contributors of user specified GitHub repositories
in the Amazon Web Services Environment.
2. Identify and list unique domains to the specified repository and sort them by the number of commits per contributor
for all the branches.
3. The Repository name and Date are the parameters to be passed for the REST API to fetch the contributor data.
4. Create a table in AWS Relational Database Service SQL instance for storing the data pertaining to the fields Unique
ID, Repo Name, Domain Name, Count, Date range parameter, Date of Run collected using API.
"""

# Importing Necessary Packages
import requests
import pandas as pd

# Input - GitHub Username & Date
# Repo_Name = input("Enter the GitHub Repository Name (Username/Repo Name):- ")
# Start_Date = input("Enter the Start Date (YYYY-MM-DD):- ")
# End_Date = input("Enter the End Date (YYYY-MM-DD):- ")


# Pre-Input Data
Repo_Name = 'hashicorp/consul'  # Repository Name
Start_Date = '2021-07-07'       # Start Date of Range
End_Date = '2021-07-09'         # End Date of Range

Data_Frame = pd.DataFrame()
Output_Json = {}

# Fetching the JSON Data from the API
# URL to which the Request will be sent to
Auth = {'Authorization': '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'}
url = f"https://api.github.com/repos/{Repo_Name}/commits?since={Start_Date}&until={End_Date}"

# Making a GET Request to the GitHub API
request = requests.get(url, Auth).json()
length = len(request)       # To examine the Total Commits taken place

# Checking if the request was received or not
if request:
    # Concatenating the JSON Data into the Data Frame and re-setting its Index
    Data_Frame = pd.concat([Data_Frame, pd.DataFrame(request)], ignore_index=True)

New_Data_Frame = Data_Frame

for request in New_Data_Frame['commit']:
    Email_Id = request['author']['email']       # Taking the Email ID of the Author
    Email_End = Email_Id.split('@')             # Splitting the Email ID into Username and Domain Name
    Company = Email_End[1].rsplit('.', 1)       # Splitting the Domain Name into the Company Name and the extension
    Company_Name = Company[0]                   # Storing the Company Initial Name

    if Company_Name in Output_Json.keys():
        Output_Json[Company_Name]['Total Contributions'] = Output_Json[Company_Name]['Total Contributions'] + 1
    else:
        Output_Json[Company_Name] = {'Total Contributions': 1, 'Unique Contributors': 0, 'Users': []}

    if Email_Id not in Output_Json[Company_Name]['Users']:
        Output_Json[Company_Name]['Users'].append(Email_Id)
        Output_Json[Company_Name]['Unique Contributors'] = Output_Json[Company_Name]['Unique Contributors'] + 1

# Output -  Company Domain Name, Total number of Commits & Total number of Contributors
print(f'Total Commits:- {length}')
print(f'Total Companies:- {list(Output_Json.keys())}')
print(f'Output:- {Output_Json}')


"""
Input : Repository name
Output: Company domain name, along with total number of commits and total number of contributors

Input: hashicorp/consul
Output should be: { "microsoft": { Total Contributions: 50, Unique Contributors: 10 } 
"hashicorp": {Total Contributions: 15, Unique Contributors: 12 } , "gmail": { Total Contributions: 50, 
Unique Contributors: 11 } , "cloudflare": { Total Contributions: 52, Unique Contributors: 10 } }
"""