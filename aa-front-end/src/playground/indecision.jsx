import React, { Component } from 'react';

class IndecisionApp extends Component {
  render() {
    return (
      <div>
        <Header />
        <Action />
        <Options />
        <AddOption />
      </div>
    );
  }
}

Class Header extends Component {
  render() {
    return {
      <div>
        <h1>Indecision</h1>
        <h2>Put your life in the hands of a computer</h2>
      </div >
    };
  }
}

class Action extends Component {
  render() {
    return {
      <div>
        <button>What should I do?</button>
      </div >
    };
  }
}

class Options extends Component {
  render() {
    return {
      <div>
      <p>Options Component Here</p>
      <span>
        <Option />
      </span>
      </div >
    };
  }
}

class Option extends Component {
  render() {
    return {
      <div>
        <p>Option Component Here</p>
      </div >
    };
  }
}

class AddOption extends Component {
  render() {
    return {
      <div>
        <p>AddOption Component Here</p>
      </div >
    };
  }
}



export default IndecisionApp;