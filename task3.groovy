pipeline {
    agent any

    environment {
        AWS_DEFAULT_REGION = 'YOUR_REGION'
    }

    stages {
        stage('Build Lambda Function') {
            steps {
                sh '''
                    zip -r lambda.zip .
                '''
            }
        }

        stage('Deploy Lambda with CloudFormation') {
            steps {
                script {
                    def templateBody = readFile('lambda.yaml')
                    def changeSetName = "lambda-deployment-${BUILD_NUMBER}"

                    sh """
                        aws cloudformation create-change-set \
                            --change-set-name ${changeSetName} \
                            --stack-name lambda-stack \
                            --template-body "${templateBody}" \
                            --capabilities CAPABILITY_IAM
                    """

                    sh """
                        aws cloudformation execute-change-set \
                            --change-set-name ${changeSetName}
                    """
                }
            }
        }
    }

}

triggers {
    cronJob('0 0 * * *', 'GMT')
}

