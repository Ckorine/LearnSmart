# Project name: LearnSmart 
# Project description
  In this Web application the student will be able to test his knowledge or learn new things for a given topic. 
  He will be able to learn with Study material such as Videos and E-book  and can take a quiz on related topic. 
  
# Features
  Signup
   - Signin <br>
  If logged in user can<br>
    - Logout<br>
    - Update his account<br>
    - View his profile<br>
    - Choose a Topic, view the related lectures and take a quiz<br>
    - Share learn material for the subjects<br>
    - View his learn analystics<br>
# Technical architecture and Technologies
  -Axios : Automatically set base URL for client & server side
![alt text](http://url/to/img.png)
# Run the app
    # Run the Frontend React-app
      - open the console in the Project folder ~/LearnSmart/frontend/learnsmart-front
      - enter the command "npm start"
      -project start on localhost 3000
    # Run the Backend Flask-app
      -open the project in your favorite IDE (for this project pycharm was used) and run the app.py
     # App Deployement to Heroku
# Deploy React-app to Heroku
    # Get npm & node version
    Define engines in package.json >>
    engines{
    "npm":  npm version 
    "node": node version
    }
    • Install serve package
     run command >> npm install serve --save
    • modify package.json
     replace 
     "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test --env=jsdom",
    "eject": "react-scripts eject"
    }
    with 
    "scripts": {
      "dev": "react-scripts start",
      "start": "serve-s build",
      "build": "react-scripts build",
      "test": "react-scripts test --env=jsdom",
      "eject": "react-scripts eject"
    }
    • Modify axios initialization -> https://learnsmart-app.herokuapp.com/

    • Sign up for Heroku
   
    • Create Heroku git repository and new Heroku app

    • Connect Heroku app to the new repository “learnsmart-app”
    • Deploy your app
      
# Deploy Flask-app to Heroku
    • Create  and initialise the Procfile >> web: guincorn wsgi:app
    • Create and initialise wsgi.py file and initialise >> <br> from .app import app <br> app=app
    • Install gunicorn application server
    • Add the requirement.txt file with commnand >> pip freeze > requirement.txt
    • Sign up for Heroku
    • Create Heroku git repository and new Heroku app
    • Connect Heroku app to the new repository “learnsmart-app”
    • Deploy your app
# Connect Flask to MongoDB 
     • Set the MONGO_URL environment variable with cmd command >> <br>
        - heroku config:set MONGO_URL=mongodb://<username>:<password>@mongoprovider.com:27409/learnsamrt-app
        - git push heroku master
     PS:of course you have to obtain this MONGO_URL variable for your heroku envirotnment by adding a mongoDB database
      
