# imonomy_task

run migrations
./manage.py makemigrations && migrate

run webserver
./manage.py runserver

then you can access app on the following host
http://localhost:8000/

filtering with params 
http://localhost:8000/?client_name=test_client&date=2020-09-12

to get the data from the api you can run 
render/service.py

it also accepts date range with 
render/service.py --date_ranges dd-mm-yyyy_dd-mm-yyyy
