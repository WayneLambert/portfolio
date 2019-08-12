import React, { Component } from 'react';
import { PageHeader, Menu } from 'antd';

class SiteHeader extends Component {
  render() {
    return (
    <PageHeader>
      <Menu theme="dark" mode="horizontal" defaultSelectedKeys={Menu.Item.key}>
        <Menu.Item key="1"><a href="/">Home</a></Menu.Item>
        <Menu.Item key="2"><a href="/blog">Blog</a></Menu.Item>
      </Menu>
    </PageHeader>
    )
  }
}

export default SiteHeader;
