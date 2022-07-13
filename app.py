import time
import pyodbc
import os
from flask import Flask, Request, render_template, request, flash
from azure.storage.blob import BlobServiceClient, ContentSettings, PublicAccess

app = Flask(__name__, template_folder="templates")

connection = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=tcp:adbdatabaseserver.database.windows.net,1433;Database=adbdatabase;Uid=adbserveruser;Pwd=Darshan@07;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30')

cursor = connection.cursor()


columnNames = ['Name','State', 'Salary', 'Grade', 'Room', 'Telnum', 'Picture', 'Keywords']
datasetPath = './people.csv'


@app.route('/', methods=['POST', 'GET'])
def Hello():
    return render_template('index.html')

if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    
    app.run()

