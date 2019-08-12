import React from 'react';
import { Layout } from 'antd';
import PostList from '../containers/PostListView';
import '../custom.css';

const { Content } = Layout;

const SiteContent = (props) => {
  return (
    <Content className="site-content">
      <PostList />
    </Content>
  )
}

export default SiteContent;
