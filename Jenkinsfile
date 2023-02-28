pipeline{
    agent any
    environment {
    
        new_tag = ''
    }

    stages{
        stage("checkout"){
            steps{
                checkout scm
            }
            
        }
        stage("version"){
            when{
               expression{ 
                return GIT_BRANCH.contains("relese")
               }
            }
            steps{
                script{
                    sh "latest_tag=$(git describe --tags --abbrev=0)"
                    sh "major=$(echo $latest_tag | awk -F. '{print $1}')"
                    sh "minor=$(echo $latest_tag | awk -F. '{print $2}')"
                    sh "patch=$(echo $latest_tag | awk -F. '{print $3}')"
                    sh "((patch++))"
                    def commandOutput = sh(returnStdout: true, script: 'echo "hello world"')
                    env.new_tag = commandOutput.trim()
                    sh "git tag ${new_tag}" 

                }
            }
        }
    }
    
}