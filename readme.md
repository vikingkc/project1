
# Django Beginners

## Description

This project demonstrates Model Creation , making migrations and ORM Queries in Django 




## Table of Contents (Optional)

- [Installation](#installation)


## Installation (REQUIRED )
Firstly create new Python virtual environment using\
```bash
python -m venv myenv
```
# Activate that environment
For windows
```bash 
myenv\Scripts\activate
```
For Linux
```bash
myenv/bin/activate
```
After the successful activation you can see (myenv) infornt of every terminal cmd change directory to project directory(directory where manage.py file resides)

## Dependency Install
We need to install django and other dependencies\
here we have requirements.txt file with is list of all required dependencies\
Run  
```bash
pip install -r requirements.txt
```
change directory to project directory to run migrations and server
```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```
and then finally
```bash
python manage.py runserver
```