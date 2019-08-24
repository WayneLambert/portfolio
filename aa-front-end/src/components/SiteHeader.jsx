import React, { Component } from 'react';
import { PageHeader,Menu, Icon } from 'antd';


class SiteHeader extends Component {
  render() {
    return (
    <PageHeader>
      <Menu theme="dark" mode="horizontal" defaultSelectedKeys={Menu.Item.key}>
        <Menu.Item key="1">
          <Icon type="home" id="btn-home" />
        </Menu.Item>
        <Menu.Item key="2">
          <a href="/react-blog">Blog</a>
        </Menu.Item>
      </Menu>
    </PageHeader>
    )
  }
}

export default SiteHeader;
