import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { createStore } from 'redux';
import Posts from './PostListView';

function reducer(state = 0,action) {
  return state + 1;
}

function main() {
  window.removeEventListener('load',main,false);
  const store = createStore(reducer);
  console.log(store.getState());
  ReactDOM.render(
    <Provider store={store}>
      <Posts />
    </Provider>
  );
}

window.addEventListener('load',main,false);
