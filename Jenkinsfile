pipeline {
    agent any

 

    stages {
        stage('Clone GitHub repo') {
            steps {
                git(
                    url: 'https://github.com/rakesh-inexture/fastapi-practice.git,
                    branch: 'main',
                    credentialsId: 'jenkins.pem'
                )
            }
        }
    }
}
