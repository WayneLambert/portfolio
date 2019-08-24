import React from 'react';
import { Route, BrowserRouter as Router } from 'react-router-dom';
import PostList from './containers/PostListView';
import PostFormView from './containers/PostForm';
import PostDetail from './containers/PostDetailView';
import PageNotFound from './components/PageNotFound';

// FIXME: Routes do not work
const BaseRouter = () => (
  <Router>
    <Route exact path='/react-blog' component={PostList} />
    <Route exact path='/react-blog/post/:postID' component={PostDetail} />
    <Route exact path='/react-blog/post' component={PostFormView} />
    <Route component={PageNotFound} />
  </Router>
);

export default BaseRouter;
