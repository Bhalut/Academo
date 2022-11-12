# Academy API

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

## Description

Academy API is a project made of Python with Django where you can find features such as registration, login, log out, get courses, get course details, get quizzes and manage it through a Teacher role.

## Features

- User registration
  - Email and password
- Login and logout user
- Quiz questions with choices
- Courses and Course Details

## Setup

Python version: `10.3.8`

This project use the following libraries and version:

- [Django](https://pypi.org/project/Django/) `4.1.3`
- [Django Rest Framework](https://pypi.org/project/djangorestframework/) `3.14.0`
- [Django Rest Framework Simple-jwt](https://pypi.org/project/djangorestframework-simplejwt/) `5.2.2`
- [MySQLClient](https://pypi.org/project/mysqlclient/) `2.1.1`

You can also check the requirements.txt file which you can install the libraries using the following command:

**Nota:** To run this program it is not necessary to do the following, we will see this later using docker compose for better control through containers.

UNIX system (Mac and linux distro)

```sh
cd app # Change directory
python3 -m venv env # Create a virtual enviroment
python3 install -r requirements.txt # Install Dependencies libraries
```

Windows

```ps
cd app # Change directory
py -m venv env # Create a virtual enviroment
py install -r requirements.txt # Install Dependencies libraries
```

## Prerequisites

For this project you will need Docker compose in your machine - [Docker Install](https://docs.docker.com/get-docker/)

you will need these files below:

For enviroment variable `.env.dev`

```sh
#file route: app/.env.dev

DEBUG=1
SECRET_KEY=django-insecure-9((sopobsdo-kv+hq%bsd1*wr940&1nxiu=ilf-6e-#byr=9px
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
```

For MySQL configuration `my.cnf`
**Nota:** These values should match the values that are configured in docker compose `.docker/docker-compose.yml`.

```sh
#file route: app/.config/my.cnf

[client]
database = app
user = app
password = app
port = 3306
HOST = 127.0.0.1
socket = ./db/mysql.sock
default-character-set = utf8
```

## 🚀 Usage

Clone the project locally in your machine.

```sh
git clone https://github.com/Bhalut/Academo.git
```

Go into the docker settings directory (`.docker`)

```sh
cd .docker
```

Run the container with docker compose

```sh
docker compose up
```

or you can use docker compose `Detached mode` settings for "Run containers in the background"

```sh
docker compose up -d
```

This will run the `db` (MySQL Database) container and the `server` (Django App) container

And you will already have the application available to view in your preferred client at :

```sh
0.0.0.0:8000/api/v1/
```

or

```sh
http://127.0.0.1:8000/api/v1
```

or

```sh
http://localhost:8000/api/v1
```

## Author

- 👤 Abdel Mejia (Twitter [@SoyBhalut](https://twitter.com/SoyBhalut) - GitHub [bhalut](https://github.com/Bhalut))
