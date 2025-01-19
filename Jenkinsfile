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
                    // Install Node.js 18.x (since Angular requires Node.js >=18)
                    sh 'curl -sL https://deb.nodesource.com/setup_18.x | bash -'
                    sh 'apt-get install -y nodejs'

                    // Install Angular CLI globally
                    sh 'npm install -g @angular/cli'

                    // Install frontend dependencies and build the frontend
                    dir('frontend') {
                        sh 'npm install'
                        sh 'ng build --prod'  // Build the frontend using Angular CLI
                    }
                }
            }
        }

        stage('Build Backend') {
            steps {
                script {
                    dir('study-management') {
                        // Install Python dependencies for the backend
                        sh 'pip install -r requirements.txt'
                    }
                }
            }
        }
        
        stage('Run Tests') {
            steps {
                script {
                    dir('study-management') {
                        // Run tests using pytest
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
                    // Add your deployment steps here, e.g., using Docker, Kubernetes, etc.
                }
            }
        }
    }
}
