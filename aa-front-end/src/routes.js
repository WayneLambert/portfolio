import React from 'react';
import { Route } from 'react-router-dom';
import PostList from './containers/PostListView';
import PostDetail from './containers/PostDetailView';

const BaseRouter = () => (
  <div>
    <Route exact path='/' component={PostList} />
    <Route exact path='/:postID' component={PostDetail} />
  </div>
);

export default BaseRouter;
