# Instawork Team Member Management Application

## Prerequisites:
This project is a simple team-member management application that allows the user to view, edit, add, and delete team members.

### Technology Stack
- Backend: Django (Python)
- Frontend: HTML, CSS, JavaScript
- Database: SQLite (default Django database)

### Installation & setup:

1) Clone the repository:
 `git clone git@github.com:akshay-narkhede/instawork_take_home.git`

2) Set up a virtual environment:
    `python -m venv env`
    `source env/bin/activate`  *(MacOS/Linux)*
3) Install required packages:
`pip install -r requirements.txt`

4) Run migrations to set up database:
`python manage.py makemigrations`
`python manage.py migrate`

5) Run collectstatic command to copy all the static files:
`python manage.py collectstatic`

6) Start the Django application
`python manage.py runserver`


### Testing of application
- Visit `http://127.0.0.1:8000/` in your web browser to start using the application.
- Use the `+` button to add new team members
- Click on a team member (avatar or name) to edit their details
- Admin users can delete team members

### Project Structure
- `models.py`: Defines the Member model (database)
- `forms.py`: Contains the MemberForm for handling input
- `views.py`: Includes class-based views for CRUD operations
- `urls.py`: Defines URL patterns for the application
- `templates/`: Contains HTML templates for rendering pages
- `static/css/style.css`: Includes custom CSS for styling


### Approach 

I started by setting up the Member model in Django. This included all the details like name, email, phone, and role.  After that, I started writing the urls and views using Django's class-based views to handle all the adding, viewing, editing, and deleting of members. 
I used Django templates for the HTML pages, which was a little tricky to get right at first. I made 2 main pages: one to show all the members and another to add a new member / to edit the existing ones. Linking everything together with Django’s URLs sometimes got confusing, but it worked out in the end. 


### Running test cases
I have written some tests for the forms, and views.
 - Form tests: Test form validation with valid & invalid data.   
 - View tests: Test list view, create view, edit view.

`python manage.py test`

### Potential problem
So, right now, I got the given project with pages to list, add, and edit team members. But here’s the thing: we haven't set up any way to check if someone’s logged in or what role they have, like if they’re an admin or just a regular user. This means everyone could technically do anything, like deleting members, which we don't want.

To fix this, we can add a login system where users can sign in with a username and password. That way, we can check who's who and make sure only admins can delete members. This wasn't specified in the original project requirements. If this is something we want to add, just let me know. 


### Reference
 - https://docs.djangoproject.com/en/4.2/topics/forms/
 - https://medium.com/@6unpnp/installing-python-0f6e02c1f1d9
 - Given Task Documentation
