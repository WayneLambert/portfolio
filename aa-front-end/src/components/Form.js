import React from 'react';
import { Form,Input,Button } from 'antd';
import axios from 'axios';

const FormItem = Form.Item;

class PostOrPutForm extends React.Component {

  styles = {
    height: 20,
    width: 600,
  };

  handleFormSubmit = (event,requestMethod,postID) => {
    event.preventDefault();
    const title = event.target.elements.title.value
    const content = event.target.elements.content.value

    // eslint-disable-next-line default-case
    switch (requestMethod) {
      case 'post':
        return axios.post('http://localhost:8000/api/blog/',{
          title: title,
          content: content,
        })
          .then(res => console.log(res))
          .catch(error => console.log(error));
      // eslint-disable-next-line no-fallthrough
      case 'put':
        return axios.put(`http://localhost:8000/api/blog/${postID}/`,{
          title: title,
          content: content,
        })
          .then(res => console.log(res))
          .catch(error => console.log(error));
    }
  }

  renderTags() {
    if (this.handleFormSubmit.requestMethod === 'post')
      return (
        <Form id="post-form" onSubmit={(event) => this.handleFormSubmit(
          event,
          this.props.requestMethod,
          this.props.postID
        )}>
          <h5 requestType="post">Create a new post...</h5>
          <FormItem style={this.styles}>
            <Input name="title" placeholder="Enter title here..." />
          </FormItem>
          <FormItem style={this.styles}>
            <Input name="content" placeholder="Enter post content here..." />
          </FormItem>
          <FormItem>
            <Button type="primary" htmlType="submit">Post</Button>
          </FormItem>
        </Form>
      )
      return (
        <Form id="put-form" onSubmit={(event) => this.handleFormSubmit(
          event,
          this.props.requestMethod,
          this.props.postID
        )}>
          <h5 requestType="put">Update the post...</h5>
          <FormItem style={this.styles}>
            <Input name="title" placeholder="Enter title here..." />
          </FormItem>
          <FormItem style={this.styles}>
            <Input name="content" placeholder="Update post content ..." />
          </FormItem>
          <FormItem>
            <Button type="primary" htmlType="submit">Put</Button>
          </FormItem>
        </Form>
      )
  }

  render() { return this.renderTags() }
}

export default PostOrPutForm;
