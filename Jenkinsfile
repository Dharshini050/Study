pipeline {
    agent any  // Run on any available agent (ensure this agent has Docker installed)

    environment {
        FRONTEND_REPO = 'https://github.com/Dharshini050/study-management-fronten'  // Frontend repo URL
        BACKEND_REPO = 'https://github.com/Dharshini050/Study'  // Backend repo URL
    }

    stages {
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

        stage('Install Backend Dependencies') {
            steps {
                script {
                    sh 'ls -al'

                    // Set up the backend's virtual environment and install dependencies
                    sh '''
                    cd study-management
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Build Frontend') {
            steps {
                script {
                    // Navigate to the frontend directory and build it
                    dir('frontend') {
                        // Install Node.js and Angular CLI
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
                    // Build the backend (ensure all dependencies are installed)
                    sh '''
                    cd study-management
                    source venv/bin/activate
                    pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run tests for the backend using the virtual environment
                    dir('study-management') {
                        sh 'source venv/bin/activate && pytest'
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Example: Deploy the Dockerized application
                    echo 'Deploying the app'

                    // Example: Deploy with Docker (adjust accordingly)
                    // docker build -t study-management .
                    // docker run -d -p 8000:8000 study-management
                }
            }
        }
    }
}
