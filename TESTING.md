The project was tested thoroughly and the results are presented below:

## Table of contents:

 * [Validation](#validation)
    + [HTML](#html)
      - [W3C Markup Validation Service](#w3c-markup-validation-service)
    + [CSS](#css)
      - [W3C CSS Validation Service](#w3c-css-validation-service)
    + [JavaScript](#javascript)
      - [JSHint](#jshint)
    + [Python](#python)
    + [Lighthouse](#lighthouse)
      - [Desktop](#desktop)
      - [Mobile](#mobile)
  * [Testing of User stories & UX values](#testing-of-user-stories-&-ux-values)
      - [General](#general)
      - [Events](#events)
      - [Blog](#blog)
      - [Contact](#contact)
  * [Testing process](#testing-process)
    + [Manual Testing](#manual-testing)
      - [Navigation bar](#navigation-bar)
      - [Footer](#footer)
      - [Home](#home)
      - [Sign up page](#sign-up-page)
      - [Login page](#login-page)
      - [Logging out](#logging-out)
      - [Events](#events-management)
      - [Blog](#blog)
      - [Comments](#comments)
      - [Contact](#contact)
      - [CRUD Functionality](#crud-functionality)
      - [Responsiveness](#responsiveness)
      - [Browsers and devices](#browsers-and-devices)
      - [Defensive Programming](#defensive-programming)
    + [Bugs](#bugs)
      - [Fixed Bugs](#fixed-bugs)
      - [Known Bugs](#known-bugs)

## Validation

### HTML
## [HTML](https://validator.w3.org):

All pages were free from errors, except those noted below
base.html:
Error :Element li not allowed as child of element nav in this context.
* All li tags are wrapped in ul tags
Error: Duplicate ID user-options & specials-link
* Used on the same page for the same function

The rest of the issues are related to Templating{}

![HTML Validation](readme/assets/)



#### W3C Markup Validation Service 

* [W3C Markup Validation Service](https://validator.w3.org/) was used to validate the HTML of the project. Each page was validated by its URL and produced no errors or warnings. When each HTML page was validated by direct input, all errors produced were due to templating.

![HTML Validation](readme/assets/)

### CSS

#### W3C CSS Validation Service

* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used to validate the CSS of the project. As well as showing no errors when validating the projects CSS through its URI, there was also no errors when each CSS file was validated through direct input.

![CSS Validation](readme/)

### JavaScript

#### JSHint

* All JavaScript files or snippets of JavaScript at the bottom of HTML files were validated successfully through [JSHint](https://jshint.com/).
    ![JavaScript Validation](readme/assets/t)


### Python

* All Python files were validated through the use of [PEP8 online](http://pep8online.com/) and all passed successfully.

    ![Python Validation](readme/assets)

### Lighthouse

* Lighthouse was also used to test the project on both desktop and mobile.


#### Desktop

![Lighthouse Desktop Result](readme/assets/)

#### Mobile

![Lighthouse Mobile Result](readme/assets/)

## Testing of User stories & UX value

* Starting from an unregistered customer...

    #### General





    ### Events
    * *As a user

        * The

        ![Homepage background](readme/assets/testing-imag)


    ### Checkout
  

    ### Blog
    * *As a user/non user I can view comments on an individual post so that I can read other peoples opinion*

        * 

        ![Read Comments](readme/assets/testing-ima)

    * *As a User I can view a list of posts so that I can select one to read based on the synopsis*

        * 

        ![Read blogs](readme/assets)

    * *As a user I can leave comments on a post so that I can be involved & express my view*

        * 

        ![Add comments](readme/assets/tes)

    ### Contact
   





## Testing process
## Manual Testing
The website was thoroughly tested as per the detailed account of the manual testing is below:

#### Navigation bar


#### Footer

#### Home


#### Sign up page
* The user can sign up and create an account by clicking the 'Accounts' dropdown menu on the top right. When they click on 'Sign Up' they are taken to the correct page to register. &check;
* Each form field provides a message if they have not been filled in correctly. &check;
* A notification will appear if a user has already registered with the email address they are using. &check;
* A message saying username exists will appear if the user inputs one already taken. &check;
* A 'password is too short' message appears if the user doesn't fill it in correctly. &check;
* Password 'too common will also appear when necessary. &check;
* It will show Password is 'entirely numeric. &check;
* Email is successfully sent to user when taken to verification page. &check;
* The link in the email takes the user to a page in which they can confirm verification. &check;
* Once signed up successfully, the user is redirected to login page so they can sign in with new credentials. &check;
* The link that takes the user to the login page works as intended. &check;
* All Allauth buttons works as expected. &check;

#### Login page
* A message will appear advising the user that the 'Username and/or Password specified are not correct'. &check;
* The user can sign in with a username or email. &check;
* The link that takes the user to the sign up page works as intended. &check;
* The user can reset their password by clicking on 'Forgot Password?'. It takes them to a page where they input their email address. When the user clicks on the link, they are able to change password and are advised its been successfully reset. &check;
* The form fields alert the user if they haven't input anything into each field. &check;
* All Allauth buttons works as expected. &check;

#### Logging out

* When the user is logged in they can log out by going to the 'Accounts' dropdown menu and selecting 'Log Out'. It correctly takes them to the Log out page where the user can log out. &check;
* When the user confirms they are logging out, by clicking on the 'Sign Out' button it correctly signs them out of their account withh a messge confirming. &check;


#### Events Page


#### Blog

##### Blog page


##### Blog Detail page


#### Blog Comment

#### Contact

* All form fields show a message if nothing is inputted into them or its content is not valid and stops the user submitting the form until it is valid. &check;
* A toast also appears on successful submission telling the user, 'Alcohol-Free Shop' will be in touch shortly. &check;
* You do not have to be a user to send a message to Alcohol-Free Shop via the contacts page 

#### CRUD Functionality

* All CRUD functionality was tested and worked as expected. &check;

#### Responsiveness
* Responsiveness work was continually worked on, some areas including the incremental & decremental buttons may need more work with alignment to be more responsive particularly on the smallest phone sizes. The subjects comments can be cut off below 350 but this can/will be resolved in time.
#### Browsers and devices
* I have constantly done test on different browsers & sent to friends & family to do the same. I made some changes in particular in the css to resolve issues on many browser using linear-gradient(footer & subject) & opacity. I found some issues on my phone but when I do the phone test on my laptop it is working ok.  

* The website was tested on the following Desktop browsers:

    * Firefox
    * Google Chrome + Mobile
    * Microsoft Edge 
    * Brave + Mobile
    * Duck Duck Go(mobile)



#### Defensive Programming


## Bugs
### Fixed Bugs
##### Bug 1


##### Bug 2

##### Bug 3
* My contact page would not open due to a programming error for at least a few days. Every time I went back to it I would tweet the code a bit & run migrations. Nothing seemed to work so I decided to delete the migrations file & run migrations again. when this didn't work decided to delete all migration files in the tree & make migrations again. As this did not work I tried deleting the back on from a different angle to make sure all migrations we removed. Until I finally tried : python3 manage.py migrate contact zero, which managed to clear the database for me to run migrations & resolve problem &check;
 


    