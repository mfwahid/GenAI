import boto3
import json

s3_client = boto3.client('s3')
bedrock_client = boto3.client('bedrock-runtime')

class aws_s3:
    def __init__(self,bucket,path,filename):
        self.bucket = bucket
        self.path = path
        self.filename = filename


    def uploadJSONContenttoS3(aws_s3,content):
        s3path = aws_s3.path + "/" + aws_s3.filename
        s3_client.put_object(Bucket=aws_s3.bucket, Key=s3path, Body=json.dumps(content))
        print("content stored in S3 Bucket")
        return content

class aws_bedrock:
    def getTitanEmbedding(aws_bedrock,content):
        modelId = 'amazon.titan-embed-text-v1'
        contentType = 'application/json'
        accept = '*/*'
        body = json.dumps({
            "inputText": json.dumps(content)
        })

        response = bedrock_client.invoke_model(
            modelId=modelId,
            contentType=contentType,
            accept=accept, 
            body=body
        )

        print(response)
        response_body = json.loads(response.get('body').read())
        print(response_body)
        return response_body