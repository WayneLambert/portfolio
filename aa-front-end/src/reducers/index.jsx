import { combineReducers } from 'redux';
import CounterReducer from '../reducers/CounterReducer';

export default combineReducers({
  counter: CounterReducer,
})
