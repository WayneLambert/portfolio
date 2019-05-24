const initialState = {
  count: 0,
}

function CounterReducer(state = initialState,action) {
  switch (action.type) {
    case "ADD_ONE": {
      return { ...state,...action }
    }
    case "MINUS_ONE": {
      return { ...state,...action }
    }
    default:
      return state
  }
}

export default CounterReducer;
