# 🚀 nopCommerce CI/CD Pipeline with Jenkins, Docker, MSSQL & Ngrok (HTTPS) 

This project sets up a **complete CI/CD pipeline** using **Jenkins** to automate the build and deployment of the [nopCommerce](https://github.com/hhsakaa/nopCommerceAk) application. The deployment is containerized using **Docker**, connected to a **MSSQL** database, and exposed securely to the internet using **Ngrok with HTTPS termination**.

---

## ✅ Features

- Automated CI/CD with **Jenkins Declarative Pipeline**
- Docker-based deployment of:
  - nopCommerce (ASP.NET Core app)
  - MSSQL Server
- Secure HTTPS exposure using **Ngrok**
- Clean and modular `docker-compose.yml`
- Jenkins automatically:
  - Pulls latest source from GitHub
  - Builds Docker image
  - Spins up containers
  - Exposes app online
- BLEU/ROUGE scoring setup included for content quality evaluation (if needed)

---

## 🛠️ Tech Stack

- Jenkins
- Docker & Docker Compose
- MSSQL Server
- Ngrok (for HTTPS exposure)
- GitHub (source version control)
- Optional: Python (for BLEU/ROUGE scoring with `nltk` and `rouge-score`)

---

## 🔧 CI/CD Pipeline Stages

1. **Checkout Stage**  
   Pulls latest code from the configured GitHub repository.

2. **Build Stage**  
   Builds Docker images using `Dockerfile`.

3. **Deploy Stage**  
   Uses `docker-compose` to spin up `nopCommerce` and `MSSQL`.

4. **Expose to Internet**  
   Starts Ngrok to expose port `8080` via HTTPS and logs the public URL.

5. **Post Action**  
   Echoes deployment success message.

---

## 🚀 Quick Start

### 1. Clone Your Forked Repo

```bash
git clone https://github.com/hhsakaa/nopCommerceAk.git
cd nopCommerceAk
```

### 2. Set Up Jenkins Pipeline

- Create a new pipeline job in Jenkins.
- Point it to your GitHub repo.
- Use the provided `Jenkinsfile`.

### 3. Install Dependencies (on Jenkins Agent)

```bash
sudo apt update
sudo apt install -y docker.io docker-compose python3-pip unzip
pip3 install nltk rouge-score
wget https://bin.ngrok.com/linux/amd64/ngrok-stable-linux-amd64.tgz
tar -xvzf ngrok-stable-linux-amd64.tgz
sudo mv ngrok /usr/local/bin
ngrok config add-authtoken <your-ngrok-authtoken>
```

---

## 🐳 Docker Setup

Ensure the root directory has the following:

- `docker-compose.yml`
- `Dockerfile` (for nopCommerce build)

```bash
docker-compose up -d
```

---

## 🔒 HTTPS with Ngrok

Jenkins runs:

```bash
ngrok http 80
```

You can fetch the public HTTPS URL using Ngrok’s local API
---

---

## 📈 Evaluation (Optional)

If you're running content evaluation:

```bash
python3 score_eval.py
```

BLEU and ROUGE scoring scripts use `nltk` and `rouge-score`.

---

## 📁 Project Structure

```
.
├── docker-compose.yml
├── Dockerfile
├── Jenkinsfile
├── score_eval.py
├── README.md
└── ...
```

---

## 🌐 Access

Once deployed, your application will be live at:

```
🔗 https://<random-subdomain>.ngrok.io
```

Check Jenkins build logs for the exact URL.

---

## 👨‍💻 Author

**Akash Raghav**  
DevOps Engineer | Cloud Enthusiast  
[LinkedIn](https://www.linkedin.com/in/hhsakaa/) · [GitHub](https://github.com/hhsakaa)

---

