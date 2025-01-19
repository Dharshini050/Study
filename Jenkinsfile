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
                    apt-get install -y python3 python3-pip python3.11-venv
                    '''

                    // Check if the virtual environment exists and create it if it doesn't
                    sh '''
                    if [ ! -d "me" ]; then
                        python3 -m venv me
                        echo "Virtual environment 'me' created successfully."
                    else
                        echo "Virtual environment 'me' already exists."
                    fi
                    '''

                    // Activate the virtual environment from the correct path (Scripts/activate)
                    sh 'bash -c "source me/Scripts/activate"'

                    // Install required Python dependencies
                    sh 'pip install --upgrade pip'
                    sh 'pip install -r requirements.txt'
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
                    // Add your deployment steps here (Docker, Kubernetes, etc.)
                }
            }
        }
    }
}
