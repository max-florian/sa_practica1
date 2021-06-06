pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'pip install flask'
            }
        }
        stage('test1') {
            steps {
                sh 'python prueba_unitaria1.py'
            }
        }
        stage('test2') {
            steps {
                sh 'python prueba_unitaria2.py'
            }
        }
    }
}