pipeline {
    agent any // Jenkins can run on any available agent

    stages {
        stage('Checkout') {
            steps {
                // Pull latest code from repo
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    . venv/bin/activate
                    pytest --html=report.html --self-contained-html
                '''
            }
        }
    }

    post {
        success {
            echo "All tests passed"
        }
        failure {
            echo "Some tests failed — check report in Jenkins"
        }
    }
}