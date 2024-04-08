pipeline{
    agent{
        label "any"
    }
    environment {  
        ECR_REPO = '767397888237.dkr.ecr.us-east-1.amazonaws.com/project_repo'   // ECR repo URI
        APP_IMAGE_NAME = 'flaskapp'                                             // name of App image
        DB_IMAGE_NAME = 'mysql'                                                // name of DB image
        APP_PATH = 'Docker/FlaskApp/Dockerfile'                               // path to App Dockerfile in GitHub repo
        DB_PATH = 'Docker/MySQL_DB/Dockerfile'                               // path to DB Dockerfile in GitHub repo
    }
    stages{
        stage("Checkout from Github"){
            steps{
                git branch: 'main', url: 'https://github.com/starboyhassan/Deploy-Python-App-on-EKS'
            }
        }

        stage('Push Images') {
            steps {
                withAWS(credentials: "${AWS_CREDENTIALS_ID}"){
                    sh "(aws ecr get-login-password --region us-east-1) | docker login -u AWS --password-stdin ${ECR_REPO}"
                    sh "docker push ${ECR_REPO}:${APP_IMAGE_NAME}-${BUILD_NUMBER}"
                    sh "docker push ${ECR_REPO}:${DB_IMAGE_NAME}-${BUILD_NUMBER}" 
                }
            }
        }

        stage('Remove Images') {
            steps {
                // delete images from jenkins server
                sh "docker rmi ${ECR_REPO}:${APP_IMAGE_NAME}-${BUILD_NUMBER}"
                sh "docker rmi ${ECR_REPO}:${DB_IMAGE_NAME}-${BUILD_NUMBER}"
            }
        }
    }

}