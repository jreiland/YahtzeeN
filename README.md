The "Smooch" font is credit Robert Leuschke and is used under the Open Font License provided in `OFL_smooch.txt` in this repository.
"Raleway" family fonts are credit Matt McInerney, Pablo Impallari, Rodrigo Fuenzalida and are used under the Open Font License provided
in `OFL_raleway.txt` in this repository.
This project is generally licensed under the MIT License provided in LICENSE.md.
Subarray algorithm provided by: https://thispointer.com/python-check-if-a-list-contains-all-the-elements-of-another-list/

__System Requirements:__

This game requires a screen resolution of 1024x768; the window cannot be scaled/resized.
To run this program, you __must__ have a 64-bit installation of Python 3, as well an installation of the required `pygame` library (v2.0.0 or greater)

To install on macOS/Linux/Other Unix-like OSes, type the following terminal command: `python3 -m pip install --user pipenv`

To install on Windows, type the following into the command prompt `py -m pip install --user pipenv`

    WARNING: This game has not been tested on platforms other than macOS!!!

The game will look somewhat odd if you do not download the font files in this repository.

__How to Play/Run the Game:__ Run `yahtzeen.py` to play the game. The gameplay is the same as regular Yahtzee, but there is no possibility of an Upper Section Bonus or Yahtzee Bonus. You can click on a die in your current set to lock it for the next roll. The game will automatically switch between Player 1 and Player 2. To attempt a move, click on the applicable upper section die, or click anywhere inside the applicable lower section box. If the move applies to your set of dice, you will receive those points. Otherwise, you will receive a zero and cannot try again.

__Known Issues:__ 
 - The "Upper Section Score," "Lower Section Score," and "Total Score" text will move depending on the number of digits that comprise the score.
 - Clicking on a section to score it will cause a jump to the other player immediately, i.e., you cannot see the score you just made before the player is switched.

__Any questions?__
    Contact John Reiland at jreiland1@pride.hofstra.edu
