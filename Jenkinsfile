pipeline{
    agent any

    stages{
        stage("checkout"){
            steps{
                deleteDir{}
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
                    sh"git log -1 --format=%H"
                }
            }
        }
    }
    
}