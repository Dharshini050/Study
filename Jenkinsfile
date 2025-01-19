pipeline {
    agent any

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
                    // Install Python and pip if not already installed
                    sh '''
                    apt-get update
                    apt-get install -y python3 python3-pip
                    '''

                    // Install virtual environment and activate it
                    dir('study-management') {
                        sh '''
                        # Check if 'me' virtual environment exists, if not create it
                        if [ ! -d "me" ]; then
                            python3 -m venv me
                        fi

                        # Activate the virtual environment
                        . me/bin/activate

                        # Install required Python dependencies
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
                    // Run tests in the backend directory
                    dir('study-management') {
                        sh '''
                        . me/bin/activate
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
                    // Add your deployment steps here (Docker, Kubernetes, etc.)
                }
            }
        }
    }
}
