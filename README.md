This project is a web application built using the Django framework, designed for managing recipes with user authentication and CRUD functionalities. Key features include:

User Authentication: The application uses django.contrib.auth for secure user authentication. The authenticate() function, login() method, and login_required decorator are utilized to ensure that only logged-in users can access specific views.

Recipe Management: Authenticated users can perform CRUD operations using function-based views:

Create: Add new recipes with details such as name, description, and an optional image.
Read: View a list of all recipes along with their details.
Update: Modify the details of existing recipes.
Delete: Remove recipes from the system.
This project showcases the use of Django's function-based views, templates, forms, and session management to deliver a dynamic and user-friendly experience.
