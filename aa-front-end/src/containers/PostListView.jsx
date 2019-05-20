import React from 'react';
import axios from 'axios';
import Posts from '../components/PostView';

const title = 'Python PEPs';
const subtitle = 'Accepted PEPs (accepted; may not be implemented yet)';

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
        <h4>{title}</h4>
        <h6>{subtitle}</h6>
        <Posts data={this.state.posts} />     
      </div>
    )
  }
}

export default PostList;
