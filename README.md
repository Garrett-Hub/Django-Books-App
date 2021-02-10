# Introduction

For the first Live Project during The Tech Academy's Software Development bootcamp we were tasked with creating a Django App in Python.  I chose to implement a database of books with a related table of authors.  The app has basic CRUD functionality and also allows the user to search the table of books by title.  Additionally, I connected to the Open Library API and allowed the user to search their database by title and filter the results by the author.  The results are then displayed in a table with a link to Open Library's page for that document.

## Project Management

For this project we used Azure DevOps with the Scrum framework for project management.  We had daily stand-ups as a team to discuss the stories we were working on and any roadblocks we might have encountered. Each Friday we had a sprint retrospective for more in depth discussions about how the week went for us.

## CRUD Functionality
The first story for this project had me creating the basic home page template and style for the app.  I also set up a simple function-based view for the home page and registered the home page URL with the overall Django Project and linked to my app from the project's home page. The app's home page extended from a base template that I used for all the templates in the app.

* ### Create
For the next story I created Models for a Book and Author.  The Book model was related to the Author model with a foreign key.  I also created ModelForms for each Model and templates with views to add new objects to the database.

* ### Read
For the next two stories I created templates and views to view every item from both tables.  Each item listed had a link to a details page that displayed all the data for each item in a ModelForm.

For an optional challenge I also created a class-based view to allow the user to search the table of books for a specific title and displayed the results in a table.

* ### Update and Delete
For the final story before moving onto working with an API I created views to delete and update items from its details page.

## API
The next few stories involved choosing a public API and allowing the user to query their database.  I used Open Library's search API and created a view that let the user search by title and filter the results by author.  The view parses through the JSON response and displays each document's title along with a link to the corresponding Open Library page.

## Skills Acquired

Creating my own app was a great way to hone my skills in Python and the Django framework.  Working in a Scrum framework was a good introduction to working as a team as well as how branching and pull requests work.