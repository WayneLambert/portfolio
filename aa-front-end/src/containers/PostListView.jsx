import React, { Component } from 'react';
import axios from 'axios';
import Posts from './../components/PostView';

class PostList extends Component {
  state = {
    posts: []
  }

  componentDidMount() {
    axios.get('http://localhost:8001/api/blog/posts/')
      .then(response => {
        this.setState({
          posts: response.data
        });
        console.log(response.data);
      })
  }

  render() {
    return (
      <div>
        <Posts data={this.state.posts} />
      </div>
    )
  }
}

export default PostList;
