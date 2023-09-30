import os
import pymongo
import mysql.connector
import json
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.assignment_2_db
collection = db.databases
#Export MongoDB Data into a JSON File
os.system("mongoexport --collection=databases --db=assignment_2_db --out=export.json")

mydb = mysql.connector.connect(
host='10.128.0.3',
user="gayatri_1",
password="pvsnm_99",
database="assignment_2_db"
)
mycursor = mydb.cursor()
print("Connected to MySQL...")

# Create a table in MySQL
sql = "CREATE TABLE dbs(name varchar(50),assignment int(2))"
mycursor.execute(sql)
print("Table Created")

for line in open('export.json','r'):
    k = 1
    entry = json.loads(line)
    n = entry['name']
    a = entry['assignment']
    print("Record ",k,": (Name, Assignment) = (",n,a,")")
    sql = ("INSERT INTO dbs(name, assignment) VALUES (%s, %s)")
    val = (n, a)
    mycursor.execute(sql, val)
    mydb.commit()
    print("Inserted entries into MySQL...")