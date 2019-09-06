// List prime numbers between 2 and 100

primeNumbers = []

function isPrime(number) {
   ` Determines whether given number is prime or not `
  for (let factor = 2; factor < number; factor++){
       if(number % factor == 0){
          return false;
       }
   }
   return true;
}

function getPrimeNumbers(maxNum) {
  ` Builds list of prime numbers up to a maximum of maxNum `
  for(let testedNum = 2; testedNum <= maxNum; testedNum++) {
      if(isPrime(testedNum)){
        primeNumbers.push(testedNum)
        console.log(primeNumbers);
    }
  }
}

primeNumbers = getPrimeNumbers(100);
