# Holiday Roulette

This code is designed for the procrastinating traveller that just can't decide where they should go to next. There is a very small sleep between each generated choice.
This is a design decision to slow down the code so that the traveller can feel the suspense whilst the roulette wheel determines their fate. :)

The purpose of the project is to illustrate the implementation of randomised choices and the logging of them using the logging module.

## Features

- Uses a random generator to decide upon a choice for each spin of the roulette wheel where the best of 1000 spins determines the winning location.
- Logs all of the choices to a log file on the server. This is not accessible to see by the visitor.
- The visitor can click a link to see the logging, although they will not actually see the log file. Instead, a script runs to read all lines into the Django template. Some formatting is done with the text to give it a fixed width font and authentic feel.
- The winning location screen includes an image of the actual location just to increase the wanderlust even more.

## Technologies Used

- Languages: Python, HTML / CSS
- Frameworks: Django, Bootstrap, FontAwesome
- Libraries: logging, operator, random, time
- Other: GitHub, Docker
