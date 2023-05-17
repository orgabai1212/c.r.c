pipeline{
    agent any
    environment {
        test_ip = "3.120.247.120"
        app_port = "5000"
        
        deploy_ip ="15.237.112.154"
        
       
    }

    stages{
        stage("checkout"){
            steps{
                checkout scm
            }

        }

        stage("test build "){
            steps{
                withCredentials([usernamePassword(credentialsId:'crc-repo',
                 usernameVariable: 'username',
                 passwordVariable: 'password')]){
                 sh("git pull https://$username:$password@github.com/orgabai1212/c.r.c.git")
                }
                
                sh"docker-compose down -v "
                sh"docker-compose build --no-cache"
                sh"docker-compose up -d"
                sh"curl -v ${test_ip}:${app_port}"
                
                
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
        // aoucxhasjcpaoj
        
    }
    
}


// ===================================================================
// pipeline{
//     agent any
//     environment {
//         test_ip = "3.120.247.120"
//         app_port = "5000"
        
//         deploy_ip ="15.237.112.154"
        
       
//     }

//     stages{
//         stage("checkout"){
//             steps{
//                 checkout scm
//             }

//         }

//         stage("update git changes"){
//             steps{

//                 withCredentials([usernamePassword(credentialsId: 'crc-repo',
//                  usernameVariable: 'username',
//                  passwordVariable: 'password')]){
//                  sh("git config --global user.email 'orgabai1212@gmail.com'")
//                  sh("git config --global user.name 'or gabay'")
//                  sh("git pull https://$username:$password@github.com/orgabai1212/c.r.c.git")
//                 }

//             }


//         }

//         stage('version') {
//             steps {
//                 script{
//                     withCredentials([usernamePassword(credentialsId: 'crc-repo',
//                      usernameVariable: 'username',
//                      passwordVariable: 'password')]){
//                      sh("git pull https://$username:$password@github.com/orgabai1212/c.r.c.git")
//                     }
//                     def version = sh(script: './check-tag.sh', returnStdout: true).trim()
//                     echo "the new version is $version"
//                     // sh "git tag $version"
//                     withCredentials([usernamePassword(credentialsId: 'crc-repo',
//                      usernameVariable: 'username',
//                      passwordVariable: 'password')]){
//                      sh "git push https://$username:$password@github.com/orgabai1212/c.r.c.git $version"
                    
//                     }
                    
                
//                 }
//             }
//         }
//         stage('test_build') {
//             steps{
//                 script{

//                  sh"cd var/jenkins_home/workspace/crc_main"
//                  sh"docker-compose down -v "
//                  sleep(time: 20, unit: 'SECONDS')
//                  sh"docker-compose build --no-cache"
//                  sh"docker-compose up -d"
//                  sh"curl -v ${test_ip}:${app_port}"
//                 }
//             }
//         }
        
//     }
    
// }