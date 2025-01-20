pipeline {
    agent any

    environment {
        FRONTEND_REPO = 'https://github.com/Dharshini050/study-management-fronten'  // Frontend repo URL
        BACKEND_REPO = 'https://github.com/Dharshini050/Study'  // Backend repo URL
    }

    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    // Install system dependencies (Python, Node.js, etc.)
                    sh '''
                    apt-get update
                    apt-get install -y python3 python3-pip python3.11-venv python3-dev curl
                    '''
                }
            }
        }

        stage('Clone Repositories') {
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
            steps {
                script {
                    // Create the virtual environment if it doesn't exist and install backend dependencies
                    sh '''
                    cd study-management
                    python3 -m venv venv
                    bash -c "source venv/bin/activate && pip install --upgrade pip"
                    bash -c "source venv/bin/activate && pip install -r requirements.txt"
                    '''
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
                    // Use the virtual environment for building the backend
                    sh '''
                    cd study-management
                    bash -c "source venv/bin/activate && pip install -r requirements.txt"
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run tests for the backend using the virtual environment
                    dir('study-management') {
                        sh 'bash -c "source venv/bin/activate && pytest"'
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Add your deployment steps here (Docker, Kubernetes, etc.)
                    echo 'Deploying the app'

                    // Example: Deploy your Dockerized application (adjust accordingly)
                    // docker build -t study-management .
                    // docker run -d -p 8000:8000 study-management
                }
            }
        }
    }
}
