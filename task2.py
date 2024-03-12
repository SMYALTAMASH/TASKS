import boto3

VPC_ID = 'vpc-12345678'  # Example VPC ID

YOUR_NAME = 'masterAlt'

def lambda_handler(event, context):
    # Initialize the AWS clients
    ec2_client = boto3.client('ec2')
    s3_client = boto3.client('s3')

    # Create EC2 instances
    for i in range(1, 11):
        instance_name = f"myinstance{i}"
        ec2_instance = ec2_client.run_instances(
            ImageId='ami-0abcdef1234567890', 
            InstanceType='t3.micro',
            MinCount=1,
            MaxCount=1,
            SubnetId='subnet-12345678',  
            SecurityGroupIds=['sg-0123456789abcdef0'], 
            KeyName='my_key_pair', 
            TagSpecifications=[{
                'ResourceType': 'instance',
                'Tags': [{'Key': 'Name', 'Value': instance_name}]
            }]
        )
        instance_id = ec2_instance['Instances'][0]['InstanceId']
        
        # Write instance ID to a local file
        with open(f'/tmp/{instance_name}_id.txt', 'w') as file:
            file.write(instance_id)

        # Upload the local file to the respective S3 bucket
        bucket_name = f'{YOUR_NAME}-mys3bucket{i}'
        s3_client.upload_file(f'/tmp/{instance_name}_id.txt', bucket_name, f'{instance_name}_id.txt')

    return {
        'statusCode': 200,
        'body': 'EC2 instances and S3 buckets created successfully!'
    }

