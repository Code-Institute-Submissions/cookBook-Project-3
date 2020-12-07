# The COOKBOOK-Prokect website

  This is my milestone project I am doing for Code Institute for  Data Centric module. The website lets you add, update, view and delete recepies that are stored in a cloud database

## UX
 
The website structure is minimalist and functional where the user is presented with a suggestive logo and a title followed by a search box with three button option to search a certain recipe, to update and reset the search.
Below the user will find the database collection with all the elements and for each element it has the option to view, update and delete the recipe. 
The update recipe page has all the fields and two buttons at the end to submit or cancel the current form. 

The wireframe was designed using Balsamic and the example can be viewed here below.
 ![Window wireframe](static/media/cookBook.png)

## Features

The website has multiple features for the user to manipulate the data base
 
### Existing Features
- Search - When the user types in the search box followed by click on the search button it allows the user to filter through the database based on 3 criterias name, cusine and course
- Update - When the user clicks the "New" button it allows to register a new recipe into the database
- Reset - When the user clicks the "Reset" button it resets the search filter to reveal all recipes in the database
- Wiew - When the user clicks the "View" Icon button corresponding to each recipe it will be able to view all the fields and details registered in the DB for that recipe
- Update -When the user clicks the "Update" Icon button corresponding to each recipe it will be able to update all the fields and details registered in the DB for that recipe
- Delete - When the user clicks the "Delete" Icon button corresponding to each recipe it will be able to delete the recipe only after it confrims the action in the dialog box

After each feature the user will recive a flash message at the top of the screen informing on the success of the action undertaken. 

### Features Left to Implement
- In the future I would like to implement a dashboard page where the user can get information about the most popular recipes by cuisine and have a daily graphic updates on the number of recipes 
added to the database on  a particular date. 

## Technologies Used

- [JQuery](https://jquery.com)- The project uses **JQuery** to simplify DOM manipulation.
- [MongoDB](https://www.mongodb.com/cloud/atlas)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [HTML](https://www.w3schools.com/html/html_intro.asp)
- [CSS](https://www.w3.org/Style/CSS/Overview.en.html)
- [Bootstrap](https://getbootstrap.com/)


## Testing

The website was manualy tested with Chrome Developer Tool in a Test Driven Development approach on difrerent screen size as well on other browsers such as Edge and Firefox.

Testing procedure 
1. Search form:
    1. Go to the "Home" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid recipe and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

2. New form:
    1. Go to the "Home" page and press the "New" Button
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with all inputs valid and verify that a success message appears.

3. Reset form:
    1. Go to the "Home" page and press the "Reset" Button
    2. Check if the database resets to diplay all recipes
4. View:
    1. Go to the "Home" page and press the "View" Button on each recipe
    2. Check if the recipe is displayed correctly with all fields 
5. Update form:
    1. Go to the "Home" page and press the "Update" Button on each recipe
    2. Check if the recipe is displayed correctly with all fields 
    3. Try to submit the new form with all inputs valid and verify that a success message appears.
3. Delete form:
    1. Go to the "Home" page and press the "Delete" Button
    2. Check if the confirmation box appears and validates the action
    3. If confirmed check if you recive the success flash message and the database was updated without the deleted recipe
    2. If not confirm check the database to see no recipe has been deleted. 

I spent quite some time on the js sweetalert confirmation issue on passing the JSON object with complex arguments in order to trigger the flask app you cand view the link below at the credits section.  

## Deployment

At the begining of the project I first created a heroku account  and used the GitHub deplyement method to link it with the current workspace. Once linked I created the requirements.txt file and the Procfile
followed by the variables configuration on the Heroku website where i have configured all sesitive data variables. 

Each time I commit and push  to the server the HEROKU gets updated with the latest version. The only diffrence between the development and the production version 
represents the debug tool which is turned off.  You can view the production version [here](https://cookbook-milestoneproject.herokuapp.com/)


## Credits

- The documentation that helped me fix the issue can be found [here](https://stackoverflow.com/questions/46034634/sweet-alert-confirmation-before-delete)
- The documentation that helped me fix the issue for the disappearing flash alerts can be found [here](https://stackoverflow.com/questions/4613952/why-flash-message-wont-disappear)
- This website uses datatables plug-in via CDN for a more dynamic and elegant display of the data tables. The link can be found [here](https://datatables.net/)
