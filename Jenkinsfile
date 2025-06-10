pipeline {
    agent any

    environment {
        IMAGE_NAME = 'nopcommerce-app'
        IMAGE_TAG = 'latest'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/nopSolutions/nopCommerce.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t nopcommerce-app:latest .'
            }
        }

        stage('Stop Existing Containers') {
            steps {
                sh 'docker-compose down || true'
            }
        }

        stage('Start Containers') {
            steps {
                sh 'docker-compose up -d'
            }
        }
        stage('Expose to Internet') {
            steps {
                sh 'ngrok http 8080 &'
            }
        }
    }


    post {
        success {
            echo '✅ nopCommerce deployed successfully.'
        }
        failure {
            echo '❌ Deployment failed. Check logs for details.'
        }
    }
}
