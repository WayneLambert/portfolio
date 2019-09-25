# Countdown Letters Game

The countdown project uses the logic from the letters game on Countdown to enable a player to play against the computer attempting to get the longest word that they can.

## Features

- Uses a functional programming style to implement the game's rules logic into the program
- A list of weighted consonants and vowels are built into the program according to the rules of the game so that the choices made have the same probability of being drawn as they would on the actual TV show game.
- The list of 113,809 english words is stored in a text file on the server. This was sourced from kaggle.com
- Validates that the word chosen by the player is one within the list of words text file
- Validates that the word chosen by the player uses only the randomly generated selection of letters
- Validates that the word chosen by the user exists as an entry in the Oxford English Dictionary's API (British English)
- Returns a game result and score displaying the winner
- Looks up the dictionary definition of the word using the Oxford English Dictionary's API (British English). Sometimes this means looking up the associated lemma version of the word.
- There is no 30 second clock like there is on the actual game of Countdown. This is intended so that recruiters and hiring managers don't have to wait for a countdown timer to expire.

## Technologies Used

- Languages: Python, HTML / CSS
- Frameworks: Django, Bootstrap, FontAwesome
- Libraries: os, random, urllib, requests
- Other: GitHub, Docker, Oxford Dictionary API

## Sources

Information and rules of the game was sourced from <http://wiki.apterous.org/Letters_game>
