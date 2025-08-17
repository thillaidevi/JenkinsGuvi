
pipeline{
    agent any //jenkins can run on any available agent

    tools{
        python 'Python3'
    }

    stages{
        stage('Checkout'){

            steps{
                // it will pull latest code from repo
                checkout scm
            }
        }

        stage('Install Dependencies'){
            steps{
                sh'''
                python3 -m venv venv
                .venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''

            }

        }

        stage('Run Tests'){
            steps{
                    sh'''
                    .venv/bin.activate
                    pytest --html=report.html
                    '''

            }

        }


    }

    post{
        success{
            echo "All test passed"
        }
        failure{
            echo "some tests failed check report in jenkins"
        }
    }


}
