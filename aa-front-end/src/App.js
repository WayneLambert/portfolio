import React,{ Component } from 'react';
import { BrowserRouter as Router } from 'react-router-dom';
import BaseRouter from './routes';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'antd/dist/antd.css';
import CustomLayout from './containers/Layout';


class App extends Component {
  state = {
    posts: []
  }

  render() {
    return (
      <div className="App">
        <Router>
          <CustomLayout>
            <BaseRouter />
          </CustomLayout>
        </Router>
      </div>
    )
  }
};

export default App;
