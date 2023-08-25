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
                sh "pip install -r requirements.txt"
            }
        }
        stage('Test') {
            steps {
                sh "python3 -m pytest"
            }
        }
        // stage('Update and Install Dependencies') {
        //     steps {
        //         sh "cd fastapi-practice/"
        //         sh "git pull"
        //         sh "pip install -r requirements.txt"
        //     }
        // }
    }
}
