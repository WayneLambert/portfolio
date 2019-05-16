import React from 'react';
import { Route } from 'react-router-dom';
import PostList from './containers/PostListView';
import PostDetail from './containers/PostDetailView';
import myCounter from './containers/Counter';

const BaseRouter = () => (
  <div>
    <Route exact path='/' component={PostList} />
    <Route exact path='/:postID' component={PostDetail} />
    {/**
    The following paths are all purposefully incorrect. They append to the back-ends API endpoint.
    These are just in place so that we can reuse the same React app to test other React and UI functionality.
    */}
    <Route exact path='/counter' component={myCounter} />
  </div>
);

export default BaseRouter;
