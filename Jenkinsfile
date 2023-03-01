pipeline{
    agent any
    environment {
        new_tag = ""
        major=""
        minor=""
        patch=""
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
                    
                    sh "latest_tag=\$(git describe --tags --abbrev=0)"
                    def majorOutput = sh(returnStdout: true, script: "major=$(echo "$latest_tag" | cut -d '.' -f1)")
                    def minorOutput = sh(returnStdout: true, script: "minor=$(echo "$latest_tag" | cut -d '.' -f1)")
                    def patchOutput = sh(returnStdout: true, script: "patch=$(echo "$latest_tag" | cut -d '.' -f1))")
                    major=majorOutput.trim()
                    minor=minorOutput.trim()
                    patch=patchOutput.trim()
                    
                    sh "echo ${major}"
                    sh "echo ${minor}"
                    sh "echo ${patch}"
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