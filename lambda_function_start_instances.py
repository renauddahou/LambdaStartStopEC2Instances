#### Start EC2 Instances ####
#### Author: Kamran Shah ####
#### Repository Address: https://github.com/shahkamran/LambdaStartStopEC2Instances
import boto3
# Change the region in below variable.
region = 'eu-west-2'
# Change the list of Instance IDs for serialised run. These instances will start in order they are listed, one at a time and will wait for an instance to be in running state before next instance is started.
serial_instances =   ['i-00000000000000001', 'i-00000000000000002', 'i-00000000000000003']
# Change the list of Instance IDs for parallel instances that will all run together after all of serial instances are in running state.
parallel_instances = ['i-0000000000000000a', 'i-0000000000000000b', 'i-0000000000000000c',]
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
# Start of loop over serial instances.
    for instance in serial_instances:
        ec2.start_instances(InstanceIds=[instance,])
        print('Starting instance: ' + str(instance))
        print('Wait till instance is running ' + str(instance))
        waiter = ec2.get_waiter('instance_running')
        waiter.wait(InstanceIds=[instance,])
        print('Instance is now running ' + str(instance))
        
# Start of all parallel instances.
    ec2.start_instances(InstanceIds=parallel_instances)
    print('started your parallel instances: ' + str(parallel_instances))

