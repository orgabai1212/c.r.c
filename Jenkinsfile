pipeline{
    agent any
    environment {
        sh (script:'git pull origin')
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
                script{
                echo "Last Git tag is ${GIT_LAST_TAG}"
                def versionArray = sh(script: "echo ${GIT_LAST_TAG} | tr '.' '\\n'", returnStdout: true).trim().split('\n')
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
                sh "git push origin  $newVersion"
                echo"test blala"
                }
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
                    def latest_tag = sh( script: """git describe --tags --abbrev=0""",returnStdout: true).trim()
                    echo "the value of latest tag is : ${latest_tag}"
                    def majorOutput = sh(returnStdout: true, script: """echo "$latest_tag" | cut -d '.' -f1)""")
                    echo "${majorOutput}"
                    def minorOutput = sh(returnStdout: true, script: """minor=\$(echo "$latest_tag" | cut -d '.' -f2)""")
                    def patchOutput = sh(returnStdout: true, script: """patch=\$(echo "$latest_tag" | cut -d '.' -f3)""")
                    major=majorOutput.trim()
                    minor=minorOutput.trim()
                    patch=patchOutput.trim()
                    echo "the major is ${major}"
                    echo "the minor is ${minor}"
                    echo "the patch ${patch}"
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