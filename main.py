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
import pymysql
from datetime import date, datetime

Start_Time = datetime.now()
# Input - GitHub Username & Date Range
# Repo_Name = input("Enter the GitHub Repository Name (Username/Repo Name):- ")
# Start_Date = input("Enter the Start Date (YYYY-MM-DD):- ")
# End_Date = input("Enter the End Date (YYYY-MM-DD):- ")


# Pre-Input Data
Repo_Name = 'hashicorp/consul'  # Repository Name
Start_Date = '2021-07-01'       # Start Date of Range
End_Date = '2021-08-13'         # End Date of Range

Auth = {'Authorization': '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'}    # Authorization Token
Run_Date = date.today()         # Run_Date to get today's date
Data_Frame = pd.DataFrame()     # Creating Pandas DataFrame to store in the data
Output_Json = {}                # Output_Json will contain the main output of the code
Length_Sum = 0                  # To keep the count of the Total Contributions made
Unique_Sum = 0                  # To keep the count of the Unique Contributors
Page_Number = 1                 # Page_Number for getting requests from more than 1 page

# Fetching the JSON Data from the API
while True:
    # URL to which the Request will be sent to fetch the details of the Commits and all other stuffs
    url = f"https://api.github.com/repos/{Repo_Name}/commits?page={Page_Number}&since={Start_Date}&until={End_Date}"

    # Getting the request
    Request = requests.get(url, Auth).json()

    # Taking the length of the request received
    Length = len(Request)

    # 'Length_Sum' analyse us with the Total Contribution made within the given Date Range
    Length_Sum += Length

    # Checking if the request was received or not
    if Request:
        # Concatenating the JSON Data into the 'Data_Frame' and re-setting its Index
        Data_Frame = pd.concat([Data_Frame, pd.DataFrame(Request)], ignore_index=True)

        # Incrementing the 'Page_Number'
        Page_Number = Page_Number + 1
    else:
        # If no 'Request' has been received then it will run the following and break the loop and exit it
        # URL to which the Request will be sent to fetch the Languages
        url = f"https://api.github.com/repos/{Repo_Name}/languages"

        # Getting the request
        Response = requests.get(url, Auth).json()
        Total_Bytes = 0         # To keep the count of the Total Bytes

        # Calculating the Total Bytes
        for x in Response:
            Total_Bytes += Response[x]

        # Calculating the Percentage
        for x in Response:
            # Calculating the Percentage and rounding of to 2 places
            Percentage = round((Response[x] / Total_Bytes * 100), 2)
            Response[x] = f'{Percentage}%'
        break

New_Data_Frame = Data_Frame                     # Copying it to New DataFrame

# Processing the JSON Data Received from the API
for Request in New_Data_Frame['commit']:
    Email_Id = Request['author']['email']       # Taking the Email Id of the Author
    Email_End = Email_Id.split('@')             # Splitting the Email Id into Username and Domain Name

    Company = Email_End[1].rsplit('.', 1)       # Splitting the Domain Name into the Company Name and the Extension
    Company_Name = Company[0]                   # Storing the Company Initial Name

    Full_Date = Request['author']['date']       # Taking the Date and Time when the commit took place
    Only_Date = Full_Date.split('T')            # Splitting the Full_Date into Date and the Time
    Date = Only_Date[0]                         # Storing the Date only

    # Loop for Processing the Total Contributions
    if Company_Name in Output_Json.keys():
        # If the 'Company_Name' is already present then it will increment the 'Total Contributions' by 1
        Output_Json[Company_Name]['Total Contributions'] = Output_Json[Company_Name]['Total Contributions'] + 1
    else:
        # If the 'Company_Name' is not present then it will assign the 'Total Contributions' to 1
        Output_Json[Company_Name] = {'Total Contributions': 1, 'Unique Contributors': 0, 'Users': [], 'Date': []}

    # Loop for Processing the Unique Contributors
    # If the particular 'Email_Id' is already present then the loop won't run, whereas if it's not present then the loop will run
    if Email_Id not in Output_Json[Company_Name]['Users']:
        # Adding the Users Email_Id inorder to make the 'Unique Contributors'
        Output_Json[Company_Name]['Users'].append(Email_Id)

        # Incrementing the 'Unique Contributors' by 1
        Output_Json[Company_Name]['Unique Contributors'] = Output_Json[Company_Name]['Unique Contributors'] + 1

        # 'Unique_Sum' analyse us with the Total Unique Contributors who made commits within the given Date Range
        Unique_Sum += 1

    # Loop for Processing the Commit Date
    if Date not in Output_Json[Company_Name]['Date']:
        Output_Json[Company_Name]['Date'].append(Date)

# Output -  Company Domain Name, Total number of Commits & Total number of Contributors
print(f'Total Companies:- {len(Output_Json)}-{list(Output_Json.keys())}')  # Printing the Domain/Companies name
print(f'Total Contributions:- {Length_Sum}')                               # Printing the Count of Total Contributions made
print(f'Unique Contributors:- {Unique_Sum}')                               # Printing the Count of Unique Contributors who have contributed
print(f'Languages Used:- {Response}')                                      # Printing the Languages
print(f'Output:- {Output_Json}')                                           # Printing the Required Json Data

# Loop for Storing the data into Database
# Establishing the connection/Connecting to the Database
connection = pymysql.connect(host="localhost", user="root", password="", database="mydb")
cur = connection.cursor()

# Query for Fetching the last 'UNIQUE_ID' from the Database
cur.execute("SELECT UNIQUE_ID FROM mydb.GitHub ORDER BY UNIQUE_ID DESC LIMIT 1;")

Unique_Id = cur.fetchall()
# Loop for Checking whether the Unique_Id is empty or not
if not Unique_Id:
    Unique_Id = 0
else:
    Unique_Id = int(Unique_Id[0][0])

for x in Output_Json:
    Unique_Id = Unique_Id + 1

    # Query for Inserting into Database
    cur.execute("INSERT INTO mydb.GitHub (UNIQUE_ID, REPO_NAME, DOMAIN_NAME, TOTAL_CONTRI, UNIQUE_CONTRI, COMMIT_DATE, DATE_OF_RUN) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                (str(Unique_Id), str(Repo_Name), str(x), str(Output_Json[x]['Total Contributions']), str(Output_Json[x]['Unique Contributors']), str(Output_Json[x]['Date']), str(Run_Date)))

    # Committing the changes in the Database
    connection.commit()

End_Time = datetime.now()
print(f'Execution Time:- {End_Time - Start_Time}')                      # Printing the Execution Time

"""                                                 
Input : Repository name
Output: Company domain name, along with total number of commits and total number of contributors

Input: hashicorp/consul
Output should be: { "microsoft": { Total Contributions: 50, Unique Contributors: 10 } 
"hashicorp": {Total Contributions: 15, Unique Contributors: 12 } , "gmail": { Total Contributions: 50, 
Unique Contributors: 11 } , "cloudflare": { Total Contributions: 52, Unique Contributors: 10 } }
"""
