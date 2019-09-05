// FizzBuzz implementation with reversal of string

function reverseString(str) {
  return str.split('').reverse().join('');
}

for (let num = 1; num < 101; num++) {
  if (num % 3 == 0 && num % 5 == 0) {
    console.log(reverseString('zzubzziF'));
  }
  if (num % 3 == 0) {
    console.log(reverseString('zziF'));
  }
  if (num % 5 == 0) {
    console.log(reverseString('zzuB'));
  }
  else {
    console.log(num);
  }
}
