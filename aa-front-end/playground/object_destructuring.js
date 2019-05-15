// Lets destructure the following the address object

const address = {
  street: '5c Highfield Road',
  city: 'Birmingham',
  country: 'UK',
};

// The standard approach to access each of the properties of the address might be to use dot notation...
const street = address.street
const city = address.city
const country = address.country

console.log(`The address is ${street} in ${city} in ${country}`)

// However, we can use destructuring...
// The colon can be thought of as the 'as' keyword which refers to the string after
// the colon is the alias for the property before it
const { country: ctry, city: cty, street: st } = address;

ctry; cty; st