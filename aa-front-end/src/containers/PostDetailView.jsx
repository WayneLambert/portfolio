import React, { Component } from 'react';
import axios from 'axios';
import { Provider } from 'react-redux';
import { Card } from 'antd';
import CounterComponent from '../containers/CounterComponent';
import store from '../store';

class PostDetail extends Component {

  state = {
    post: {},
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
        Publish Date: {this.state.post.publish_date}<br />
        Updated Date: {this.state.post.updated_date}<br />
        <br />
        <React.Fragment>                
          <Provider store={store}>
            <CounterComponent />
          </Provider>
        </React.Fragment>
      </Card>
    )
  }
}

export default PostDetail;
