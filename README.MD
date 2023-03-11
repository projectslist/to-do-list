# TODO List
This is a Django project with a set of URL patterns that includes views for registration, login, logout, task list, task details, task creation, task update, and task deletion.
It is a simple CRUD project with unit tests examples.

# Installation
- Clone the repository using git clone 
- ``https://github.com/projectslist/to-do-list.git``.
- Make ready python env for the project
- Run the server using python manage.py runserver.

# URL Patterns
The following URL patterns are defined in the urlpatterns list in urls.py:

- /register/ - The RegisterPage view handles user registration.
- /login/ - The CustomLoginView view handles user login.
- /logout/ - The LogoutView view logs out the user and redirects to the login page.
- / - The TaskList view displays a list of all tasks.
- /task/<int:pk> - The TaskDetails view displays details of a particular task.
- /task-create/ - The TaskCreate view allows users to create a new task.
- /task-update/<int:pk> - The TaskUpdate view allows users to update an existing task.
- /task-delete/<int:id>/ - The DeleteView.delete_post method allows users to delete an existing task.



# License
This project is licensed under the MIT License.
