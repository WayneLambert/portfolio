/* eslint-disable react/react-in-jsx-scope */
let count = 0;
const addOne = () => {
  console.log('addOne');
};

const template = (
  <div>
    <h1>Count: {count}</h1>
    <button onClick={addOne}>+1</button>
  </div>
);
