pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/<your-username>/quote-of-the-day.git'
            }
        }
        stage('Install deps') {
            steps {
                sh 'python -m pip install --upgrade pip && pip install -r requirements.txt'
            }
        }
        stage('Static check') {
            steps {
                sh 'python -m py_compile app.py'
            }
        }
        stage('Docker build') {
            steps {
                sh 'docker build -t quote-app:${BUILD_NUMBER} .'
            }
        }
        stage('Docker run') {
            steps {
                sh '''
                    docker rm -f quote_container || true
                    docker run -d -p 5000:5000 --name quote_container quote-app:${BUILD_NUMBER}
                '''
            }
        }
    }
    post {
        success { echo "Pipeline succeeded" }
        failure { echo "Pipeline failed" }
    }
}
