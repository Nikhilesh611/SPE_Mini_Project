pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = 'nikhilesh611/scientific_calculator'
        DOCKER_HUB_CREDENTIALS_ID = 'dockerhub-creds'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Nikhilesh611/SPE_Mini_Project.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                // Use a shell to set up a virtual environment and install dependencies
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh '''
                    . .venv/bin/activate
                    python -m unittest discover tests
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image from Dockerfile
                    def customImage = docker.build(DOCKER_IMAGE_NAME)
                }
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', DOCKER_HUB_CREDENTIALS_ID) {
                        docker.image(DOCKER_IMAGE_NAME).push('latest')
                    }
                }
            }
        }

        stage('Deploy with Ansible') {
            steps {
                // Pull the latest image and deploy using your Ansible playbook
                sh 'ansible-playbook -i ~/hosts.ini ~/deploy.yml'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check console output for errors.'
        }
    }
}
