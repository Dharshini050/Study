pipeline {
    agent any

    environment {
        FRONTEND_REPO = 'https://github.com/Dharshini050/study-management-fronten'  // Replace with your frontend repo URL
        BACKEND_REPO = 'https://github.com/Dharshini050/Study'  // Replace with your backend repo URL
    }

    stages {
        stage('Clone Repositories') {
            steps {
                script {
                    // Clone the backend repository
                    git url: BACKEND_REPO, branch: 'master'

                    // Clone the frontend repository
                    dir('frontend') {
                        git url: FRONTEND_REPO, branch: 'master'
                    }
                }
            }
        }

        stage('Build Frontend') {
            steps {
                script {
                    // Navigate to the frontend directory and build
                    dir('frontend') {
                        // Install Node.js if needed
                        sh 'curl -sL https://deb.nodesource.com/setup_18.x | bash -'
                        sh 'apt-get install -y nodejs'

                        // Install Angular CLI globally
                        sh 'npm install -g @angular/cli'

                        // Install frontend dependencies
                        sh 'npm install'

                        // Build the frontend
                        sh 'ng build --configuration production'
                    }
                }
            }
        }

        stage('Build Backend') {
            steps {
                script {
                    dir('study-management') {
                    // Install Python and pip if not already installed
                    sh '''
                    source me/bin/activate
                    apt-get update
                    apt-get install -y python3 python3-pip
            
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    '''
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    dir('study-management') {
                        //Activate the virtual environment on Windows
                        sh'''
                        source me/bin/activate
                        pytest
                        '''
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
