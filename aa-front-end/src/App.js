import React,{ Component } from 'react';
import { BrowserRouter as Router } from 'react-router-dom';
import BaseRouter from './routes';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'antd/dist/antd.css';
import CustomLayout from './containers/Layout';

const app = {
  title: 'Blog posts about Python PEPs',
  subtitle: 'Accepted PEPs (accepted; may not be implemented yet)'
};

class App extends Component {
  state = {
    posts: []
  }

  render() {
    return (
      <div className="App">
        <Router>
          <CustomLayout>
            <h3>{app.title}</h3>
            <h6>{app.subtitle}</h6>
            <BaseRouter />
          </CustomLayout>
        </Router>
      </div>
    )
  }
};

export default App;
