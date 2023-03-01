pipeline{
    agent any
    environment {
        new_tag = ""
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
                    sh "major=\$(echo \$latest_tag | awk -F\\. '{print \$1}')"
                    sh "echo \$major"
                    sh "minor=\$(echo \$latest_tag | awk -F\\. '{print \$2}')"
                    sh "echo \$minor"

                    sh "patch=\$(echo \$latest_tag | awk -F\\. '{print \$3}')"
                    sh "echo \$patch"
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