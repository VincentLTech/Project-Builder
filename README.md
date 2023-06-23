
<h1 align="center">
    Project Builder 
</h1>
___

## Table of Contents
* [Background](#Background)
* [Features](#Features)
* [Technologies Used](#Technologies-Used)
* [Functionality](#Functionality)
* [Design](#Design)
* [Running Locally](#Running-Locally)

___

## Background
It was a solo project that I wanted to create to practice my knowledge in Python/Flask/MySQL Development.

[Return to Table of Contents](#Table-of-Contents)

___

## Features
* Guide to how the websit works

* Try Registering for your account for the first time. Or Login if you have already registered

<img src="Screenshots\Screenshot1.jpg" alt="Game One" width="600">  

* If this is yout first time registering for your account, add your name email and password.

<img src="Screenshots\Screenshot2.jpg" alt="Game Two" width="600">  

* If this is yout first time registering for your account, add you profile picture, your username and self description.

<img src="Screenshots\Screenshot3.jpg" alt="MostlyComplete" width="600">  

<img src="Screenshots\Screenshot4.jpg" alt="Game won" width="600">  

* To get started, click on create a new project.

<img src="Screenshots\Screenshot5.jpg" alt="FinalMessage" width="600">  

* Add your project name and description and other information it will ask of your project.

<img src="Screenshots\Screenshot6.jpg" alt="MostlyComplete" width="600">  

* After posting, you will be able to see the projects you deployed in the site.

<img src="Screenshots\Screenshot7.jpg" alt="Game won" width="600">  

* And you will be able to see your project in the global depot page where you can see other projects from other users and add a like to them.

<img src="Screenshots\Screenshot8.jpg" alt="FinalMessage" width="600">  


[Return to Table of Contents](#Table-of-Contents)
___

## Technologies Used
* HTML
* CSS
* Python
* Flask
* MySQL



[Return to Table of Contents](#Table-of-Contents)
___

## Functionality
Upon loading the page, pairs of images have been randomly assigned to the gameboard and "covered" with question mark images.  The user clicks on a square to reveal the hidden image.  Once two squares have been selected, the game freezes for a couple seconds so the user can see both images.  If the images match, they are replaced with a success image.  If they do not match, they are covered with the question mark image again.

Once all images have been correctly paired, the center squares display a success message.  The user may click a button to continue to the final page which displays a birthday wish.


[Return to Table of Contents](#Table-of-Contents)

___

## Design
Placement of images is randomized so the game is new every time it played.

Selected images are displayed for a couple seconds during which no further clicks are registered.


[Return to Table of Contents](#Table-of-Contents)

___

## Running Locally

1. Clone this repository
    ```
    https://github.com/GalacticKnight/Project-Builder.git
    ```
2. Move into the repository
    ```
    cd Project-Builder
    ```
3. Run these commands ONE at a time
    ```
    pipenv install flask
    pipenv shell
    pipenv install flask-bcrypt
    pipenv install PyMySQL flask
    ```
4. Run this command
    ```
    python server.py
    ```

[Return to Table of Contents](#Table-of-Contents)
