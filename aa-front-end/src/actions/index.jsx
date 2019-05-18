export const incrementCount = count => {
  const num = count + 1
  return {
    type: 'INCREMENT_COUNT',
    count: num
  }
}

export const decrementCount = count => {
  const num = count - 1
  return {
    type: 'DECREMENT_COUNT',
    count: num
  }
}
