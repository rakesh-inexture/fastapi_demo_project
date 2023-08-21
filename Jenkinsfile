pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/rakesh-inexture/fastapi-practice.git']])
            }
        }

        stage('Test Sudo') {
            steps {
                sh "sudo echo 'Sudo test successful'"
            }
        }

        stage('Build') {
            steps {
                sh 'sudo apt update'
                sh 'sudo apt install -y python3-pip'
                sh "pip install -r requirements.txt"
                
            }
        }
        stage('Test') {
            steps {
                sh "python3 -m pytest"
            }
        }
    }
    
}
