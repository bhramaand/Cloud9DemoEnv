import boto3
s3 = boto3.client('s3')

r = s3.select_object_content(
        Bucket='jbarr-us-west-2',
        Key='sample-data/airportCodes.csv',
        ExpressionType='SQL',
        Expression="select * from s3object s where s.\"Country (Name)\" like '%United States%'",
        InputSerialization = {'CSV': {"FileHeaderInfo": "Use"}},
        OutputSerialization = {'CSV': {}},
)

for event in r['Payload']:
    if 'Records' in event:
        records = event['Records']['Payload'].decode('utf-8')
        print(records)
    elif 'Stats' in event:
        statsDetails = event['Stats']['Details']
        print("Stats details bytesScanned: ")
        print(statsDetails['BytesScanned'])
        print("Stats details bytesProcessed: ")
        print(statsDetails['BytesProcessed'])