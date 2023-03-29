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
        stage('version') {
            steps {
                script{
                    withCredentials([usernamePassword(credentialsId: 'crc-repo',
                     usernameVariable: 'username',
                     passwordVariable: 'password')]){
                     sh("git pull https://$username:$password@github.com/orgabai1212/c.r.c.git")
                    
                    }


                    sh "tag=\$(git describe --tags --abbrev=0 2> /dev/null)"
                    def GIT_LAST_TAG = sh(script: 'echo \$tag', returnStdout: true).trim()
                    echo "tag is $GIT_LAST_TAG"
                    if (GIT_LAST_TAG==""){
                     echo "no tags"
                    }
                    else{
                     echo "Last Git tag is $GIT_LAST_TAG"
                     def versionArray = sh(script: "echo $GIT_LAST_TAG | tr '.' '\\n'", returnStdout: true).trim().split('\n')
                     def major = versionArray[0]
                     def minor = versionArray[1]
                     def patch = versionArray[2]
                     patch ++
                     def newVersion=major+"."+minor+"."+patch
                     echo "the major is $major"
                     echo "the minor is $minor"
                     echo "the patch is $patch"
                     echo "the new version is $newVersion"
                     sh "git tag $newVersion"
                     withCredentials([usernamePassword(credentialsId: 'crc-repo',
                      usernameVariable: 'username',
                      passwordVariable: 'password')]){
                      sh "git push https://$username:$password@github.com/orgabai1212/c.r.c.git $newVersion"
                    
                      }
                    } 
                
                }
            }
        }
        
    }
    
}