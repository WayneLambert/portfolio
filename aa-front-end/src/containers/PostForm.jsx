import React from 'react';
import axios from 'axios';
import PostForm from '../components/Form';

const blogAPIEndPointURL = 'http://localhost:8000/api/blog/'

class PostFormView extends React.Component {
  state = {
    post: []
  }

  handleFormSubmit = (event,requestType,postID) => {
    event.preventDefault();
    const title = event.target.elements.title.value;
    const content = event.target.elements.content.value;

    // eslint-disable-next-line default-case
    switch (requestType) {
      case 'post':
        axios.post(blogAPIEndPointURL, {
          title: title,
          content: content,
        })
        .then(res => console.log(res));
      // eslint-disable-next-line no-fallthrough
      case 'put':
        axios.put(blogAPIEndPointURL + postID, {
          title: title,
          content: content,
        })
        .then(res => console.log(res));
    }
  }

  componentDidMount() {
    axios.get(blogAPIEndPointURL)
      .then(res => {
        this.setState({
          post: res.data
        });
        console.log(res.data);
      })
  }

  render() {
    return (
      <div>
        <PostForm requestType="post" postID={null}/>
        <PostForm requestType="put" postID={this.postID}/>
      </div>
    )
  }
}

export default PostFormView;
