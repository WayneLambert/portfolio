/** If a class is created in a module, then it is private by default. This means
that it is not accessible to other modules within my project. To make a class
accessible, the 'export' keyword should be used before the 'class' keyword.
This makes it public and accessible in other modules within the project using the
'import' keyword.

Let's import the Person parent class and Programmer sub-class from the 'classes' module
 */

import Person from './classes';           // Example of a default import
import { Programmer } from './classes';   // Example of a named import

const person = new Person('John Smith');
const programmer = new Programmer('Steve Wozniak', 'BASIC');
console.log(person);
console.log(programmer);


// Note the pattern here. Coming from a history of Python, I am used to the
// convention of from { library } import {class }
// JavaScript have done something really creative :)
// They have gone for import { Class } from 'library';
