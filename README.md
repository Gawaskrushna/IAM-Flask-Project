🔐 Identity and Access Management (IAM) System – Flask

📌 Project Overview

This project is a Role-Based Identity and Access Management (IAM) System developed using Python Flask. It manages user identities and controls access based on different roles such as SuperAdmin, Admin, Employee, and User.

The system ensures secure authentication, authorization, and user lifecycle management, similar to real-world enterprise IAM solutions.

🚀 Features

✅ User Registration and Login
✅ Secure Password Hashing (SHA-256)
✅ Role-Based Access Control (RBAC)
✅ SuperAdmin, Admin, Employee, and User roles
✅ Separate Dashboard for each role
✅ User Creation and Deletion
✅ Protection for critical accounts
✅ Session Management
✅ Professional Dashboard UI
✅ Secure Logout


👥 User Roles and Permissions -
Role	Permissions,
SuperAdmin	Full access, manage all users,
Admin	Create and delete Employee and User,
Employee	Limited dashboard access,
User	Basic dashboard access.

🛠️ Technology Stack

Backend:
Python
Flask

Frontend:
HTML
CSS

Database:
SQLite

Other Tools
Git
GitHub
VS Code

📂 Project Structure
IAM-Flask-Project
│
├── app.py
├── database.db
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── admin.html
│   ├── superadmin.html
│   ├── employee.html
│   └── user.html
│
├── static/
│   └── style.css
│
└── README.md

⚙️ Installation and Setup
Step 1: Clone Repository
git clone https://github.com/yourusername/IAM-Flask-Project.git
Step 2: Go to Project Folder
cd IAM-Flask-Project
Step 3: Install Flask
pip install flask
Step 4: Run Application
python app.py
Step 5: Open Browser
http://127.0.0.1:5000

🔑 Default SuperAdmin Login

Username: superadmin
Password: super123

🔒 Security Features

Password hashing

Session management

Role-based access restriction

Protected SuperAdmin account

Self-delete protection


🎯 Learning Outcomes

Through this project, I learned:
Identity and Access Management concepts,
Authentication and Authorization,
Role-Based Access Control,
Flask Framework,
Database integration,
Session handling,
Git and GitHub version control.


👨‍💻 Author

Krushna Gawas


📎 GitHub Repository

https://github.com/Gawaskrushna/IAM-Flask-Project.git

