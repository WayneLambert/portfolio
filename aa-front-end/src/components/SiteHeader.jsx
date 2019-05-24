import React, { Component } from 'react';
import { PageHeader, Menu } from 'antd';

class SiteHeader extends Component {
  render() {
    return (
    <PageHeader style={{ position: 'fixed',zIndex: 1,height: '0px',width: '100%' }}>
      <div className="logo" />
      <Menu
        theme="dark"
        mode="horizontal"
        defaultSelectedKeys={Menu.Item.key}
        style={{ lineHeight: '50px' }}
      >
        <Menu.Item key="1"><a href="/">Home</a></Menu.Item>
        <Menu.Item key="2"><a href="/blog">Blog</a></Menu.Item>
        <Menu.Item key="3"><a href="/cv">CV</a></Menu.Item>
      </Menu>
    </PageHeader>
    )
  }
}

export default SiteHeader;