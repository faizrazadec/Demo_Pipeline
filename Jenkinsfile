pipeline {
    agent any

    environment {
        PYTHON = '/usr/bin/python3'
        PIP = '/usr/bin/pip3'
        VENV = 'venv'
    }

    stages {
        stage('Build') {
            steps {
                // Create virtual environment
                sh 'python -m venv ${VENV}'

                // Activate virtual environment
                sh 'source ${VENV}/bin/activate'

                // Install dependencies
                sh 'pip install -r requirements.txt'

                // Build project (e.g., compile, package)
                sh 'python setup.py build'
            }
        }

        stage('Test') {
            steps {
                // Run unit tests
                sh 'python -m unittest discover -s tests'

                // Generate test report
                junit 'reports.xml'
            }
        }

        stage('Deploy') {
            steps {
                // Deploy to production environment
                sh 'python deploy.py'

                // Notify team about deployment
                mail to: 'team@example.com',
                     subject: 'Deployment Successful',
                     body: 'Python project deployed successfully.'
            }
        }
    }

    post {
        always {
            // Cleanup virtual environment
            sh 'deactivate'
            sh 'rm -rf ${VENV}'

            // Archive artifacts
            archiveArtifacts artifacts: '**/reports.xml', fingerprint: true
        }

        failure {
            // Notify team about failure
            mail to: 'team@example.com',
                 subject: 'Deployment Failed',
                 body: 'Python project deployment failed.'

            // Clean workspace
            cleanWs()
        }
    }
}