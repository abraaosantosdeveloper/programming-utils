import mysql.connector

"""
>>>WARNING<<<
Before using this file, make sure to follow the steps below:

1. Open you cmd or terminal
2. run the command: pip install mysql-connector-python
3. DO NOT RUN pip install mysql-connector
    reason: this can cause conflicts between the two libraries
    and your app WILL NOT RUN. The first one is discontinued.
4. Open your app, code and be happy. =]

======== THANK ME LATER ========
--- Have a nice coding night ---
"""

# if the db is running in the same computer
# you can use both 127.0.0.1 and localhost
# The standard port is 3306, but you better always check
# so that you can use the correct port
hostname = "127.0.0.1"
port = "3306"

# DBMS credentials - you can create these
# credentials as well if you want
user = "root"
pswd =""

# Database name - replace with your db name
db = "db_name"

# This is the primary function to execute
# the basics: set the connection
def con():
    cnx = mysql.connector.connect(host=hostname,
    port=port,
    user=user,
    password=pswd,
    database=db)
    return cnx

# Use this function when you need to update
# the information in the DB or insert new data

# This function was updated

# def executeCommand(command:str):
#     cnx = con()
#     cursor = cnx.cursor()
#     cursor.execute(command)
#     cnx.commit()
#     cnx.close()

def executeCommand(command:str, params=None):
    cnx = con()
    cursor = cnx.cursor()
    if params:
        cursor.execute(command, params)
    else:
        cursor.execute(command)
    cnx.commit()
    cnx.close()

# This function just execute a data request.
# You can use it when you need to return any data
# from db
# The only difference between this function 
# and the one above is the use of the return 
# and fetch all statements.

# This function was updated

# def executeQuery(query:str) -> list:
#     cnx = con()
#     cursor = cnx.cursor()
#     cursor.execute(query)
#     result = cursor.fetchall()
#     cnx.close()
#     return result

def executeQuery(query:str, params=None) -> list:
    cnx = con()
    cursor = cnx.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    result = cursor.fetchall()
    cnx.close()
    return result

# Use this function when you want the app to return the first position data in query only

def executeSingleFetchQuery(query:str, params=None):
    cnx = con()
    cursor = cnx.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    result = cursor.fetchone()
    cnx.close()
    return result
