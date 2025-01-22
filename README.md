# Recipe Manager Web Application

This project is a web application built using the Django framework, designed for managing recipes with user authentication and CRUD functionalities. Key features include:

## Key Features
### User Authentication
The application uses `django.contrib.auth` for secure user authentication. The `authenticate()` function, `login()` method, and `login_required` decorator are utilized to ensure that only authorized users can access specific views.

### Recipe Management
Authenticated users can perform CRUD operations using function-based views:

- **Create**: Add new recipes with details such as name, description, and an optional image.
- **Read**: View a list of all recipes along with their details.
- **Update**: Modify the details of existing recipes.
- **Delete**: Remove recipes from the system.

This project showcases the use of Django's function-based views, templates, forms, and session management to deliver a dynamic and user-friendly experience.

## Slug Details
In this application, slugs are used for creating SEO-friendly URLs for each recipe. A **slug** is a short label used in the URL, generated from the recipe name. Slug generation follows these rules:

- Slugs are automatically created from the recipe name, with spaces replaced by hyphens.
- If a recipe name is changed, the slug will be updated to match the new name.
- The slug is stored in the database, and each recipe's detail page can be accessed via its unique slug (e.g., `http://127.0.0.1:8000/recipe/<slug>`).

## Setting Up the Project

### 1. Clone the Repository
Start by cloning the project repository from GitHub (or your chosen platform):

```bash
git clone https://github.com/sanju17-prog/recipe_maker.git
```

### 2. Set Up a Virtual Environment
Create and activate a virtual environment to isolate project dependencies:

- For Linux/Mac:
```bash
python3 -m venv env
source env/bin/activate
```

- For Windows:
```bash
python -m venv env
env\Scripts\activate
```

### 3. Install Dependencies
Install the required packages using pip:

```bash
pip install -r requirements.txt
```

### 4. Configure the Database
Apply the migrations to set up the database: 

```bash
python manage.py migrate
```

### 5. Run the Development Server
Start the Django development server:

```bash 
python manage.py runserver
```

### 6. Access the Application
Open your browser and navigate to:

```http://127.0.0.1:8000/```

### 7. Load Static Files

```bash
python manage.py collectstatic
```

```bash

Now, the **slug details** section is added, explaining how slugs are generated and used in the application. This should provide the necessary details for users interacting with your project!
```



