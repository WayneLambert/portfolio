import React from 'react';
import { Layout } from 'antd';
import PostList from '../containers/PostListView';
const { Content } = Layout;

const SiteContent = (props) => {
  return (
    <Content className="content" style={{ padding: '80px 50px',marginTop: 0 }}>
      <div style={{ background: '#fff',padding: 24,minHeight: 800 }}>
        <PostList />
      </div>
    </Content>
  )
}

export default SiteContent;