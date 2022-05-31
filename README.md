# DJANGO_AUTH


## Create a new Django project for a blog , the project should have the following:

### You have 2 Models:
- Post (user , title, content, date , image) . Note : for user make sure to use the User model from Django
- Comment (first_name, email, content, date)

### Your website should have
- An index page to display all the blogs (only image & title  & date) .
- A detail Page for each post , in that page display the post (image, title, date, content) & the comments (firstname, date, content)
- Create a group "editors" in the admin panel or programmatically . This group should have the permission for adding a post. 
- User can add a post only if he has permission to add a post. 
- User can only get to the add post page if he is authenticated and has permission , or else forward the user to register / login page. 


Note : use .gitignore to not inclue the folder "venv" in the repo.
