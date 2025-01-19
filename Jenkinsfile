pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Dharshini050/Study.git'
            }
        }
        stage('Build Frontend') {
    steps {
        script {
            // Install Node.js and npm if not available
            sh 'curl -sL https://deb.nodesource.com/setup_16.x | bash -'
            sh 'apt-get install -y nodejs'

            // Now install frontend dependencies
            dir('frontend') {
                sh 'npm install'
                sh 'ng build --prod'
                    }
                }
            }
        }

        stage('Build Backend') {
            steps {
                script {
                    dir('study-management') {
                        sh 'pip install -r requirements.txt'
                    }
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    dir('study-management') {
                        sh 'pytest'
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    // Example: Deploy your Dockerized application
                    echo 'Deploying the app'
                    // Add deployment steps here
                }
            }
        }
    }
}
