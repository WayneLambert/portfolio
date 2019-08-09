// Simple class of a Person object
// The 'export' keyword makes the class public (i.e. importable in other modules)
// The 'default' keyword is used as it is the parent class and therefore should be the default

export default class Person {
  constructor(name) {
    this.name = name;
  }

  walk() {
    console.log('Walk');
  }
}

/**
Let's define a programmer class. This time, we will use inheritance to extend
from the parent class of Person
*/

export class Programmer extends Person {
  constructor(name,language) {
    super(name);
    this.language = language;
  }
  
  program() {
    console.log('program');
  }
}

const programmer = new Programmer('Mark Zuckerberg')
console.log(programmer);

programmer.name = 'Wayne Lambert'
console.log(programmer);

programmer.program()
console.log(programmer.walk,programmer.program);

programmer.language = 'JavaScript'
console.log(programmer);
