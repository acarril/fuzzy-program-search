import boto3
from chalice import Chalice
from chalicelib import db, unfuzz

app = Chalice(app_name='fuzzy-program-search')

def dummy():
    """
    Collection of all s3.client() functions.
    The sole purpose is to force Chalice to generate the right permissions in the policy.
    Does nothing and returns nothing.
    """
    s3 = boto3.client('s3')
    s3.put_object()
    s3.download_file()
    s3.get_object()
    s3.list_objects_v2()
    s3.get_bucket_location()

@app.route('/')
def index():
    if False:
        dummy()
    return {'hello': 'world'}

@app.route('/fuzzysearch', methods=['POST'])
def fuzzysearch():
    body = app.current_request.json_body
    query, query_type = body['query'], body['query_type']
    df = db.OptionsDB(query_type+'.csv').read_csv_from_s3()
    return unfuzz.Choices(df).fuzzy_search(query=query)

