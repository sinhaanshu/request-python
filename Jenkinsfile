pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                script {
                    git branch: 'main', url: 'https://github.com/sinhaanshu/request-python.git'
                }
            }
        }
        stage('Setup venv') {
            steps {
                sh '''
                python3 -m venv test_venv
                . test_venv/bin/activate
                pip3 install --upgrade pip
                pip3 install -r requirements.txt
                '''
            }
        }
        stage('Run requests.py') {
            steps {
                sh '''
                . test_venv/bin/activate
                python3 requests.py
                '''
            }
        }

    }

}
