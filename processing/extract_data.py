import boto3 
import pandas as pd 
from io import BytesIO

s3 = boto3.client("s3")
bucket = "xideralaws-curso-paoesquivel2026"
key = "titanic.csv"

def get_data():
    response = s3.get_object(Bucket=bucket, Key= key)
    df = pd.read_csv(BytesIO(response["Body"].read()))
    return df.head(5)

def get_reponse():
    response = "Extrayendo data"
    return response