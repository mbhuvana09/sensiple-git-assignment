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
        stage('Code Quality Check') {
            steps {
                script {
                    sh 'pip install pylint'
                    sh 'pylint addition.py subtraction.py'
                }
            }
        }
        stage('Unit Tests') {
            steps {
                script {
                    sh 'pip install pytest'
                    sh 'pytest'
                }
            }
        }
        stage('Artifact Archiving') {
            steps {
                archiveArtifacts artifacts: '*.py', allowEmptyArchive: true
            }
        }
    }
 
}
