import json
import urllib.parse
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = boto3.client('s3')

def lambda_handler(event, context):
    logger.info("Received event: %s", json.dumps(event))

    # Get bucket and object details from S3 event
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    object_key = urllib.parse.unquote_plus(
        event['Records'][0]['s3']['object']['key']
    )

    destination_bucket = source_bucket.replace("input", "output")
    destination_key = f"processed-{object_key}"

    try:
        # Copy object to output bucket with new name
        s3.copy_object(
            Bucket=destination_bucket,
            CopySource={'Bucket': source_bucket, 'Key': object_key},
            Key=destination_key
        )

        logger.info(
            "Successfully processed %s from %s to %s",
            object_key,
            source_bucket,
            destination_bucket
        )

        return {
            "statusCode": 200,
            "body": json.dumps("Image processed successfully")
        }

    except Exception as e:
        logger.error("Error processing image: %s", str(e))
        raise
