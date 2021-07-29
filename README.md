# Lambda Start/ Stop EC2 Instances
Start and Stop EC2 instances in controlled fashion using Lambda function backed by Python Boto3

The functions defined have two type of instances that are started or stopped through a Lambda function as below.

## Serial Instances:
These instances are started or stopped in the order they are listed and one instance will start at a time and the process will wait till it is in running state before it starts or stops the next instance.

## Parallel Instances:
These instances are started or stopped after all of Serial instances are in the required state. Parallel instances wait for Serial instances to finish and then parallel instances are triggered st the same time.

# IAM Role Security Policy
In order to run these Lambda functions, you will require a minimum of EC2 Stop, Start, DescribeInstances and ReportInstanceStatus permissions in a policy and role assigned to Lambda functions. A sample of JSON policy is available in this repository which you can change according to your requirements. The JSON policy in this example restricts start and stop access to instances with a specific tag defined and set to true.

