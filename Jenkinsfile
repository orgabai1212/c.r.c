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
         
        stage('Check for Git tag') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'crc-repo',
                        usernameVariable: 'username',
                        passwordVariable: 'password')]){
                        sh("git pull https://$username:$password@github.com/orgabai1212/c.r.c.git")
                    
                        }  
                        def tag = sh(script: 'git describe --tags --abbrev=0 2> /dev/null', returnStdout: true).trim()
                        if (tag == "") {
                         echo "No Git tag found, setting version to 0.0.1"
                         def major = 0
                         def minor = 0
                         def patch = 1
                        } 
                        else {
                         echo "Git tag found: $tag"
                         def versionArray = sh(script: "echo $tag | tr '.' '\\n'", returnStdout: true).trim().split('\n')
                         def major = versionArray[0]
                         def minor = versionArray[1]
                         def patch = versionArray[2]
                         patch++
                         def newVersion = major + "." + minor + "." + patch
                         echo "the major is $major"
                         echo "the minor is $minor"
                         echo "the patch is $patch"
                         echo "the new version is $newVersion"
                    }
                }
            }
        }
        stage('Push new Git tag') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'crc-repo', usernameVariable: 'username', passwordVariable: 'password')]) {
                        sh "git tag $newVersion"
                        sh "git push https://$username:$password@github.com/orgabai1212/c.r.c.git $newVersion"
                    }
                }
            }
        }
        
    
    }
}



