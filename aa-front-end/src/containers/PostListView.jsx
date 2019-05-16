import React from 'react';
import axios from 'axios';
import Posts from '../components/Post';

class PostList extends React.Component {
  state = {
    posts: []
  }

  // const app => {
  //   title: 'Blog posts about Python PEPs',
  //   subtitle: 'Accepted PEPs (accepted; may not be implemented yet)'
  // };
  
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
