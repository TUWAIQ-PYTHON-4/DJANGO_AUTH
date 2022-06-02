# DJANGO_AUTH

Website link: https://tuwaiq-django-jawaherblog.herokuapp.com/


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

### what an unregistered visioter will see.
![Screenshot (412)](https://user-images.githubusercontent.com/63616896/171518304-235ab6e7-4fb5-4762-bb44-17d0bcb3bd19.png)


### what a registered user in editor group will see.
![Screenshot (413)](https://user-images.githubusercontent.com/63616896/171518370-0d114b71-6ea0-44af-895b-868a27700fad.png)

![Screenshot (414)](https://user-images.githubusercontent.com/63616896/171518428-5a316748-a86f-4b7d-b64b-7dbe25268b24.png)

### Post details 
![Screenshot (415)](https://user-images.githubusercontent.com/63616896/171518487-c017a281-fe78-43dd-b5bf-e11338e511f9.png)
![Screenshot (416)](https://user-images.githubusercontent.com/63616896/171518558-94674bde-c8fa-441b-9297-00688bc2b0b3.png)
![Screenshot (417)](https://user-images.githubusercontent.com/63616896/171518608-f19c8a6e-1f26-4ca2-9193-36ee2c0a2cff.png)


