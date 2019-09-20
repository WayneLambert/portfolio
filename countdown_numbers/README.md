# Countdown Numbers Game

The countdown project uses the logic from the numbers game on Countdown to enable a player to play against the computer attempting to get the closest number they can to the target.

## Features

• Uses a functional programming style to implement the game's rules logic into the program
• Validates that the calculation method used by the player is permitted
• Returns a game result and score displaying the winner
• Returns a calculation by Carol Vorderman which is as close of possible to the target number
• There is no 30 second clock like there is on the actual game of Countdown. This is intended so that recruiters and hiring managers don't have to wait for a countdown timer to expire

## Rules

Here are the rules for the numbers game on Countdown:

- Six, face-down, numbered tiles are selected from twenty-four shuffled tiles.
  - The tiles are arranged into two groups:
    - Large Numbers: There are four numbers in the large set. These are 25 , 50 , 75 and 100
    - Small Numbers: There are twenty numbers in the small set, two each of the numbers 1-10
- One contestant selects between none and 4 numbers from the large set (i.e from the top) and the remaining numbers are drawn from the small set to make six numbers in total
- A random three-digit target number is then chosen by the computer
- The contestants are given 30 seconds to get as close as possible to the chosen target by using just the four basic arithmetic operators + - × ÷
- Brackets in the calculations are permitted and ordinary BODMAS operations apply
- Not all of the digits need to be used
- Concatenation of digits is not permitted (For example, you cannot use a “2” and “2” to make “22”)
- At no intermediate step in the process can:
  - the current running total become negative
  - the running total involve a fraction
- Each numbered tile can only be used once in the calculation

## The Scoring

- 10 points are awarded for correctly getting the exact solution
- 7 points are awarded for getting within 5 of the required solution
- 5 points are awarded for getting within 10 points of the required solution
- Additional points are not granted for a closer solution within the same banding
  - For example, a player that is one away from the target scores the same as a player that is two away from the target. The game is considered a draw, although the player closest may be invited to show their calculation.
