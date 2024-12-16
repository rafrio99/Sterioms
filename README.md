# Sterioms
#Backend
# STERIOMS Backend

## Prerequisites
- Python
- Django
- PostgreSQL
- Django Rest Framework

## Project Overview
The **Sterilization Information Management System (STERIOMS)** backend is designed to manage, track, and record sterilization processes across medical and laboratory settings, ensuring safe and efficient operations. This guide will help you set up the backend for development and testing.

## Cloning the Project ⬇️📂
To get started, navigate to a directory where you want to clone the project and run:
```bash
git clone git@github.com:sdt-grp-two-uestc/backend.git
```
## Virtual Environment 📁🏚️
Change directory into the project director. Create a virtual environment named `venv` using Python's module `venv`.
```cmd
cd sterioms/

python -m venv venv

```

Activate the virtual environment and install the dependencies
```cmd
source venv/Scripts/activate

pip install -r requirements.txt
```

Anytime you are done and wish to exit the virtual  environment, run:
```cmd
deactivate
```

## Environment Variables 📁🔐
Create a file named `.env` in the project root directory.
```cmd
touch .env
```

Set the values for these variables in the `.env` file.
```.env
DBNAME=<your_database_name>
DBUSER=<your_database_user>
DBPASS=<your_database_password>
DBHOST=<your_database_host>
DBPORT=<your_database_port>

```

## Starting the Development Server :electron:
Specifying a port number is optional
```cmd
python manage.py runserver [PORT]
```

------
Frontend
# Vue 3 + Vite

Frontend Project Setup Guide: Welcome to the frontend project! This guide will walk you through setting up your development environment, from installing dependencies to running the project.

Prerequisites: Ensure you have the following software installed on your machine before proceeding.

1. Node.js
Download and install Node.js from the official website: [Node.js](https://nodejs.org/en).
To verify if Node.js is installed, run the following command in your terminal: `node -v`
This should return the version number of Node.js installed on your machine.
2. Git
Download and install Git from the official website: [Git](https://git-scm.com/).
To verify if Git is installed, run: `git --version`
This should return the version number of Git installed on your machine.

Project Setup: Once you have Node.js and Git installed, follow the steps below to set up the project.

1. Clone the Project
First, clone the project repository from GitHub using Git: `git clone https://github.com/sdt-grp-two-uestc/frontend.git`
2. Navigate to the Frontend Directory
After cloning the repository, navigate into the frontend folder: `cd frontend`
3. Install Project Dependencies
Now, install the project dependencies using npm. This will download all required packages and modules for the frontend: `npm install`
4. Run the Development Server
Once all dependencies are installed, you can start the development server by running: `npm run dev`
This will start the development server and serve the project locally: `http://localhost:5173/`

Happy coding! 🎉

