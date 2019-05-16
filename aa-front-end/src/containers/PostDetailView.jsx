import React from 'react';
import axios from 'axios';
import { Card } from 'antd';
import PostForm from './PostForm';

class PostDetail extends React.Component {
  state = {
    post: {}
  }
  
  componentDidMount() {
    const postID = this.props.match.params.postID;
    axios.get(`http://localhost:8000/api/blog/${postID}`)
      .then(res => {
        this.setState({
          post: res.data
        });
      })
  }

  render() {
    return (
      <Card title={this.state.post.title}>
        <p>{this.state.post.body}</p>
        <h3>Update the post...</h3>
        <PostForm requestType="put" postID={this.props.match.params.postID}/>
      </Card>
    )
  }
}

export default PostDetail;
