pipeline{
    agent any
    // environment {
    //     branch = env.GIT_BRANCH
    //     // GIT_LAST_TAG = sh(script: 'git pull origin && git describe --tags --abbrev=0', returnStdout: true).trim()
    //     // (GIT_MAJOR, GIT_MINOR, GIT_PATCH) = GIT_LAST_TAG.split('.')
    // }

    stages{
        stage("checkout"){
            steps{
                checkout scm
            }

        }

        stage("test build "){
            steps{
                withCredentials([usernamePassword(credentialsId: 'crc-repo',
                 usernameVariable: 'username',
                 passwordVariable: 'password')]){
                 sh("git pull https://$username:$password@github.com/orgabai1212/c.r.c.git")
                }
                sh"docker-compose down"
                sh"docker-compose build --no-cache"
                sh"docker-compose up"
                

                


            }




        }
        stage('version') {
            steps {
                script{
                    withCredentials([usernamePassword(credentialsId: 'crc-repo',
                     usernameVariable: 'username',
                     passwordVariable: 'password')]){
                     sh("git pull https://$username:$password@github.com/orgabai1212/c.r.c.git")
                    }
                    def version = sh(script: './check-tag.sh', returnStdout: true).trim()
                    echo "the new version is $version"
                    sh "git tag $version"
                    withCredentials([usernamePassword(credentialsId: 'crc-repo',
                     usernameVariable: 'username',
                     passwordVariable: 'password')]){
                     sh "git push https://$username:$password@github.com/orgabai1212/c.r.c.git $version"
                    
                    }
                    
                
                }
            }
        }
        
    }
    
}