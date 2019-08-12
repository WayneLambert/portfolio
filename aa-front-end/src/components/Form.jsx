import React, { Component } from 'react';
import { Form,Input,Button } from 'antd';
import axios from 'axios';

const FormItem = Form.Item;
const blogAPIEndPointURL = process.env.DEV_API_URL

class PostForm extends Component {

  styles = {
    height: 20,
    width: 600,
  };

  handleFormSubmit = async (event,requestType,postID) => {
    event.preventDefault();
    const title = event.target.elements.title.value
    const content = event.target.elements.content.value

    try {
      const res = await axios.post(blogAPIEndPointURL,{
        title: title,
        content: content,
      });
      return console.log(res);
    }
    catch (error) {
      return console.log(error);
    }
  }

  renderTags() {
    return (
      <Form id="post-form" onSubmit={(event) => this.handleFormSubmit(
        event,
        this.props.requestType,
        this.props.postID
      )}>
        <h6 requestType="post">Create a new post...</h6>
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
  }

  render() { return this.renderTags() }
}

export default PostForm;
