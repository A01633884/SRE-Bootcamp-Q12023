import mysql.connector
import boto3
import os
import jwt

ENDPOINT = "sre-bootcamp-selection-challenge.cabf3yhjqvmq.us-east-1.rds.amazonaws.com"
PORT = "3306"
USER = "secret"
REGION = "us-east-1"
DBNAME = "bootcamp_tht"
os.environ['LIBMYSQL_ENABLE_CLEARTEXT_PLUGIN'] = '1'
session = boto3.Session(profile_name='default')
client = session.client('rds')


try:
    conn = mysql.connector.connect(
        host=ENDPOINT, user=USER, passwd="jOdznoyH6swQB9sTGdLUeeSrtejWkcw", port=PORT, database=DBNAME, ssl_ca='SSLCERTIFICATE')
except Exception as e:
    print("Database connection failed due to {}".format(e))
    
class Token:

    def generate_token(self, username, password):
        return 'test'


class Restricted:

    def access_data(self, authorization):
        return 'test'
