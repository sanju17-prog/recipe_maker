This project is a web application built using the Django framework, designed for managing recipes with user authentication and CRUD functionalities. Key features include:

User Authentication: The application uses django.contrib.auth for secure user authentication. The authenticate() function, login() method, and login_required decorator are utilized to ensure that only authorized users can access specific views.

Recipe Management: Authenticated users can perform CRUD operations using function-based views:

Create: Add new recipes with details such as name, description, and an optional image.
Read: View a list of all recipes along with their details.
Update: Modify the details of existing recipes.
Delete: Remove recipes from the system.

This project showcases the use of Django's function-based views, templates, forms, and session management to deliver a dynamic and user-friendly experience.


Here's how to set up and run the project: 
- Follow these steps to run this Django project in your local environment:

1. Clone the Repository
Start by cloning the project repository from GitHub (or your chosen platform):

git clone https://github.com/sanju17-prog/recipe_maker.git 

2. Set Up a Virtual Environment
Create and activate a virtual environment to isolate project dependencies:

- For Linux/Mac:
python3 -m venv env
source env/bin/activate

- For Windows:
python -m venv env
env\Scripts\activate

3. Install Dependencies
Install the required packages using pip:

pip install -r requirements.txt

4. Configure the Database
Apply the migrations to set up the database: 

python manage.py migrate

5. Run the Development Server
Start the Django development server:

python manage.py runserver

6. Access the Application
Open your browser and navigate to:

http://127.0.0.1:8000/

7. Load Static Files

python manage.py collectstatic





