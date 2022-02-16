# Alcoholic Free Social Drinks Ireland

## About
This website was setup to provide a platform for people who are considering taking a break from alcohol & those who don't drink alcohol. It allows people to freely share their experiences with a non-alcoholic drink lifestyle & leaves open a comments space for curious people to interact.

It is also a place for people who enjoy going out to drink non-alcoholic drinks to meet other alcohol free drinkers in their locality. 

## **Contents**

- [**UX (User Experience)**](#ux-user-experience)
  - [**User Stories**](#user-stories)
  - [**Site Owner Goals**](#site-owner-goals)
- [**Design Choices**](#design-choices)
  - [**Colours**](#colours)
  - [**Fonts**](#fonts)
  - [**Colours**](#colours)
  - [**Imagery**](#imagery)
  - [**Wireframes**](#wireframes)
- [**Technologies**](#technologies)
  - [**Languages**](#languages)
  - [**Database**](#database)
  - [**Libraries**](#libraries)
  - [**Tools**](#tools)
- [**Features**](#features)
  - [**Site Navigation**](#site-navigation)
  - [**Features Implemented**](#features-implemented)
  - [**Future Features**](#future-features)
  - [**Database Layout**](#database-layout)
  - [**Responsive Design**](#responsive-design)
- [**Version Control**](#version-control)
- [**Testing**](#testing)
- [**Deployment**](#deployment)
  - [**Running Locally**](#running-locally)
- [**Credits**](#credits)
  - [**Code**](#code)
  - [**Content**](#content)
  - [**Images**](#images)
  - [**Inspiration**](#inspiration)
  - [**Acknowledgements**](#acknowledgements)

## **UX (User Experience)**


### **User Stories**
- All users
    - I would like to find more information on alcohol free drinks.
    - I would like to find more information on peoples experience of replacing alcohol with a alcohol free lifestyle so that I can make a more informed decision. 
    - I would like to share my experiences of replacing alcohol with a alcohol free lifestyle so that those considering can make a more informed decision.
    - I want the site to be easy to navigate on mobile primarily so I can use it on the go.
    - I want the site to be responsive on all devices.
    - I would like to be able to comment on articles/blogs so that I can express my views to share with others
    - I would like to be able to write my own blog post to share my experience with others who may be curious
    - I would like to be able to like the posts by other Users on the website so I can express my appreciation
    - I would like to be able to arrange an event so that I can meet other people in my area who enjoy drinking alcohol free drinks
    - I would like to be able to like comments so that I can express my agreement

- As a first time user
    - I would like to be able to register with no problems and minimal information required.
    - I would like it to be able to read the articles before I register to participate.
    - I would like to be able to register via a simple process so that I can join the community.
    - I would like the navigation to be self explanotory & User friendly on all devices

- As a returning user
  - I would like to be able to delete my posts or comments or likes on request.
  - I would like to be able to log in to see book reviews I have written and favourited on one page


### **Site Owner Goals** 
  - To allow alcohol free drinkers a space to share their positive & negative experiences with a non-alcoholic drink lifestyle.
  - To give alcohol free drinkers the opportunity to easily set up social/meetup events in their local communities.  
  - To provide a place for the approx 20% of the population who do not drink alcohol to join social meetups in their locality, as not drinking alcohol can sometimes cause them to miss out on some social interactions.

## **Design Choices**

### **Colours**
The Colours started with a dark mahogony frame to express an atmosphere of a dark, trendy, stylish cocktail bar. 

### **Fonts**

### **Imagery**
The images were sourced using various websites _________ which offered free images when referenced respectively 

### **Wireframes**

## **Technologies**
- [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML)
  - Used as the main markup language for the website content.
- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)
  - Used to style the individual webpages.
- [Python 3](https://www.python.org/)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
    - Used to show the questions through pagination and for the game play. -->


### **Languages**

### **Database**
- [Postgres]

### **Libraries & Frameworks**
- [Django](https://www.djangoproject.com/)
    -High level framework used for rapid development of the site.
- [Bootstrap5.0](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
    -CSS Framework for developing responsive and mobile-first websites.

### **Tools**

[Back to contents](#contents)

## **Features**

### **Site Navigation**

### **Features Implemented**

#### **Features relevant to all pages** (extended via *base.html*):

- **Header**
  - **Navigation**

- **Hero sections**

- **Footer** 

#### **Home Page** (*index.html*) 

#### **Log In Page** (*login.html*)
  **Form** 

#### **Register** (*register.html*)
   **Form**

[Back to contents](#contents)

#### **Blog Page**
 etc......

[Back to contents](#contents)

### **Error Pages**

#### *404.html*

### **Responsive Design**

### **Future Features**

## **Database Layout**
- **Posts Diagram**

|     Key    |     Name     |     Type       |
| -----------| -------------| ---------------|
|            |Title(Unique) |Char(200)       |
|ForeignKey  |Author        |User model      |
|            |Created date  |DateTime        |
|            |Updated date  |DateTime        |
|            |Content       |TextField       |
|            |Featured Image|Cloudinary Image|
|            |Excerpt       |TextField       |
|Many to Many|Likes         |User model      |
|            |Slug(Unique)  |SlugField       |
|            |Status        |Integer         |
- **Comments Diagram**

|     Key    |    Name    |     Type    |   Extra Info    |
| ---------- | -----------| ------------|-----------------|
|ForeignKey  |post        |Post model   |Cascade on delete|
|            |name        |CharField    |Max length 80    |
|            |email       |EmailField   |                 |
|            |body        |TextField    |                 |
|            |created+on  |DateTimeField|auto_now_add_True|
|            |approved    |BooleanField |default False    |

- **Add Events Diagram**

|     Key    |     Name     |     Type       |
| -----------| -------------| ---------------|
|            |Title(Unique) |Char(200)       |
<!-- |ForeignKey  |Author        |User model      |
|            |Created date  |DateTime        |
|            |Updated date  |DateTime        |
|            |Content       |TextField       |
|            |Featured Image|Cloudinary Image|
|            |Excerpt       |TextField       |
|Many to Many|Likes         |User model      |
|            |Slug(Unique)  |SlugField       |
|            |Status        |Integer         |  -->

[Back to contents](#contents)

## **Version Control**

### Gitpod Workspaces

### Gitpod branching and committing to GitHub

[Back to contents](#contents)

## **Testing**

## **Deployment**



## **Credits**

### **Code**

### **Inspiration**


### **Acknowledgements**
[Back to contents](#contents)

