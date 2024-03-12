Jenkinsfile:

The pipeline defines stages for building the Lambda zip and deploying it using CloudFormation.
The Build Lambda Function stage zips the current directory content (assuming your code is there).
The Deploy Lambda with CloudFormation stage uses the AWS CLI to:
Read the CloudFormation template content.
Create a change set with the template and execute it to update the stack.
The pipeline triggers every Monday at 9:00 AM GMT using the cron job syntax.

CloudFormation Template (lambda.yaml):

This template defines an IAM role for the Lambda function and the Lambda function itself.
Update the Runtime property to match your Lambda script's runtime.
The template uses the !Sub function to reference the zipped Lambda code from the Jenkins workspace.

