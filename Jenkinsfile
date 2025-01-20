// pipeline {
//     agent any

//     environment {
//         FRONTEND_REPO = 'https://github.com/Dharshini050/study-management-fronten'  // Replace with your frontend repo URL
//         BACKEND_REPO = 'https://github.com/Dharshini050/Study'  // Replace with your backend repo URL
//     }

//     stages {
//         stage('Clone Repositories') {
//             steps {
//                 script {
//                     // Clone the backend repository
//                     git url: BACKEND_REPO, branch: 'master'

//                     // Clone the frontend repository
//                     dir('frontend') {
//                         git url: FRONTEND_REPO, branch: 'master'
//                     }
//                 }
//             }
//         }

//         stage('Build Frontend') {
//             steps {
//                 script {
//                     // Navigate to the frontend directory and build
//                     dir('frontend') {
//                         // Install Node.js if needed
//                         sh 'curl -sL https://deb.nodesource.com/setup_18.x | bash -'
//                         sh 'apt-get install -y nodejs'

//                         // Install Angular CLI globally
//                         sh 'npm install -g @angular/cli'

//                         // Install frontend dependencies
//                         sh 'npm install'

//                         // Build the frontend
//                         sh 'ng build --configuration production'
//                     }
//                 }
//             }
//         }

//         stage('Build Backend') {
//             steps {
//                 script {
//                     // Install Python and pip if not already installed
//                     sh '''
//                     apt-get update
//                     apt-get install -y python3 python3-pip
//                     '''
//                     // Build the backend
//                     dir('study-management') {
//                         sh 'pip install -r requirements.txt'
//                     }
//                 }
//             }
//         }

//         stage('Run Tests') {
//             steps {
//                 script {
//                     dir('study-management') {
//                         sh 'pytest'
//                     }
//                 }
//             }
//         }

//         stage('Deploy') {
//             steps {
//                 script {
//                     // Example: Deploy your Dockerized application
//                     echo 'Deploying the app'
//                     // Add deployment steps here
//                 }
//             }
//         }
//     }
// }


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
                    // Install Python dependencies and virtual environment tools
                    sh '''
                    apt-get update
                    apt-get install -y python3 python3-pip python3.11-venv python3-dev
                    '''
                }
            }
        }

<<<<<<< HEAD

=======
>>>>>>> 400a68ee7bf21f50f135dd1f15c454917b8b4c3b
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
                    // Create the virtual environment if it doesn't exist
                    sh '''
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
                    // Use the virtual environment from the 'Setup Virtual Environment' stage
                    sh '''
<<<<<<< HEAD
                    apt-get update
                    apt-get install -y python3 python3-pip python3.11-venv
                    '''
        
                    // Upgrade pip globally
                    sh 'pip3 install --upgrade pip'
        
                    // Install dependencies globally from requirements.txt
                    sh 'pip3 install -r requirements.txt'
        
                    // Verify that the required packages are installed
                    sh 'pip3 freeze'
=======
                    bash -c "source venv/bin/activate && pip install -r requirements.txt"
                    '''
        
                    // Verify that the required packages are installed in the virtual environment
                    sh 'bash -c "source venv/bin/activate && pip freeze"'
>>>>>>> 400a68ee7bf21f50f135dd1f15c454917b8b4c3b
                }
            }
        }


        stage('Run Tests') {
            steps {
                script {
                    dir('study-management') {
                        // Use the virtual environment for tests
                        sh 'bash -c "source venv/bin/activate && pytest"'
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
