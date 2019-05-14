import React from 'react';
import { Layout,Menu,Breadcrumb } from 'antd';
import { Link } from 'react-router-dom';

const { Header, Content, Footer } = Layout;

const CustomLayout = (props) => {
    return(
        <Layout className="layout">
            <Header style={{ position: 'fixed',zIndex: 1,width: '100%' }}>
                <div className="logo" />
                <Menu
                    theme="dark"
                    mode="horizontal"
                    defaultSelectedKeys={['2']}
                    style={{ lineHeight: '64px' }}
                >
                    <Menu.Item key="1">Django</Menu.Item>
                    <Menu.Item key="2">React</Menu.Item>
                    <Menu.Item key="3">CV</Menu.Item>
                </Menu>
            </Header>
            <Content style={{ padding: '0 50px',marginTop: 64 }}>
                <Breadcrumb style={{ margin: '16px 0' }}>
                    <Breadcrumb.Item><Link to="/">Home</Link></Breadcrumb.Item>
                    <Breadcrumb.Item><Link>List</Link></Breadcrumb.Item>
                    <Breadcrumb.Item><Link>App</Link></Breadcrumb.Item>
                </Breadcrumb>
                <div style={{ background: '#fff',padding: 24,minHeight: 380 }}>
                    {props.children}
                </div>
            </Content>
            <Footer style={{ textAlign: 'left' }}>waynelambert.dev</Footer>
        </Layout>
    );
}

export default CustomLayout;
