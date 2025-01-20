pipeline {
    agent none  // Global agent definition
    environment {
        FRONTEND_REPO = 'https://github.com/Dharshini050/study-management-fronten'
        BACKEND_REPO = 'https://github.com/Dharshini050/Study'
    }

    stages {
        stage('Checkout Repositories') {
            agent { label 'docker' }  // Run this stage on a node with Docker installed
            steps {
                script {
                    // Clone the backend repository into the workspace
                    git url: BACKEND_REPO, branch: 'master'

                    // Clone the frontend repository into the 'frontend' folder within the workspace
                    dir('frontend') {
                        git url: FRONTEND_REPO, branch: 'master'
                    }
                }
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                script {
                    // Use the Python Docker image to run the setup in a container
                    docker.image('python:3.11').inside {
                        // Set up the virtual environment and install backend dependencies
                        sh '''
                        cd Study
                        python3 -m venv venv
                        source venv/bin/activate
                        pip install -r requirements.txt
                        '''
                    }
                }
            }
        }

        stage('Build Frontend') {
            steps {
                script {
                    // Use the Node Docker image to build the frontend
                    docker.image('node:18').inside {
                        // Install Node.js if needed
                        sh 'npm install -g @angular/cli'

                        // Install frontend dependencies
                        sh 'npm install'

                        // Build the frontend (Angular)
                        sh 'ng build --configuration production'
                    }
                }
            }
        }

        stage('Build Backend') {
            steps {
                script {
                    // Use the Python Docker image to build the backend
                    docker.image('python:3.11').inside {
                        // Use the virtual environment for building the backend
                        sh '''
                        cd Study
                        source venv/bin/activate
                        pip install -r requirements.txt
                        '''
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Use the Python Docker image to run tests for the backend
                    docker.image('python:3.11').inside {
                        // Run tests for the backend using the virtual environment
                        dir('Study') {
                            sh 'source venv/bin/activate && pytest'
                        }
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Add your deployment steps here (Docker, Kubernetes, etc.)
                    echo 'Deploying the app'
                    // For example, you could use Docker Compose or other deployment steps
                }
            }
        }
    }
}
