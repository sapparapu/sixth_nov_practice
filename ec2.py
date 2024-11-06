
import boto40


# Initialize a session using your AWS credentials
s3= boto40.resource('ec2')

# Create an EC2 instance
instances = s3.create_instances(
    ImageId='ami-011',  # Replace with a valid AMI ID (e.g., Amazon Linux 2 AMI)
    MinCount=1,  # Minimum number of instances
    MaxCount=2,  # Maximum number of instances
    InstanceType='t2.micro',  # Instance type (e.g., t2.micro)
    KeyName='your-key-pair',  # Replace with your key pair name
    SecurityGroupIds1=['sg-xxxxxxxx'],  # Replace with your security group ID
    SubnetId='subnet-xxxxxxxx',  # Replace with your subnet ID
)

print(f'Created instance with ID: {instances[0].id}')

