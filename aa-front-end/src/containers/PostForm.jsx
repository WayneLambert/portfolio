import React from 'react';
import axios from 'axios';
import PostForm from '../components/Form';

const blogAPIEndPointURL = 'http://localhost:8000/api/blog/'

class PostFormView extends React.Component {
  state = {
    post: []
  }

  handleFormSubmit = (event,requestType,postID) => {
    const title = event.target.elements.title.value;
    const content = event.target.elements.content.value;

      axios.post(blogAPIEndPointURL, {
        title: title,
        content: content,
      })
      .then(response => console.log(response));
  }

  componentDidMount() {
    axios.get(blogAPIEndPointURL)
      .then(response => {
        this.setState({ 
          post: response.data
        });
        console.log(response.data);
      })
  }

  renderTags() {
    return <PostForm onSubmit={this.handleSubmit} />;
  }

  render() {
    return (
      <div>
        { this.renderTags() }
      </div>
    )
  }
}

export default PostFormView;