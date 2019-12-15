[![Build Status](https://travis-ci.org/KimKiHyuk/Resume-Admin.svg?branch=master)](https://travis-ci.org/KimKiHyuk/Resume-Admin)

# Resume Admin Page


## make tar 
* tar -cvf secrets.tar .secrets
* travis encrypt-file secrets.tar --add

## migration
* python manage.py makemigrations 
* python manage.py migrate

## update requirements.txt
* pip freeze > requirements.txt