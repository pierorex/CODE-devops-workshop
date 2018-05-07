pipeline {
  // Run this pipeline on the Jenkins Master (unless otherwise specified)
  agent { label 'master' }

  stages {

    stage ('Run Unit & Integration Tests') {
      // For this stage, tell Jenkins to build the agent form the dockerfile

      agent {
        dockerfile true
      }

      steps {
        // Run the Unit Tests
        sh 'py.test app/tests -v --junitprefix=linux --junitxml test_results.xml || true'
        // Run the Integration Tests
        // sh 'py.test app/tests/integration -v --junitprefix=linux --junitxml integration_results.xml || true'
      }
      post {
        // Parse the test results so they appear in BlueOcean UI
        always {
          junit '**/*_results.xml'
        }
      }
    }

    stage ('Docker Build & Run') {
      // Since no agent{} is specified, this stage will run on the Jenkins Master
      when {
        // Only run the application when on 'master' branch
        branch 'master'
      }
      steps {  
        // Remove any existing running containers
        sh 'docker container rm --force flask-calculator-app || true'
        // Re-build the Docker Image and tag it as 'latest'
        sh 'docker build --rm -t flask-calculator-img .'
        sh 'docker tag flask-calculator-img flask-calculator-img:latest'
        // Run the new Docker Image
        sh 'docker container run --name flask-calculator-app -p 5000:5000 -d flask-calculator-img:latest'
      }
      post {
        success {
          sh "echo The app can be tested by visiting: http://`curl -s http://169.254.169.254/latest/meta-data/public-hostname`:5000"
        }
      }
    }
  }
}
