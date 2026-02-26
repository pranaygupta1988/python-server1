pipeline{
    agent { label 'built-in' }
    stages{
        stage("Environment Variable"){
            steps{
                echo "Setting Environment variables"
                sh "export PATH=$PATH:/usr/bin"
            }
        }
        stage("SCM"){
            steps{
                echo "Pulling changes from Git repository"
                git branch: 'main', url: 'https://github.com/pranaygupta1988/python-server1.git'
            }
        }
        stage("Docker Login"){
            steps{
                echo "Logging to docker"
                withCredentials([string(credentialsId: 'DOCKER_HUB_TOKEN', variable: 'DOCKER_HUB_TOKEN')]) {
                 sh "echo $DOCKER_HUB_TOKEN | docker login -u pranaygupta1988 --password-stdin"
                } 
            }
        }
        stage("Build"){
            steps{
                echo "Building image"
                sh "docker image build -t pranaygupta1988/python-server1 ."
            }
        }
        stage("Pushing the image"){
            steps{
                echo "Pushing the image"
                sh "docker image push pranaygupta1988/python-server1"
            }
        }
        stage("Removing existing service"){
            steps{
                echo "Removing existing service"
                sh "docker service rm python-server1"
            }
        }

        stage("Creating New Service"){
            steps{
                echo "Creating new service"
                sh "docker service create --name python-server1 -p 5000:5000 --replicas 2 pranaygupta1988/python-server1"
            }
        }
    }
}
