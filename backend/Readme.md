# go to backend folder
`cd backend/`

# create venv
`virtualenv venv`

# activate venv
`source venv/bin/activate`

Mac, Linux: ( `pipenv install` )
             `pipenv shell`

# install
`pip install -r requirements.txt`

`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py add_users`

Mac, Linux:
`python manage.py loaddata data/master-data/*.json`

`python manage.py runserver`

# deactivate venv
`deactivate`

# save new packages
`pip freeze > requirements.txt`
