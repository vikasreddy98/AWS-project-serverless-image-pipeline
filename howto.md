# Build & Implementation Guide

This document provides a step-by-step walkthrough of how this serverless image processing pipeline was built.

---

## Phase 1 – S3 Buckets

### Create Input Bucket
- Created a private S3 bucket to receive image uploads
- Public access blocked to maintain security

![Input Bucket](https://github.com/vikasreddy98/AWS-project-serverless-image-pipeline/blob/8e13086f1f4ac70ffe94fc2ea49572b11ce8868d/screenshots/s3-input-bucket.png)

### Upload Test Image
- Uploaded a sample image to trigger the pipeline

![S3 Upload](screenshots/s3-upload.png)

---

## Phase 2 – IAM Role

### Lambda Execution Role
- Created a dedicated IAM role for Lambda
- Attached AWSLambdaBasicExecutionRole for logging
- Added inline policy for least-privilege S3 access

![IAM Role Permissions](screenshots/iam-inline-policy.png)

---

## Phase 3 – Lambda Function

### Function Creation
- Created Lambda function using Python 3.12
- Attached existing IAM role

![Lambda Function](screenshots/lambda-function.png)

### Lambda Code
- Reads image from input bucket
- Copies image to output bucket with new name
- Logs execution details

![Lambda Code](screenshots/lambda-code.png)

---

## Phase 4 – Testing & Verification

### Output Bucket Verification
- Processed image appears automatically in output bucket

![Output Bucket](screenshots/s3-output-object.png)

### CloudWatch Logs
- Verified successful Lambda execution via logs

![CloudWatch Logs](screenshots/cloudwatch-logs.png)

