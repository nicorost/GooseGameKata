# The Goose Game Kata
Goose game is a game where two or more players move pieces around a track by rolling a die. The aim of the game is to reach square number sixty-three before any of the other players and avoid obstacles. ([wikipedia](https://en.wikipedia.org/wiki/Game_of_the_Goose))

This kata has been invented by [Matteo Vaccari](https://github.com/xpmatteo) and adapted from the [Awesome Katas Repo](https://github.com/xpeppers/goose-game-kata/), you can find the original slides [here](https://www.slideshare.net/pierodibello/il-dilettevole-giuoco-delloca-coding-dojo).

![Goose Game Board](https://www.allbusinesstemplates.com/thumbs/bc3357aa-9188-4a9a-96d7-2366127f9f87.png)


**Exercise:** Implement the game below, focusing on writing the best code you can produce.  Use the `Game` class as a template, filling in the methods with appropriate logic based on the game rules below.  The `Gui` relies on the listed `Game` methods to render the game, and will start to work as the `Game` is made to work properly, when the `main.py` script is run.


## Game Rules for a 2-Player Game

  - Two players give their names and start the game.  
  - On a player's turn, they roll two 6-sided dice.  The player moves their piece the total number of spaces as the total of their dice roll.  (e.g. rolling a 3 and 4 means moving 7 spaces.)
  - A player wins if they land **exactly** on space 63.
  - If a player rolls past space 63 (e.g. 64), they **"bounce"**, and go back to where they began their turn.
  

### 5. Space "6" is "The Bridge"
As a player, when I get to the space "The Bridge", I jump to the space "12"

**Scenarios:**
1. Get to "The Bridge"
   ```cucumber
   If there is one participant "Pippo" on space "4"
   assuming that the dice get 1 and 1
   when the user writes: "move Pippo"
   the system responds: "Pippo rolls 1, 1. Pippo moves from 4 to The Bridge. Pippo jumps to 12"
   ```

### 6. If you land on "The Goose", move again
As a player, when I get to a space with a picture of "The Goose", I move forward again by the sum of the two dice rolled before

The spaces 5, 9, 14, 18, 23, 27 have a picture of "The Goose"

**Scenarios:**
1. Single Jump
   ```cucumber
   If there is one participant "Pippo" on space "3"
   assuming that the dice get 1 and 1
   when the user writes: "move Pippo"
   the system responds: "Pippo rolls 1, 1. Pippo moves from 3 to 5, The Goose. Pippo moves again and goes to 7"
   ```

2. Multiple Jump
   ```cucumber
   If there is one participant "Pippo" on space "10"
   assuming that the dice get 2 and 2
   when the user writes: "move Pippo"
   the system responds: "Pippo rolls 2, 2. Pippo moves from 10 to 14, The Goose. Pippo moves again and goes to 18, The Goose. Pippo moves again and goes to 22"
   ```

### 7. Prank (Optional Step)
As a player, when I land on a space occupied by another player, I send him to my previous position so that the game can be more entertaining.

**Scenarios:**
1. Prank
   ```cucumber
   If there are two participants "Pippo" and "Pluto" respectively on spaces "15" and "17"
   assuming that the dice get 1 and 1
   when the user writes: "move Pippo"
   the system responds: "Pippo rolls 1, 1. Pippo moves from 15 to 17. On 17 there is Pluto, who returns to 15"
   ```
