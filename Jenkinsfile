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
                archiveArtifacts artifacts: '*.py, hosts', allowEmptyArchive: true
            }
        }

        stage('Debug Hosts File') {
            steps {
                script {
                    sh '''
                        echo "Contents of hosts file:"
                        cat hosts
                    '''
                }
            }
        }

        stage('Deploy with Ansible') {
            steps {
                script {
                    sh '''
                        ansible-playbook -i hosts main.yml --private-key=shoppingkey.pem --ssh-extra-args='-o StrictHostKeyChecking=no'
 
                    '''
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            sh '''
                . venv/bin/activate
                deactivate
            '''
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
