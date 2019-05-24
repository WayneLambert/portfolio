import React from 'react';
import { Route, Switch } from 'react-router-dom';
import HomeView from './components/Home';
import PostList from './containers/PostListView';
import PostFormView from './containers/PostForm';
import PostDetail from './containers/PostDetailView';
import PageNotFound from './components/PageNotFound';

const BaseRouter = () => (
  <Switch>
    <Route exact path='/' component={HomeView} />
    <Route exact path='/blog' component={PostList} />
    <Route exact path='/blog/post' component={PostFormView} />
    <Route exact path='/blog/:postID' component={PostDetail} />
    <Route component={PageNotFound} />
  </Switch>
);

export default BaseRouter;