export const addOne = count => {
  const num = count + 1
  return {
    type: 'ADD_ONE',
    count: num
  }
}

export const minusOne = count => {
  const num = count - 1
  return {
    type: 'MINUS_ONE',
    count: num
  }
}
