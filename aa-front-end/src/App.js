import React,{ Component } from 'react'
import { BrowserRouter as Router } from 'react-router-dom';
import BaseRouter from './routes';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'antd/dist/antd.css';
import axios from 'axios'
import Posts from './components/Post';
import CustomLayout from './containers/Layout';

const app = {
  title: 'Blog posts about Python PEPs',
  subtitle: 'Accepted PEPs (accepted; may not be implemented yet)'
};

const onFormSubmit = (e) => {
  e.preventDefault();
  console.log('form submitted');
};

class App extends Component {
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
      <Router>
        <CustomLayout>
          <h3>{app.title}</h3>
          <h5>{app.subtitle}</h5>
          <Posts data={this.state.posts} />
        </CustomLayout>
      </Router>
    )
  }
};

export default App;
