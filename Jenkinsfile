def appName = 'my-python-app' // Must match your AWS ECR repo name
def awsAccountId = '708972351530' // e.g., 123456789012
def awsRegion = 'ap-south-1' 
def credentialsId = 'my-aws-iam-keys' // Your Jenkins credential ID

pipeline {
    agent any

    environment {
        // Full ECR repository URL
        ECR_REGISTRY = "${awsAccountId}.dkr.ecr.${awsRegion}.amazonaws.com"
        ECR_REPO = "${ECR_REGISTRY}/${appName}"
        // Set the image tag to the Jenkins Build Number
        IMAGE_TAG = "build-${BUILD_NUMBER}"
    }

    stages {
        stage('Login to AWS ECR') {
            steps {
                // Securely load credentials for ECR login
                withCredentials([
                    [$class: 'AmazonWebServicesCredentialsBinding', 
                     credentialsId: credentialsId, 
                     accessKeyVariable: 'AWS_ACCESS_KEY_ID', 
                     secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']
                ]) {
                    echo "Logging into AWS ECR..."
                    // Get ECR login password and pipe it to docker login command (Windows requires 'bat')
                    bat "aws ecr get-login-password --region ${awsRegion} | docker login --username AWS --password-stdin ${ECR_REGISTRY}"
                }
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image using the Dockerfile
                    // Tag the image with the full ECR path and the build number
                    docker.build("${ECR_REPO}:${IMAGE_TAG}").push()
                }
            }
        }
        
        stage('Push to ECR') {
            steps {
                echo "Pushing image to ECR: ${ECR_REPO}:${IMAGE_TAG}"
        
                // 1. Tag the image with the 'latest' tag using the bat step
                bat "docker tag ${ECR_REPO}:${IMAGE_TAG} ${ECR_REPO}:latest"
        
                echo "Tagged image as latest. Now pushing both tags..."
                
                // 2. Push the 'latest' tag
                bat "docker push ${ECR_REPO}:latest"
        
                echo "Deployment image ${ECR_REPO}:${IMAGE_TAG} pushed successfully!"
            }
        }
    }
}