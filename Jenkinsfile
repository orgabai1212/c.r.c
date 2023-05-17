pipeline{
    agent any
    environment {
        test_ip = "3.123.37.155"
        app_port = "5000"
        deploy_ip ="18.192.209.235"
        
       
    }

    stages{
        stage("checkout"){
            steps{
                checkout scm
            }

        }

        stage("test build "){
            steps{
                script{
                 withCredentials([usernamePassword(credentialsId:'crc-repo',
                  usernameVariable: 'username',
                  passwordVariable: 'password')]){
                  sh("git pull https://$username:$password@github.com/orgabai1212/c.r.c.git")
                 }
                
                 sh"docker-compose down -v "
                 sh"docker-compose build --no-cache"
                 sh"docker-compose up -d"
                 sleep (time: 5, unit: 'SECONDS')
                 sh"curl -v ${test_ip}:${app_port}"
                }
                
                
            }




        }
        stage('version + ecr') {
            steps {
                script{
                    withCredentials([usernamePassword(credentialsId: 'crc-repo2',
                     usernameVariable: 'username',
                     passwordVariable: 'password')]){
                     sh("git pull https://$username:$password@github.com/orgabai1212/c.r.c.git")
                    }
                    def version = sh(script: './check-tag.sh', returnStdout: true).trim()
                    echo "the new version is $version"
                    sh "git tag $version"
                    withCredentials([usernamePassword(credentialsId: 'crc-repo2',
                     usernameVariable: 'username',
                     passwordVariable: 'password')]){
                     sh "git push https://$username:$password@github.com/orgabai1212/c.r.c.git $version"
                     sh "docker build -t crc_app:$version ."
                     sh "docker tag crc_app:$version 932763848879.dkr.ecr.eu-central-1.amazonaws.com/crc:$version"
                     sh "docker push 932763848879.dkr.ecr.eu-central-1.amazonaws.com/crc:$version"
                    
                    }
                    
                    
                }
            }
        }
        stage('ssh'){
            steps{
                withCredentials([sshUserPrivateKey(credentialsId: "ssh", keyFileVariable: "", usernameVariable: "ssh")]) {
                    sh "ssh ubuntu@${deploy_ip} touch motherfucker"
                    // sh "ssh ubuntu@${deploy_ip} docker image rm -f 644435390668.dkr.ecr.eu-west-3.amazonaws.com/or-cowsay:v3"
                    // sh "ssh ubuntu@${deploy_ip} aws ecr get-login-password --region eu-west-3 | docker login --username AWS --password-stdin 644435390668.dkr.ecr.eu-west-3.amazonaws.com"
            		// sh "ssh ubuntu@${deploy_ip} docker pull 644435390668.dkr.ecr.eu-west-3.amazonaws.com/or-cowsay:v3"
                    // sh "ssh ubuntu@${deploy_ip} docker run -d --name cowsay_mission -p ${deploy_port}:3001 -e PORT=3001 644435390668.dkr.ecr.eu-west-3.amazonaws.com/or-cowsay:v3"
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