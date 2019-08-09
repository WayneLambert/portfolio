
function getFirstName(Name) {
  return Name.split(' ')[0];
}

console.log('getFirstName:', getFirstName('Wayne Lambert'));

// An arrow function which returns the first element of the splitted full name
// Notice this representation does not require the function keyword
const getFirstNameArrow = (fullName) => {
  return fullName.split(' ')[0];
}

console.log('getFirstNameArrow:', getFirstNameArrow('Lionel Messi'));

// A more terse representation of the arrow function above
// Notice this version of the function does not need the return keyword either
const getFirstNameArrowInLine = (Name) => Name.split(' ')[0]

console.log('getFirstNameArrowInLine:', getFirstNameArrowInLine('Christiano Ronaldo'));



const multiplier = {
  numbers: [1, 2, 3, 4, 5],
  multiplyBy: 6,
  multiply() {
    return this.numbers.map((number) => number * this.multiplyBy);
  }
};

console.log(multiplier.multiply());
