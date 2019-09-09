# Development Plan - Countdown Project

## View 1 - countdown_letters/selection/

The first view should simply map a url `selection` to a page where the player is presented with a form where they can select from a text box permitting them to enter either a 3, 4 or 5 indicating the number of vowels they would like to use.

If the player chooses a value and clicks the submit button, then a POST request is submitted and the form is validated and the input cleansed. The input is then captured and rendered as context into the next view that is presented, 'game'.

## View 2 - countdown_letters/game/

The player is presented with another screen (`game`) which indicates the outcome of their random vowel and consonant choices into 9 suitably styled text boxes which render each of the selected letters individually.

After 5 seconds with a visual `.....` -> `....` -> `...` -> `..` -> `.` indicator, a JavaScript countdown timer starts from 30 seconds. If I can make this an analogue timer, then all the better for authenticity.

The player has access to a submit button where they can enter their word if they are confident of not requiring the full 30 seconds. Once the 30 seconds has elapsed, the text box becomes a locked object and the submission is automated.

A script will run to validate that the answer that the player has provided is an eligible one.

- This means it uses only letters that were available to be selected
- It belongs within the words.txt file of permitted words

Once validated, the script will return context to the screen telling the player that the word was eligible/ineligible and returning the corresponding score.

The score given is:

- For any word between 1 and 8 letters, 1 point per letter.
- For a 9 letter word, double points applies, therefore 18 points is awarded.

A message is returned to the interface with some conversational items for authenticity.

Another script runs to pick the largest possible eligible word from the words.txt file and return this a the computer's answer. The computer player we will call Suzie (as this will resonate as being Suzie Dent from dictionary corner). Again, the points that Suzie scores will be in line with the aforementioned rules.
