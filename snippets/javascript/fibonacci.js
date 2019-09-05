// Solution using a for loop and an array
function fibonacciArray(previous, current, maximum) {
  fibNums = []
  for (let num = 1; num < maximum; num++) {
    fibNums.push(previous)
    console.log(`Fib ${num} = ${previous}`)
    current = [previous + current, previous = current][0];
  }
  return fibNums
}


fibonacciArray(previous = 0,current = 1,maximum = 101)
