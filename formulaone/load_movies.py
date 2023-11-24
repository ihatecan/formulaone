import boto3
from boto3.dynamodb.conditions import Key
import simplejson as json 
from helpers import get_raw_data_path

with open("config.json", "r") as f:
    keys = json.load(f)


session = boto3.Session(
    aws_access_key_id=keys["aws_access_key_id"],
    aws_secret_access_key=keys["aws_secret_access_key"]
)

dynamo_resource = session.resource(
    'dynamodb',
    region_name='eu-west-1'
)

movies = dynamo_resource.Table('doc-example-table-movies')


df = movies.query(
    KeyConditionExpression=Key('year').eq(2013)
)


raw_data_path = get_raw_data_path()
raw_data_path.mkdir(parents=True, exist_ok=True)

with open(raw_data_path / 'rawdata.json', 'w') as f:
    json.dump(df, f, indent=2)