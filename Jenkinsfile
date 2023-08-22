pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/rakesh-inexture/fastapi-practice.git']])
            }
        }

        stage('Build') {
            steps {
                sh "/usr/bin/python3.10 -m pip install -r requirements.txt"
            }
        }

        stage('Test') {
            steps {
                sh "/usr/bin/python3.10 -m pytest"
            }
        }
    } 
}
