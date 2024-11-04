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

        stage('Deploy with Ansible') {
            steps {
                script {
                    sh '''
                        ansible-playbook -i /home/ubuntu/hosts /home/ubuntu/main.yml --key-file /home/ubuntu/shoppingkey.pem
                    '''
                }
            }
        }
    }
}
