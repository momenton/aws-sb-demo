import boto3
from time import sleep, time
from os import environ as env

REGION_NAME = env.get("REGION_NAME")
AWS_ACCESS_KEY_ID = env.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env.get("AWS_SECRET_ACCESS_KEY")
QUEUE_URL = env.get("QUEUE_URL")

print(REGION_NAME)

sqs = boto3.client('sqs',
                   region_name=REGION_NAME,
                   aws_access_key_id=AWS_ACCESS_KEY_ID,
                   aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

if __name__ == "__main__":
    # Get the queue. This returns an SQS.Queue instance
    for i in range(0, 100):
        while True:
            try:
                response = sqs.send_message(
                    QueueUrl=QUEUE_URL,
                    DelaySeconds=10,
                    MessageAttributes={
                        'Title': {
                            'DataType': 'String',
                            'StringValue': 'AWS Service Broker Demo'
                        },
                        'Author': {
                            'DataType': 'String',
                            'StringValue': 'Melchi Salins'
                        },
                        'WeeksOn': {
                            'DataType': 'Number',
                            'StringValue': '1'
                        }
                    },
                    MessageBody=(
                        "Hello Melbourne Kubernetes Meetup!!! "
                    )
                )
                print("Response MessageID: ", response["MessageId"])
                sleep(5)
            except Exception as e:
                print(e)
                print("Retrying in 5 seconds")
                sleep(5)
                continue
            break
