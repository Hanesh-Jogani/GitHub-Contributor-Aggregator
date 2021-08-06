"""
1. Requirement: Create an API Service to fetch the statistics of the contributors of user specified GitHub repositories
in the Amazon Web Services Environment.
2. Identify and list unique domains to the specified repository and sort them by the number of commits per contributor
for all the branches.
3. The Repository name and Date are the parameters to be passed for the REST API to fetch the contributor data.
4. Create a table in AWS Relational Database Service SQL instance for storing the data pertaining to the fields Unique
ID, Repo Name, Domain Name, Count, Date range parameter, Date of Run collected using API.
"""

# Importing Necessary Packages/Libraries
import requests
import pandas as pd
from datetime import date

# Input - GitHub Username & Date Range
# Repo_Name = input("Enter the GitHub Repository Name (Username/Repo Name):- ")
# Start_Date = input("Enter the Start Date (YYYY-MM-DD):- ")
# End_Date = input("Enter the End Date (YYYY-MM-DD):- ")


# Pre-Input Data
Repo_Name = 'hashicorp/consul'  # Repository Name
Start_Date = '2021-04-01'       # Start Date of Range
End_Date = '2021-08-05'         # End Date of Range

Auth = {'Authorization': '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'}    # Authorization Token
Run_Date = date.today()         # Run_Date to get today's date
Data_Frame = pd.DataFrame()     # Creating Pandas DataFrame to store in the data
Output_Json = {}                # Output_Json will contain the main output of the code
Length_Sum = 0                  # To keep the count of the Total Contributions made
Unique_Sum = 0                  # To keep the count of the Unique Contributors
page_number = 1

# Fetching the JSON Data from the API
while True:
    # URL to which the Request will be sent to
    url = f"https://api.github.com/repos/{Repo_Name}/commits?page={page_number}&since={Start_Date}&until={End_Date}"

    # URL to which the Request will be sent to
    request = requests.get(url, Auth).json()
    length = len(request)
    Length_Sum += length

    # Checking if the request was received or not
    if request:
        # Concatenating the JSON Data into the Data Frame and re-setting its Index
        Data_Frame = pd.concat([Data_Frame, pd.DataFrame(request)], ignore_index=True)

        # Incrementing the Page Number
        page_number = page_number + 1
    else:
        break

New_Data_Frame = Data_Frame     # Copying it to New DataFrame

# Processing the JSON Data Received from the API
for request in New_Data_Frame['commit']:
    Email_Id = request['author']['email']       # Taking the Email ID of the Author
    Email_End = Email_Id.split('@')             # Splitting the Email ID into Username and Domain Name

    Company = Email_End[1].rsplit('.', 1)       # Splitting the Domain Name into the Company Name and the Extension
    Company_Name = Company[0]                   # Storing the Company Initial Name

    Full_Date = request['author']['date']       # Taking the Date and Time when the commit took place
    Only_Date = Full_Date.split('T')            # Splitting the Full_Date into Date and the Time
    Date = Only_Date[0]                         # Storing the Date only

    if Company_Name in Output_Json.keys():
        Output_Json[Company_Name]['Total Contributions'] = Output_Json[Company_Name]['Total Contributions'] + 1
    else:
        Output_Json[Company_Name] = {'Total Contributions': 1, 'Unique Contributors': 0, 'Users': [], 'Date': []}

    if Email_Id not in Output_Json[Company_Name]['Users']:
        Output_Json[Company_Name]['Users'].append(Email_Id)
        Output_Json[Company_Name]['Unique Contributors'] = Output_Json[Company_Name]['Unique Contributors'] + 1
        Unique_Sum += 1

    if Date not in Output_Json[Company_Name]['Date']:
        Output_Json[Company_Name]['Date'].append(Date)

# Output -  Company Domain Name, Total number of Commits & Total number of Contributors
print(f'Total Companies:- {list(Output_Json.keys())}')  # Printing the Domain/Companies name
print(f'Total Contributions:- {Length_Sum}')            # Printing the Count of Total Contributions made
print(f'Unique Contributors:- {Unique_Sum}')            # Printing the Count of Unique Contributors who have contributed
print(f'Output:- {Output_Json}')                        # Printing the Required Json Data


"""
Input : Repository name
Output: Company domain name, along with total number of commits and total number of contributors

Input: hashicorp/consul
Output should be: { "microsoft": { Total Contributions: 50, Unique Contributors: 10 } 
"hashicorp": {Total Contributions: 15, Unique Contributors: 12 } , "gmail": { Total Contributions: 50, 
Unique Contributors: 11 } , "cloudflare": { Total Contributions: 52, Unique Contributors: 10 } }
"""
