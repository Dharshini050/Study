pipeline {
    agent none  // No agent defined at the top level, define in individual stages
    environment {
        FRONTEND_REPO = 'https://github.com/Dharshini050/study-management-fronten'  // Frontend repo URL
        BACKEND_REPO = 'https://github.com/Dharshini050/Study'  // Backend repo URL
    }

    stages {
        stage('Checkout Repositories') {
            agent { docker { image 'python:3.11' } }  // Define docker agent for this stage
            steps {
                script {
                    // Clone the backend repository into the 'study-management' folder
                    git url: BACKEND_REPO, branch: 'master'

                    // Clone the frontend repository into the 'frontend' folder
                    dir('frontend') {
                        git url: FRONTEND_REPO, branch: 'master'
                    }
                }
            }
        }

        stage('Setup Virtual Environment') {
            agent { docker { image 'python:3.11' } }  // Use docker image for this stage
            steps {
                script {
                    // Set up the virtual environment and install backend dependencies
                    sh '''
                    cd study_management
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Build Frontend') {
            agent { docker { image 'node:18' } }  // Use node Docker image for frontend build
            steps {
                script {
                    // Install Node.js if needed
                    sh 'npm install -g @angular/cli'

                    // Install frontend dependencies
                    sh 'npm install'

                    // Build the frontend
                    sh 'ng build --configuration production'
                }
            }
        }

        stage('Build Backend') {
            agent { docker { image 'python:3.11' } }  // Use docker image for this stage
            steps {
                script {
                    // Use the virtual environment for building the backend
                    sh '''
                    cd study_management
                    source venv/bin/activate
                    pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Tests') {
            agent { docker { image 'python:3.11' } }  // Use docker image for this stage
            steps {
                script {
                    // Run tests for the backend using the virtual environment
                    dir('study_management') {
                        sh 'source venv/bin/activate && pytest'
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Add your deployment steps here (Docker, Kubernetes, etc.)
                    echo 'Deploying the app'
                }
            }
        }
    }
}
