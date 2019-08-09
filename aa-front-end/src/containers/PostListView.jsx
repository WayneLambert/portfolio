import React, { Component } from 'react';
import axios from 'axios';
import Posts from '../components/PostView';

const title = 'Blog Posts';
const subtitle = 'Blog posts in development of the React version of the blog';

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
        <h4>{title}</h4>
        <h6>{subtitle}</h6>
        <Posts data={this.state.posts} />     
      </div>
    )
  }
}

export default PostList;
