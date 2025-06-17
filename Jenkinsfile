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
                sh 'docker-compose up -d --network host'
            }
        }
        stage('Expose to Internet') {
            environment {
                        NGROK_AUTH_TOKEN = credentials('NGROK_AUTH_TOKEN')
            }    
            steps {
                sh 'ngrok config add-authtoken $NGROK_AUTH_TOKEN'
                sh 'ngrok http 80 &'
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
