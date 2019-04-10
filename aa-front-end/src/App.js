import React, { Component } from 'react';
import axios from 'axios';

class App extends Component {
  state = {
    books: []
  };

  componentDidMount() {
    this.getBooks();
  }

  getBooks() {
    axios
      .get('http://localhost:8000/api/books/')
      .then(res => {
        this.setState({ books: res.data });
      })
      .catch(err => {
        console.log(err);
      });
  }

  render() {
    return (
      <div>
        <div>
          {this.state.books.map(item => (
            <div key={item.id}>
              <h1>{item.title}</h1>
              <h2>{item.subtitle}</h2>
              <h4>{item.title}</h4>
              <h6>{item.title}</h6>
            </div>
          ))}
        </div>
      </div>
    );
  }
}

export default App;
