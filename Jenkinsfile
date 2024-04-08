pipeline{
    agent{
        label "any"
    }
    stages{
        stage("Checkout from Github"){
            steps{
                git branch: 'main', url: 'https://github.com/starboyhassan/Deploy-Python-App-on-EKS'
            }
        }
    }

}