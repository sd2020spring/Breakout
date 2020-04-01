# Mini Project 4: Breakout
By Izumi and Lilo

## Project Overview
We implemented Breakout, the arcade game, using the pygame library. It is functional and entertaining, with customizable dimensions, difficulty, and color schemes.

## Results
We accomplished creating a functional and customizable game of breakout that allows the user to customize the game state in **model.py/BreakoutModel/__init__**, for example to edit the wall dimensions/number of layers, color scheme, paddle/ball size, etc.

Some examples of the game in action:  
<img src="images/image2.png" width="450"> <img src="images/image4.png" width="450">

## Implementation
### Classes
Our code uses the Model-View-Controller framework and has the following classes:
* Model: BreakoutModel
* Game view: PyGameWindowView
* Controllers: PyGameKeyboardController & PyGameMouseController
* 3 game objects:
  * Ball
  * Paddle
  * Wall

### Interactions/Actions

    BreakoutModel's scope includes all 3 gamepieces and their location/size, so this is where their interactions are handled:
      * calculates when the ball hits a specific brick, and tells the wall to remove it
      * calculates when the ball has fallen below the paddle, and changes 'loser' to True
      * checks how many bricks are left, and if it is 0, changes 'winner' to True
      * calculates whether the ball hit the paddle, and tells the ball when to change its' speed to bounce off
    Ball: calculates whether it has hit the walls of the window, and changes its' speed to bounce off
    Wall:
      * tracks how many layers are left on each brick using the 2D array 'bricks'
      * displays the color of each brick as the color at the index of the number of layers in the 'colors' array
    Paddle: tracks its' x position, wrapping at the edges of the screen
    PyGameKeyboardController & PyGameMouseController: tell the paddle where to move to
    PyGameWindowView: draws the game based on the underlying game state in the given BreakoutModel
    breakout.py: start_game() method ties together the model, view, controller by doing all of the following in the main loop:
      * updating the model
      * redrawing the view
      * having the controller handle events

### UML Class Diagram
<img src="images/UML Class.png">

### Design Decision
We made the design choice to allow the wall to have multiple layers which correspond to the display color because it added complexity, customizability, and visual appeal to the game. Leaving the wall as 1 layer only and instead working on other features such as the start/end screens was less desirable because it would add more classes and require some restructuring to this project, which we did not feel we had the time to execute.

## Reflection
From a process point of view, the fact that we were able to functionally code our project was a success. It was appropriately scoped, being completely doable, and there is even a bit more room to expand outwards, adding extra features or even making a whole 'arcade' full of games.

In terms of working with a partner, we didn't have the time to sketch out the whole project and divide up work before spring break/coronavirus leave because we only had half of a class period. We were able to work successfully remotely, but had not properly gotten started until after the break, detracting from the time we had to work. Next time, we will make an initial plan as soon as possible and adapt it as necessary.
