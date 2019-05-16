import React from 'react';
import { Layout, Menu } from 'antd';

const { Header, Content, Footer } = Layout;
const yearOfToday = new Date().getFullYear()

const CustomLayout = (props) => {
    return(
        <Layout className="layout">
          <Header style={{ position: 'fixed',zIndex: 1,height: '0px',width: '100%' }}>
              <div className="logo" />
              <Menu
                theme="dark"
                mode="horizontal"
                defaultSelectedKeys={Menu.Item.key}
                style={{ lineHeight: '50px' }}
                textAlign="right"
              >
                <Menu.Item key="1"><a href="/">Home</a></Menu.Item>
                <Menu.Item key="2"><a href="/blog">Blog</a></Menu.Item>
                <Menu.Item key="3"><a href="/cv">CV</a></Menu.Item>
              </Menu>
          </Header>
          <Content className="content" style={{ padding: '0 50px',marginTop: 45 }}>
            <div style={{ background: '#fff',padding: 24,minHeight: 800 }}>
                {props.children}
            </div>
          </Content>
          <Footer className="footer" style={{ textAlign: 'left' }}>
            &copy; <span id="year">{yearOfToday} waynelambert.dev</span>
          </Footer>
        </Layout>
    );
}

export default CustomLayout;
