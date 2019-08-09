// We can use spread operators to concatenate arrays

const first = [1,2,3]
const second = [4,5,6]

// The old approach
const oldCombined = first.concat(second);

// The new approach
const newCombined = [...first,...second];

console.log(oldCombined);
console.log(newCombined);

// Both methods return the same result, however the new approach is much more flexible.
// We can add new elements in the middle or at the end of the array

const moreCombined = ['inserted at start',...first,'inserted in middle',...second,'inserted at end']
console.log(moreCombined);

// We can clone an array. We can see that they're both the same
const clone = [...first]
console.log(first);
console.log(clone);

// Combine some objects
const firstObject = { name: 'Wayne' }
const secondObject = { job: 'Developer' }
const combinedObjects = { ...firstObject,...secondObject, location: 'UK' }
console.log(combinedObjects);
