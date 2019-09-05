// Calculates the number of `guesses` required to arrive at the `chosen_num`

function binarySearch(tmpArray,guess) {
  guessCount = 1;
  lowerBound = 0;
  upperBound = tmpArray.length;

  while (lowerBound <= upperBound) {
    midpoint = Math.floor((upperBound + lowerBound) / 2)

    if (guess < midpoint) {
      upperBound = midpoint - 1
      guessCount += 1
    };
    if (guess > midpoint) {
      lowerBound = midpoint + 1
      guessCount += 1
    };
    if (guess == midpoint) {
      return guessCount
    };
  }
}

millionItemArray = []
for (let i = 1; i <= 1000001; i++) {
  millionItemArray.push(i)
}
chosenNum = 646235

numberOfGuesses = binarySearch(millionItemArray, chosenNum)

console.log(`It took ${numberOfGuesses} guesses to get to the right number.`);
