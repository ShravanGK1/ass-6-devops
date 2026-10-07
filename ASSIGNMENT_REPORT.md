# Assignment No. 6: Practical Report

## Title
**Integrate Jenkins with a Git Repository and Automate Source Code Retrieval from GitHub**

---

### **Aim**
To configure Jenkins with a GitHub repository and automate the process of pulling source code from the repository for Continuous Integration.

---

### **Objectives**
1. Understand the core role of Jenkins in automating CI/CD workflows.
2. Install and configure the Git and GitHub plugins in Jenkins.
3. Establish a secure connection between Jenkins and a remote GitHub repository.
4. Set up an automated build job (Freestyle & Declarative Pipeline) to checkout code upon execution.
5. Verify build status, workspace directory, and inspect console logs.

---

### **Prerequisites**
- Jenkins server up and running (`http://localhost:8080`).
- Git CLI installed and present in system PATH.
- GitHub account with an initialized repository.
- Python runtime environment.

---

### **Theoretical Concept**
**Jenkins** is an open-source automation server enabling developers to build, test, and deploy software continuously. 

**CI/CD Workflow Overview:**
```
+------------------+         +-------------------+         +-------------------+
|  Developer       |  git    |  GitHub           | Webhook |  Jenkins Server   |
|  Local Workspace | ------> |  Remote Repo      | ------> |  (Automated Build |
|                  |  push   |  (main branch)    | / Poll  |   & Test Run)     |
+------------------+         +-------------------+         +-------------------+
                                                                     |
                                                                     v
                                                            +-------------------+
                                                            | Build Artifacts   |
                                                            | & Console Report  |
                                                            +-------------------+
```

1. **Source Code Retrieval:** Jenkins uses the Git plugin to clone or fetch recent commits into its isolated workspace (`/var/jenkins_home/workspace/<job-name>` or `C:\ProgramData\Jenkins\.jenkins\workspace\<job-name>`).
2. **Build and Test:** Configured build triggers or manual runs invoke the test suite and build scripts.
3. **Feedback:** Jenkins marks the build with `SUCCESS`, `UNSTABLE`, or `FAILURE` and records logs.

---

### **Step-by-Step Procedure**

#### Step 1: Create and Push Repository to GitHub
1. Initialize local repository:
   ```bash
   git init
   git add .
   git commit -m "Initial commit for Jenkins Integration"
   git branch -M main
   git remote add origin https://github.com/<username>/<repo-name>.git
   git push -u origin main
   ```

#### Step 2: Configure Git Plugin in Jenkins
1. Open Jenkins: `http://localhost:8080`
2. Navigate to **Manage Jenkins** ➔ **Plugins** ➔ **Installed Plugins** (verify **Git Plugin** and **GitHub Integration Plugin** are enabled).
3. Under **Manage Jenkins** ➔ **Tools** ➔ **Git installations**, ensure `git.exe` path is properly detected or default `Default` is used.

#### Step 3: Create Jenkins Freestyle Job
1. From Dashboard, click **New Item**.
2. Enter Item Name: `GitHub-Jenkins-Demo`.
3. Choose **Freestyle project** and click **OK**.

#### Step 4: Configure Source Code Management (SCM)
1. In the job configuration, navigate to **Source Code Management**.
2. Select **Git**.
3. **Repository URL**: `https://github.com/<username>/<repo-name>.git`
4. **Credentials**: Select GitHub credentials (if private repo) or leave `none` (if public).
5. **Branches to build**: `*/main`.

#### Step 5: Configure Build Step
1. Scroll down to **Build Steps** ➔ **Add build step**.
2. Select **Execute Windows batch command** (Windows) or **Execute shell** (Linux).
3. Add the following command:
   ```bash
   python -m unittest test_app.py
   python app.py
   ```

#### Step 6: Trigger Build & Verify Console Output
1. Click **Save**, then click **Build Now**.
2. Click on the generated build number (e.g. `#1`) ➔ **Console Output**.

---

### **Sample Console Output**
```text
Started by user admin
Running as SYSTEM
Building in workspace C:\ProgramData\Jenkins\.jenkins\workspace\GitHub-Jenkins-Demo
using credential github-auth
 > git.exe rev-parse --resolve-git-dir C:\ProgramData\Jenkins\.jenkins\workspace\GitHub-Jenkins-Demo\.git # timeout=10
Fetching changes from the remote Git repository
 > git.exe config remote.origin.url https://github.com/example-user/ass-6_devops.git # timeout=10
Fetching upstream changes from https://github.com/example-user/ass-6_devops.git
 > git.exe fetch --tags --force --progress -- https://github.com/example-user/ass-6_devops.git +refs/heads/*:refs/remotes/origin/* # timeout=10
 > git.exe rev-parse "refs/remotes/origin/main^{commit}" # timeout=10
Checking out Revision 8a4b12c9f9e1d8481234567890abcdef12345678 (refs/remotes/origin/main)
 > git.exe config core.sparsecheckout # timeout=10
 > git.exe checkout -f 8a4b12c9f9e1d8481234567890abcdef12345678 # timeout=10
Commit message: "Initial commit for Jenkins Integration"
[GitHub-Jenkins-Demo] $ cmd /c call ...
...
Ran 3 tests in 0.002s

OK
==================================================
Hello, DevOps Engineer! Welcome to Jenkins CI/CD Integration.
Sample Calculation (5 + 7): 12
Health Status: OK
==================================================
Application executed successfully during Jenkins build!

Finished: SUCCESS
```

---

### **Pipeline as Code (Jenkinsfile)**
```groovy
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Pulling latest code from GitHub...'
                checkout scm
            }
        }
        stage('Test') {
            steps {
                echo 'Running Unit Tests...'
                script {
                    if (isUnix()) {
                        sh 'python3 -m unittest discover -s . -p "test_*.py"'
                    } else {
                        bat 'python -m unittest discover -s . -p "test_*.py"'
                    }
                }
            }
        }
        stage('Build & Run') {
            steps {
                echo 'Executing Application...'
                script {
                    if (isUnix()) {
                        sh 'python3 app.py'
                    } else {
                        bat 'python app.py'
                    }
                }
            }
        }
    }
    post {
        success {
            echo 'Build and test executed successfully!'
        }
    }
}
```

---

### **Conclusion**
In this assignment, Jenkins was successfully configured and connected to a remote GitHub repository. The automated retrieval of source code via Git SCM was implemented and validated using both Freestyle and Pipeline build configurations. The automated test suite and execution steps verified continuous integration readiness.
