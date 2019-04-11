import React, { Component } from 'react';
import axios from 'axios';

class App extends Component {
  state = {
    posts: []
  };

  componentDidMount() {
    this.getPosts();
  }

  getPosts() {
    axios
      .get('http://localhost:8000/api/blog/')
      .then(res => {
        this.setState({ posts: res.data });
      })
      .catch(err => {
        console.log(err);
      });
  }

  render() {
    return (
      <div>
        <div>
          {this.state.posts.map(item => (
            <div key={item.id}>
              <h3>{item.title}</h3>
              <h4>{item.body}</h4>
              <h4>{item.author}</h4>
              <h6>{item.publish_date}</h6>
              <h6>{item.updated_date}</h6>
            </div>
          ))}
        </div>
      </div>
    );
  }
}

export default App;
