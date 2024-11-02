pipeline {
    agent any

    options {
        timeout(time: 30, unit: 'MINUTES')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Set Up Environment') {
            steps {
                script {
                    // Create virtual environment and install dependencies
                    sh 'python3 -m venv venv'
                    sh '''
                        . venv/bin/activate
                        pip install pylint pytest
                    '''
                }
            }
        }

        stage('Code Quality Check') {
            steps {
                script {
                    // Run pylint on the specified Python files
                    sh '''
                        . venv/bin/activate
                        pylint addition.py subtraction.py
                    '''
                }
            }
        }

        stage('Unit Tests') {
            steps {
                script {
                    // Run pytest for unit tests
                    sh '''
                        . venv/bin/activate
                        pytest
                    '''
                }
            }
        }

        stage('Artifact Archiving') {
            steps {
                // Archive Python files as artifacts
                archiveArtifacts artifacts: '*.py', allowEmptyArchive: true
            }
        }
        stage('Deploy') {
            steps {
                script {
                    ansiblePlaybook(
                        playbook: 'setup.yml',
                        inventory: 'hosts', // Define your hosts file
                        credentialsId: 'shoppingkey' // Your SSH credentials
                    )
                }
            }
        }

    }   
}
