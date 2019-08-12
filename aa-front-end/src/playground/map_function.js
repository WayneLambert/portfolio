// An array of colours can be mapped using an arrow function

// Traditional JavaScript Function
// const colours = ['red','green','blue']
// const items = colours.map(function (colour) {
//   return '<li>' + colour + '</li>'
// });

// The above function can be refactored into an arrow function improving its readability
// Also notice the use of the backtick operator to denote a string placeholder.
// The ${} placeholder enables a string to be placed within it. This is essentially the same as Python's f strings.
const colours = ['red', 'green', 'blue']
const items = colours.map(colour => `<li>${colour}</li>`);
console.log(items);
