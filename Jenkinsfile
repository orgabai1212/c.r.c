pipeline{
    agent any
    environment {
        GIT_LAST_TAG = sh(script: 'git describe --tags --abbrev=0', returnStdout: true).trim()
        // (GIT_MAJOR, GIT_MINOR, GIT_PATCH) = GIT_LAST_TAG.split('.')
    }

    stages{
        stage("checkout"){
            steps{
                checkout scm
            }
            
        }
        stage('Example') {
            steps {
                echo "Last Git tag is ${GIT_LAST_TAG}"
                // echo "Git major version is ${GIT_MAJOR}"
                // echo "Git minor version is ${GIT_MINOR}"
                // echo "Git patch version is ${GIT_PATCH}"
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
                    
                    sh "latest_tag=\$(git describe --tags --abbrev=0)"
                    def latest_tag = sh(returnStdout: true, script: """latest_tag=\$(git describe --tags --abbrev=0)""").trim()
                    echo "the value of latest tag is :${latest_tag}"
                    def majorOutput = sh(returnStdout: true, script: """major=\$(echo "$latest_tag" | cut -d '.' -f1)""")
                    def minorOutput = sh(returnStdout: true, script: """minor=\$(echo "$latest_tag" | cut -d '.' -f1)""")
                    def patchOutput = sh(returnStdout: true, script: """patch=\$(echo "$latest_tag" | cut -d '.' -f1)""")
                    major=majorOutput.trim()
                    minor=minorOutput.trim()
                    patch=patchOutput.trim()
                    
                    echo "${major}"
                    echo "${minor}"
                    echo "${patch}"
                    patch++
                    println "${patch}"
                    sh ''' patch=\$((patch + 1))'''
                    sh "echo \$patch"
                    def commandOutput = sh(returnStdout: true, script: 'echo "\$major.\$minor.\$patch"')
                    new_tag = commandOutput.trim()
                    sh "git tag ${new_tag}" 

                }
            }
        }
    }
    
}