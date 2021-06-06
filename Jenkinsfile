pipeline {
    agent none
    stages {
        stage('build') {
            agent { 
                docker { 
                    image 'python:3.7.2' 
                } 
            }
            steps {
                sh 'pip install flask'
            }
        }
        stage('test1') {
            agent { 
                docker { 
                    image 'python:3.7.2' 
                } 
            }
            steps {
                sh 'python prueba_unitaria1.py'
            }
        }
        stage('test2') {
            agent { 
                docker { 
                    image 'python:3.7.2' 
                } 
            }
            steps {
                sh 'python prueba_unitaria2.py'
            }
        }
    }
}