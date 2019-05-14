import React from 'react';
import Posts from '../components/Post';
import axios from 'axios';

class PostList extends React.Component {
  state = {
    posts: []
  }
  
  componentDidMount() {
    axios.get('http://localhost:8000/api/blog')
      .then(res => {
        this.setState({
          posts: res.data
        });
        console.log(res.data);
      })
  }

  render() {
    return (
      <Posts data={this.state.posts} />
    )
  }
}

export default PostList;
