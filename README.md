# CoffeeHouse

[Deployed site](http://coffee-house-4393250a7201.herokuapp.com/)\
Use "Ctrl + click" or "CMD + click" to open in new tab

# Table of contents    

1. [UX](#ux)
2. [Features](#features)
    1. [Existing Features](#existing-features)
    2. [Future Features Consideration](#future-features-consideration)
3. [Technologies used](#technologies-used)
4. [Testing](#testing)
    1. [Manual Testing](#manual-testing)
    2. [Automated Testing](#automated-testing)
5. [Deployment](#deployment)
6. [Credits](#credits)
7. [Acknowledgements](#acknowledgements)

# UX

### User stories
* First Time Visitor Goals
    * First time users should be able to understand the purpose of the site.
    * They should be able to navigate the site without any issue.
    * The site should encourage users to interact with it.

* Returning Visitor Goals
    * Returning visitors should be able to notice any changes on the website.
    * The site should still encourage users to interact with it.

* Frequent User Goals
    * Frequent users should be able to take a break and have enjoyable conversation with the community.
    * They may spend some time looking at other users’ tables.

### Design

Colour Scheme

Main colours used on the website\
![Color palette](static/assets/images/colour_palette.png)

Typography

### Wireframes
<details>
<summary>Mobile</summary>

![Mobile wireframe](static/assets/images/Wireframe_Mobile.png)

</details>
<details>
<summary>Tablet</summary>

![Tablet wireframe](static/assets/images/Wireframe_Tablet.png)

</details>
<details>
<summary>Desktop</summary>

![Desktop wireframe](static/assets/images/Wireframe_Desktop.png)

</details>

# Features

## Existing features

### Landing page 

The landing page itself is the login page. It is meant to encourage visitors to create an account before proceeding to the site.\
Once logged in, users will be presented with the currently active tables.\
Due to Django Allauth’s session handling, in case a user doesn't log out before leaving the site, the session will not be terminated
and they will be presented with the tables as well instead of a login page again.\
\
Here users can create or join any table they wish.\
To create a table they simply need to locate the creation button, and a modal will be presented to name and describe the table.\
\
While it is possible to visit this page without logging in, the creation button is hidden, until the user is logged in.\
This is to ensure only verified users can create new tables.\
Table join buttons remain visible, instead they redirect to the login page thanks to Django Allauth's login required view property.\
In this case after a successful login, the user will be redirected to the table view right after.

### Table

Each active table will have a separate page. On this page users can have a conversation with each other.\
Users can add replies using the button on the bottom. They can also update their comments easily.\
Tables can be deactivated only by the user who created them, and the corresponding button is visible exclusively to the creator.

### Navigation bars

The footer element is positioned and fixed at the bottom of the page.\
The element provides links to social media platforms, namely in order Facebook, X, Google and Github.\

On top is the navigation bar. It is positioned and fixed to the top of the screen.\
Once a user is logged in, the bar will be populated with a dropdown menu, greeting the user.\
In this menu the user can logout and access their information to update.\
If the site is currently displaying a table page, a back button is added so the users can easily navigate back to all tables.

### Account management

On this page users can update their details, or delete their account.

## Future features consideration

# Technologies used

* Used [Balsamiq](https://balsamiq.com) to create wireframes.
* Used [Visual Studio Code](https://code.visualstudio.com) as IDE.
* Used [Github](https://github.com) to store and deploy the repository.
* Used [Sourcetree](https://www.sourcetreeapp.com) for version control.
* Used [Opera](https://www.opera.com), [Mozilla](https://www.mozilla.org/en-GB/) and [Chrome](https://www.google.com/intl/en_uk/chrome/) browsers and their respective developer tools for testing.

# Testing

## Manual testing

## Automated testing

### HTML validation

### CSS validation 

### JS validation

# Deployment

### Github pages

### Forking a repository

### Download local repository

### Clone a repository with Sourcetree

# Credits
    * Gitignore generated via [ChatGPT](https://chatgpt.com)
    * Index.html template was copied and modified from previous [Best Barber project](https://github.com/bics/BestBarber)
    * Used [Bootstrap](https://getbootstrap.com) as css.

### Code

    * Modal code block taken and modified from official Bootsrap documentation https://getbootstrap.com/docs/5.0/components/modal/
    * Card code block taken from official Bootstrap documentation for cards https://getbootstrap.com/docs/5.3/components/card/
    * Dropdown menu code block taken from official Bootstrap documentation for dropdowns https://getbootstrap.com/docs/4.0/components/dropdowns/
    * Allauth fields taken from Code Institute material
    * Snippets generated using Chatgpt:
        * tables.html image selector for new table creation
        * Styling for the above image selector
        * Hiding form field when creating new tables
        * Auto updating form with logged in user
        * Conversation view
        * Custom admin user register for site
        * Error handling for replies, when users have no pictures
        * Allauth settings
        * Allauth signup form
        * Allauth login form
        * Account management form fields
        * Null check for model variable
        * Deletion view try-catch block
        * SMTP settings entries
        * Cloudinary settings for file uploads
        * Helper text for avatar uploads
    * Code inspired from playlist created by Codemy.com https://www.youtube.com/watch?v=HHx3tTQWUx0&list=PLCC34OHNcOtqW9BJmgQPPzUpJ8hl49AGy
        * 

### Content

### Media

coffee_grounds : https://www.freepik.com/free-photo/close-up-view-dark-fresh-roasted-coffee-beans-coffee-beans-background_10427093.htm#fromView=search&page=1&position=39&uuid=dd3094e1-c073-4c34-a288-5332a4380af5&query=coffee

coffee_mug_cartoony : https://www.freepik.com/free-vector/coffee-love-foam-with-beans-cartoon-icon-illustration_12006499.htm#fromView=search&page=1&position=48&uuid=dd3094e1-c073-4c34-a288-5332a4380af5&query=coffee

coffee_drank : https://www.freepik.com/free-photo/overhead-vertical-shot-person-s-hand-near-latte-art-coffee-wooden-surface_7901191.htm#fromView=search&page=2&position=2&uuid=dd3094e1-c073-4c34-a288-5332a4380af5&query=coffee

coffee_interior : generated by ChatGPT

coffee_mug_tilted : https://www.freepik.com/free-vector/coffee-cup-cartoon-vector-icon-illustration-food-drink-icon-isolated-flat-vector_394067450.htm#fromView=search&page=4&position=29&uuid=dd3094e1-c073-4c34-a288-5332a4380af5&query=coffee

coffee_separated : https://www.freepik.com/free-photo/coffee-beans-top-view-white-background-space-text_8060692.htm#fromView=search&page=2&position=39&uuid=c749efba-f08b-4b9c-ad49-001cd20ad639&query=coffee

coffee_separated_nobg : modified in Canva

avatars.jpg : https://www.freepik.com/free-vector/profile-icons-pack-hand-drawn-style_18156023.htm#fromView=search&page=1&position=7&uuid=80e53d81-6ddc-4bcb-9e26-615757ec447a&query=avatar

empty_avatar : https://www.freepik.com/free-vector/blank-user-circles_134996379.htm#fromView=search&page=1&position=1&uuid=f8d57935-e0cc-4c71-9735-a9e8336ee67e&query=empty+avatar

# Acknowledgements



