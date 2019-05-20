import React,{ Component } from 'react';
import { BrowserRouter as Router } from 'react-router-dom';
import BaseRouter from './routes';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'antd/dist/antd.css';
import SiteLayout from './containers/SiteLayout';


class App extends Component {
  state = {
    posts: []
  }

  render() {
    return (
      <div className="App">
        <Router>
          <SiteLayout>
            <BaseRouter />
          </SiteLayout>
        </Router>
      </div>
    )
  }
};

export default App;
