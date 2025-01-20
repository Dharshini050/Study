pipeline {
    agent any
    environment {
        FRONTEND_REPO = 'https://github.com/Dharshini050/study-management-fronten'
        BACKEND_REPO = 'https://github.com/Dharshini050/Study'
        FRONTEND_DIR = 'frontend'
        BACKEND_DIR = 'backend'
    }
    stages {
        stage('Checkout Repositories') {
            steps {
                script {
                    // Checkout frontend and backend repositories using GitHub credentials
                    withCredentials([usernamePassword(credentialsId: 'github-credentials', usernameVariable: 'GITHUB_USER', passwordVariable: 'GITHUB_TOKEN')]) {
                        // Checkout frontend and backend repos
                        git credentialsId: 'github-credentials', url: FRONTEND_REPO
                        git credentialsId: 'github-credentials', url: BACKEND_REPO
                    }
                }
            }
        }
        stage('Setup Backend Virtual Environment') {
            steps {
                script {
                    // Setup Python virtual environment for the backend
                    sh 'python3 -m venv venv'
                    sh '. venv/bin/activate'
                    sh 'pip install -r ${BACKEND_DIR}/requirements.txt'  // Install backend dependencies
                }
            }
        }
        stage('Build Frontend') {
            steps {
                script {
                    // Install frontend dependencies and build the frontend (Angular)
                    sh 'cd ${FRONTEND_DIR} && npm install'
                    sh 'cd ${FRONTEND_DIR} && ng build --prod'  // Build the frontend for production
                }
            }
        }
        stage('Run Backend Tests') {
            steps {
                script {
                    // Run backend tests (using pytest or your test framework of choice)
                    sh 'cd ${BACKEND_DIR} && pytest tests'  // Adjust this if your test location is different
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    // Example deployment step using Docker (you can customize as per your deployment method)
                    echo "Deploying Application..."

                    // Assuming you are using Docker Compose
                    sh 'docker-compose -f ${BACKEND_DIR}/docker-compose.yml up -d'  // Deploy backend with Docker
                    sh 'docker-compose -f ${FRONTEND_DIR}/docker-compose.yml up -d'  // Deploy frontend with Docker (if needed)
                }
            }
        }
    }
    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline execution failed!'
        }
    }
}
