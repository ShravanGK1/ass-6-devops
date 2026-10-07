# Assignment No. 6: Jenkins Integration with GitHub

## Title
**Integrate Jenkins with a Git Repository and Automate Source Code Retrieval from GitHub**

---

## 🎯 Aim
To configure Jenkins with a GitHub repository and automate the process of pulling source code from the repository for Continuous Integration (CI).

---

## 📌 Objectives
1. Understand the role of Jenkins in CI/CD pipelines.
2. Install and configure Git & GitHub plugins in Jenkins.
3. Connect Jenkins with a GitHub repository.
4. Create a Jenkins Freestyle Job / Pipeline Job for automated source code checkout.
5. Execute a simple build and automated tests through Jenkins.

---

## 📋 Prerequisites
- **Jenkins:** Installed and running (Default: `http://localhost:8080`)
- **Git:** Installed on local machine and configured in Jenkins Global Tool Configuration
- **GitHub Account:** Active account with this repository pushed
- **Python / Java:** Installed on the host/agent system

---

## 📂 Repository Structure
```
ass-6_devops/
├── README.md               # Project & Assignment Documentation
├── ASSIGNMENT_REPORT.md    # Detailed lab report with steps and expected console outputs
├── index.html              # Sample frontend web page
├── app.py                  # Sample Python application logic
├── test_app.py             # Automated unit tests for Jenkins CI stage
└── Jenkinsfile             # Declarative Jenkins CI/CD pipeline
```

---

## 🛠️ Step-by-Step Jenkins Configuration Guide

### Method 1: Freestyle Project Configuration
1. Open Jenkins Dashboard (`http://localhost:8080`).
2. Click **New Item** ➔ Name: `GitHub-Jenkins-Demo` ➔ Select **Freestyle project** ➔ Click **OK**.
3. Under **Source Code Management (SCM)**:
   - Select **Git**.
   - Enter Repository URL: `https://github.com/<your-username>/<your-repo-name>.git`
   - Specify Branch: `*/main` (or `*/master`).
   - For private repos, add GitHub Personal Access Token (PAT) under **Credentials**.
4. Under **Build Steps**:
   - Add build step ➔ **Execute Windows batch command** (or **Execute shell** on Linux):
     ```bash
     python -m unittest test_app.py
     python app.py
     ```
5. Click **Save**.
6. Click **Build Now** to trigger the build.

---

### Method 2: Jenkins Pipeline (Recommended)
1. Open Jenkins Dashboard ➔ Click **New Item**.
2. Enter Name: `GitHub-Jenkins-Pipeline` ➔ Select **Pipeline** ➔ Click **OK**.
3. Under **Pipeline Definition**:
   - Select **Pipeline script from SCM**.
   - SCM: **Git**.
   - Repository URL: `https://github.com/<your-username>/<your-repo-name>.git`
   - Branch Specifier: `*/main`.
   - Script Path: `Jenkinsfile`.
4. Click **Save** and then **Build Now**.

---

## 📊 Expected Output & Verification
- Jenkins automatically clones the latest commit from GitHub into `workspace/`.
- Unit tests in `test_app.py` run and pass.
- `app.py` executes successfully.
- **Build Status:** Green / Blue (SUCCESS).
