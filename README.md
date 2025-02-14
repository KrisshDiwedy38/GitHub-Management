# GitHub Management Project

## Overview
The **GitHub Management Project** automates common GitHub tasks using the GitHub API. This project allows users to create repositories, manage issues, retreive the list of repositories and delete repositories—all through API calls.

## Features
- **Create a Repository**
- **List User Repositories**
- **Create an Issue in a Repository**
- **Delete a Repository**

## 🛠️ Technologies Used
- **Python** 🐍
- **GitHub REST API** 🔗
- **Requests Library** 📡

## Authentication
To interact with the GitHub API, you need to generate a **Personal Access Token (PAT)**:
1. Go to [GitHub Developer Settings](https://github.com/settings/tokens)
2. Click **Generate new token**
3. Select necessary scopes
    -  Read access to metadata
    -  Read and Write access to administration, code, and issues
5. Copy and store your token securely

## Setup Instructions
```sh
# Clone the Repository
git clone https://github.com/your-username/github-management-project.git
cd github-management-project

# Install Dependencies
pip install requests

# Set Up Environment Variables
export GITHUB_TOKEN="your_personal_access_token"

# Run the Script
python manage_github.py
```

## API Endpoints Used
```markdown
| Action              | Method | URL Format |
|---------------------|--------|------------------------------------------------|
| Create Repo        | `POST`  | `https://api.github.com/user/repos` |
| List User Repos    | `GET`   | `https://api.github.com/user/repos` |
| Create Issue       | `POST`  | `https://api.github.com/repos/{owner}/{repo}/issues` |
| Delete Repo        | `DELETE` | `https://api.github.com/repos/{owner}/{repo}` |
```

## 📝 Example Usage
### **Creating a Repository**
```python
import requests

GITHUB_TOKEN = "your_token_here"
headers = {"Authorization": f"Bearer {GITHUB_TOKEN}", "Accept": "application/vnd.github+json"}

owner = "KrisshDiwedy38"
repo_name = "Hello-World"
repo_desc = "Example Repository"
url = f"https://api.github.com/repos/user/repos"

data = { 'name' : repo_name , 'description' : repo_desc , 'homepage' f"https://github.com/{repo_name}", "private" : False}

response = requests.post(url, headers=headers, json= data)
if response.status_code == 201:
  print(f"{repo_name} Created Successfully!)
else:
    print(f"Error: {response.status_code}, {repo_name} could not be created")
```

## 🤝 Contributions
Contributions are welcome! Feel free to fork this repository, create a branch, and submit a pull request. 

---
### ✨ Happy Coding! 🚀

