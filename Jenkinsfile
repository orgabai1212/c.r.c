pipeline{
    agent anny

    stages{
        stage("checkout"){
            steps{
               checkout scm
            }
            post{
                
                success{
                    echo "good"
                }
                failure{
                    echo "bad"
                }
            }
        }
    }
    
}