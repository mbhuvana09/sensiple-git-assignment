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
                    sh '''
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install pylint pytest
                    '''
                }
            }
        }

        stage('Code Quality Check') {
            steps {
                script {
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
                    sh '''
                        . venv/bin/activate
                        pytest
                    '''
                }
            }
        }

        stage('Artifact Archiving') {
            steps {
                archiveArtifacts artifacts: '*.py', allowEmptyArchive: true
            }
        }

        stage('Debug') {
            steps {
                script {
                    // This stage is for debugging purposes
                    sh '''
                        pwd
                        ls -l
                    '''
                }
            }
        }

        stage('Check Hosts File') {
            steps {
                script {
                    // Verify the hosts file is present in the workspace
                    sh '''
                        echo "Checking for hosts file:"
                        ls -l hosts
                    '''
                }
            }
        }

        stage('Deploy with Ansible') {
            steps {
                script {
                    // Execute the Ansible playbook
                    sh '''
                        ansible-playbook -i hosts main.yml --key-file shoppingkey.pem
                    '''
                }
            }
        }
    }

    post {
        always {
            // Always run this block to ensure we have some logging
            echo 'Pipeline completed.'
        }
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Deployment failed.'
        }
    }
}
