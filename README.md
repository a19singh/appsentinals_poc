# AppSentials

## Steps to setup

Note: use python3 as default python

- clone the repository

- Install the required packages to run the program
`
python -r requirements.txt
`

- Create db migrations using command
`
cd appsentinels
python manage.py makemigration
python manage.py migrate
`

- Run the app on localhost
`
python manage.py runserver
`

- Now the endpoint can be used from the web browser on 127.0.0.1:8000

- The below endpoint can be used to create a user
`
http://127.0.0.1:8000/user/create_user
`

- To get the user list, use the below endpoint
`
http://127.0.0.1:8000/user/fetch_user
`

- To fetch a specific user detail. use the below endpoint, where id can be obatined from above endpoint
`
http://127.0.0.1:8000/user/fetch_user/<int:id>
`

Note: For time being all the migrations and some data has been pre added into db
