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
                    source .venv/bin/activate
                    python -m unittest discover tests
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Explicitly tag with 'latest' and commit SHA for uniqueness
                    def commitId = sh(script: 'git rev-parse --short HEAD', returnStdout: true).trim()
                    def imageTag = "${DOCKER_IMAGE_NAME}:${commitId}"
                    docker.build(imageTag, '.')
                    
                    // Also tag as latest
                    sh "docker tag ${imageTag} ${DOCKER_IMAGE_NAME}:latest"
                }
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', DOCKER_HUB_CREDENTIALS_ID) {
                        // Push both latest and commit-tagged images
                        def commitId = sh(script: 'git rev-parse --short HEAD', returnStdout: true).trim()
                        docker.image("${DOCKER_IMAGE_NAME}:${commitId}").push()
                        docker.image("${DOCKER_IMAGE_NAME}:latest").push()
                    }
                }
            }
        }

        stage('Deploy with Ansible') {
            steps {
                sh 'ansible-playbook -i ansible/hosts.ini ansible/deploy.yml'
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
