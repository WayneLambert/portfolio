import React from 'react';
import axios from 'axios';
import Posts from '../components/PostView';

// const app => {
//   title: 'Blog posts about Python PEPs',
//   subtitle: 'Accepted PEPs (accepted; may not be implemented yet)'
// };

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
      <div>
        <h4>Python PEPs</h4>
        <h6>Accepted PEPs (may not be implemented yet)</h6>
        <Posts data={this.state.posts} />     
      </div>
    )
  }
}

export default PostList;
