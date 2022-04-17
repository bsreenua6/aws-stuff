import boto3

ec2_resource = boto3.resource('ec2', region_name='us-east-1')

#filter for non 'Application' tagged Ec2 instances
for instance in ec2_resource.instances.all():
    if 'Application' not in [tag['Key'] for tag in instance.tags]:
         print(instance.id)
         #stop the non 'Application' tagged Ec2 instances
         instance.stop()
