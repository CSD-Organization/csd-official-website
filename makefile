.DEFAULT_GOAL = run

py := python

# Run server
run: manage.py
	@${py} manage.py runserver

run_insc:
	@${py} manage.py runserver --insecure

# Make migrations
compile: manage.py
	@${py} manage.py makemigrations master
	@${py} manage.py migrate

# Create super user
user: manage.py
	@${py} manage.py createsuperuser