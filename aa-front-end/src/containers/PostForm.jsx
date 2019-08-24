import React from 'react';
import axios from 'axios';
import PostForm from './../components/Form';


class PostFormView extends React.Component {
  state = {
    post: []
  }

  handleFormSubmit = (event,requestType,postID) => {
    const title = event.target.elements.title.value;
    const content = event.target.elements.content.value;

      axios.post(process.env.REACT_APP_API_ENDPOINT, {
        title: title,
        content: content,
      })
      .then(res => console.log(res));
  }

  componentDidMount() {
    axios.get(process.env.REACT_APP_API_ENDPOINT)
      .then(res => {
        this.setState({ 
          post: res.data
        });
        console.log(res.data);
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
