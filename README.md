# The Goose Game Kata
Goose game is a game where two or more players move pieces around a track by rolling a die. The aim of the game is to reach square number sixty-three before any of the other players and avoid obstacles. ([wikipedia](https://en.wikipedia.org/wiki/Game_of_the_Goose))

This kata has been invented by [Matteo Vaccari](https://github.com/xpmatteo) and adapted from the [Awesome Katas Repo](https://github.com/xpeppers/goose-game-kata/), you can find the original slides [here](https://www.slideshare.net/pierodibello/il-dilettevole-giuoco-delloca-coding-dojo).

![Goose Game Board](https://images.tom.shop/producten/original/jumbo_ganzenbord_2_166098.jpg)


**Exercise:** Implement the game below, focusing on writing the best code you can produce.  Use the `Game` class as a template, filling in the methods with appropriate logic based on the game rules below.  The `Gui` relies on the listed `Game` methods to render the game, and will start to work as the `Game` is made to work properly, when the `main.py` script is run.  

***Note*** The `Gui` class does not implement any of the game rules below; it only draws the current state of the board based on information from the `Game` class.


## Game Rules for a 2-Player Game

  - Two players give their names and start the game.  
  - On a player's turn, they roll two 6-sided dice.  The player moves their piece the total number of spaces as the total of their dice roll.  (e.g. rolling a 3 and 4 means moving 7 spaces.)
  - **Win**: A player wins if they land **exactly** on space 63.
  - **Bounce**: If a player rolls past space 63 (e.g. 64), they **"bounce"**, and go back to where they began their turn.
  - **Bridge**: If a player lands on space 9, then they go directly to space 16 in the same turn.
  - **Goose**: If a player lands on space 4, 8, 13, 18, 23, or 27 (a green space), they get to roll again!
  - **Prank**: If a player lands on a space occupied by another player, then they send the other player back to their previous position (e.g. if player 1 was on 20, then lands on player 2 at space 22, then player 2 is moved immediately to space 20.)
