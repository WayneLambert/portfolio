import React, { Component } from 'react';
import axios from 'axios';
import { Card } from 'antd';
import CounterComponent from '../containers/CounterComponent';

const blogAPIEndPointURL = process.env.DEV_API_URL

class PostDetail extends Component {

  state = {
    post: {},
  }

  componentDidMount() {
    const postID = this.props.match.params.postID;
    axios.get(`${blogAPIEndPointURL}${postID}`)
      .then(response => {
        this.setState({
          post: response.data
        });
      })
  }

  render() {
    return (
      <Card title={this.state.post.title}>
        <p>{this.state.post.body}</p>
        Publish Date: {this.state.post.publish_date}<br />
        Updated Date: {this.state.post.updated_date}<br />
        <br />
        <React.Fragment>
          <CounterComponent />
        </React.Fragment>
      </Card>
    )
  }
}

export default PostDetail;
