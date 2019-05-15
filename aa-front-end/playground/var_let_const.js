function sayHello() {
  for (let i = 0; i < 5; i++) {
    console.log(i);
  }
  console.log(i);
}

sayHello();

// The result of this code is that the console logged i is not defined because
// the first occuring instance of i is within the for loop therefore its scope
// is bound to the for loop