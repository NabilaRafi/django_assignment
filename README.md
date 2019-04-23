# django_assignment


Description on Task completed:
*****************************

- Created Login page using basic login modules available in Django
- Welcome page with a link, which navigates to the graph view
- Length of one random joke is ploted in the charts.js,  http://api.icndb.com/jokes/random 

Setup and commands used:
************************

- Install python, PIP and then Django

- Followed the django documentation https://docs.djangoproject.com/en/2.2/intro/tutorial01/ to create the project and application structutre. Both the project and application name are created as tikoassignment

- Three views Login.html, welcome.html and graph.html are created as templates. Base html is used to load the common libraries such as jquery, charts, bootstrap js and bootstrap css.

- application routing are defined in the urls.py file

- one auth user is created using the 'python manage.py createsuperuser' and followed the documentation (https://docs.djangoproject.com/en/2.2/topics/auth/default/) to create and validate the user creation.

- Basic styling is done using the bootstrap classes, need to improve the same later on

Command to run application: python manage.py runserver

Steps to run the application:

- launch http://127.0.0.1:8000/charts/login
- enter username: admin, Password: Google@123
- Navigates to the welcome screen which naviagtes to graph view
- joke length of one json object is plotted in the graph


Further improvements:

- Unit test needs to be included
- login failure scenario to be handled
- Styling and UX needs to be added
- gulp tasks to be integrated








