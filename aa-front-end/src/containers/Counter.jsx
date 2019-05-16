import React, { Component } from 'react';
import Counter from '../components/counter';

class myCounter extends Counter {
  state = {
    count: 0,
    imageURL: 'https://picsum.photos/100'
  };

  styles = {
    fontSize: 10,
    fontWeight: 'normal',
  }

  render() {
    return (
      <div>
        <img className="img-circle img-thumbnail m-2" src={this.state.imageURL} alt="random alt text" />
        <button onClick={this.handleIncrement} className="btn btn-dark btn-sm m-1">Increment</button>
        <button onClick={this.handleDecrement} className="btn btn-light btn-sm m-1">Decrement</button>
        <div>
          <span className={this.getBadgeClasses()} style={this.styles}>The current number is {this.state.count}</span>
        </div>
      </div>
      );
    };

  getBadgeClasses() {
    let badgeClass = "badge m-2 badge-";
    badgeClass += this.state.count === 0 ? "warning" : "primary";
    return badgeClass;
  }

  handleIncrement = () => {
    this.setState({ count: this.state.count + 1 })
  }
  
  handleDecrement = () => {
    this.setState({ count: this.state.count - 1 })
  }
}

export default myCounter;
