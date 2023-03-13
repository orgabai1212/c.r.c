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
                    
                    // define latest tag
        sh "latest_tag=\$(git describe --tags --abbrev=0)"
        def latest_tag = sh(script: """latest_tag=\$(git describe --tags --abbrev=0)""", returnStdout: true).trim()
        echo "the value of latest tag is : ${latest_tag}"

        // extract major, minor, and patch versions
        def majorOutput = sh(returnStdout: true, script: """major=\$(echo "$latest_tag" | cut -d '.' -f1)""")
        def minorOutput = sh(returnStdout: true, script: """minor=\$(echo "$latest_tag" | cut -d '.' -f2)""")
        def patchOutput = sh(returnStdout: true, script: """patch=\$(echo "$latest_tag" | cut -d '.' -f3)""")
        env.major = majorOutput.trim()
        env.minor = minorOutput.trim()
        env.patch = patchOutput.trim()

        echo "major: ${env.major}"
        echo "minor: ${env.minor}"
        echo "patch: ${env.patch}"

        // increment patch version
        env.patch = env.patch.toInteger() + 1
        sh "echo \$patch"

        // create new tag
        def commandOutput = sh(returnStdout: true, script: 'echo "${env.major}.${env.minor}.${env.patch}"')
        env.new_tag = commandOutput.trim()
        sh "git tag ${env.new_tag}"
    
                }
            }
        }
    }
    
}