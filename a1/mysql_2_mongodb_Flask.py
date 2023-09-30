from flask import Flask
import os
import pymongo
import mysql.connector
import json

app = Flask(__name__)

@app.route('/')

def datamigration_sql_2_mongo():
        mysqldb = mysql.connector.connect(host='10.128.0.3',database="assignment_2_db",user="gayatri_1",password="pvsnm_99")
        print("Connected to MySQL...")
        mycursor = mysqldb.cursor(dictionary=True)
        mycursor.execute("SELECT * from dbs")
        myresult = mycursor.fetchall()
        print(myresult)

        print("Connecting to MongoBD...")
        mongodb_host = "mongodb://10.128.0.2:27017/"
        mongodb_dbname = "assignment_2_db"

        print("Successful! Connected to MongoDB...")
        myclient = pymongo.MongoClient(mongodb_host)
        mydb = myclient[mongodb_dbname]
        mycol = mydb["databases"]


        if len(myresult) > 0:
           x = mycol.insert_many(myresult)
           print(len(x.inserted_ids))
        print("Document Inserted!")
        return "Data Migration from Sql to Mongodb done using Flask API\n"

if __name__ == '__main__':

    app.run()