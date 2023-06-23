
<h1 align="center">
    Memory Game
</h1>

<!-- <p align="center">
    <a href="" alt="Video Tour">Take a Video Tour</a>
</p> -->

![Page Image](/Screenshots/InitialPage.png?raw=true)

<!-- [![Video Tour](/Screenshots/Login.png?raw=true)](https://youtu.be/) -->

### *A Birthday Activity*  
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
I thought it would be fun to use my coding skills to create a unique birthday "card" for a friend.

[Return to Table of Contents](#Table-of-Contents)

___

## Features
* Location of images is randomized each time the memory game is started

<img src="https://github.com/Purposefully/MemoryGame/blob/master/Screenshots/GameOne.png?raw=true" alt="Game One" width="300">  

<img src="https://github.com/Purposefully/MemoryGame/blob/master/Screenshots/GameTwo.png?raw=true" alt="Game Two" width="300">  

* Success pattern shows which squares have already been solved

<img src="https://github.com/Purposefully/MemoryGame/blob/master/Screenshots/MostlyComplete.png?raw=true" alt="MostlyComplete" width="300">  

* Success message displays when game has been won

<img src="https://github.com/Purposefully/MemoryGame/blob/master/Screenshots/Success.png?raw=true" alt="Game won" width="300">  

* Final birthday message page displays

<img src="https://github.com/Purposefully/MemoryGame/blob/master/Screenshots/FinalMessage.png?raw=true" alt="FinalMessage" width="300">  


[Return to Table of Contents](#Table-of-Contents)
___

## Technologies Used
* HTML
* CSS
* JavaScript



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
    git clone https://github.com/Purposefully/MemoryGame.git
    ```
2. Move into the repository
    ```
    cd MemoryGame
    ```
3. Run the index.html file
    ```
    index.html
    ```


[Return to Table of Contents](#Table-of-Contents)
