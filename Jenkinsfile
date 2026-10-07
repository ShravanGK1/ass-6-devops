pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Pulling latest source code from GitHub repository...'
                checkout scm
            }
        }

        stage('Verify Files') {
            steps {
                echo 'Listing repository contents in Jenkins workspace...'
                // Works on both Linux and Windows Jenkins nodes
                script {
                    if (isUnix()) {
                        sh 'ls -la'
                    } else {
                        bat 'dir'
                    }
                }
            }
        }

        stage('Test') {
            steps {
                echo 'Running automated unit tests...'
                script {
                    if (isUnix()) {
                        sh 'python3 -m unittest discover -s . -p "test_*.py"'
                    } else {
                        bat 'python -m unittest discover -s . -p "test_*.py"'
                    }
                }
            }
        }

        stage('Build & Execute') {
            steps {
                echo 'Executing application build...'
                script {
                    if (isUnix()) {
                        sh 'python3 app.py'
                    } else {
                        bat 'python app.py'
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution finished.'
        }
        success {
            echo 'Build, Test, and Checkout completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the console output for error details.'
        }
    }
}
