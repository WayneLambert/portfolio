import React,{ Component } from 'react';

class Counter extends Component {
  state = {
    count: 0
  };

  render() {
    return (
      <div>
        <span style={{ fontSize: 20 }} className="badge badge-primary m-2">
          {'Literal'}
        </span>
        <button className="btn btn-secondary btn-sm">Increment</button>
      </div>
    );
  }
}

export default Counter;
