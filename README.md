# Full-Stack Template Project 
I created this project to help me learn how to build a full stack project.
This is a basic template project that I can use as a reference for basic CRUD
usage of a database API in a web application. With this template, I can focus on 
more complex features. 

Frontend:
    Javascript
    React

Backend:
    Python
    Flask
    SQLAlchemy


# The rest of the readme is an explanation to myself of how the project works. 
# Files and what they do:

Frontend: 
    ContactList.jsx - displays all contacts from the database using react web page

    ContactForm.jsx - create a new contact using react web page
        /* this is a explanation of how the page works for future reference */
            sets up the page on line 3
            creates the variables to be displayed lines 4-6
            onSubmit function to send data to the backend
                recreate data lines 11-15
                create url and declare options lines 16-23
                fetch API data from backend lines 24-30
            returns react web page html design 

    App.jsx - the main page of the application

    main.jsx - the rendering of the app so it can be an App 

Backend:
    config.py - using Flask config SQLAlchemy database to store data

    models.py - in the database created adding a contact class with basic information to store and a to_json method to convert to json 

    main.py - Flask web app with routes to create, read, update, and delete contact functions this should basically be the menu for the API 

# Steps to make full-stack project: 

*if you do not know what data you need start to build the frontend with dummy data 
*this will help you know what data you need to store use get etc
Backend (reminder that backend is in itself basically an API):
1. create backend folder
2. create models folder for to store objects, data structures
3. create config folder for setting up database & other APIs 
4. create main file for routes to communicate with databases APIs data structures etc 
5. Ensure that everything data wise or changing wise within the desired application must be somehow retrieved

Frontend:
1. %npm create vite@latest frontend -- --template react
2. following step 1 run commands: npm install, npm run dev
3. create pages in SRC 