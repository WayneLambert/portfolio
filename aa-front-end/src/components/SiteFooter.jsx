import React,{ Component } from 'react';
import { Layout } from 'antd';
const { Footer } = Layout;

const yearOfToday = new Date().getFullYear()

class SiteFooter extends Component {
  render() {
    return (
      <Footer className="site-footer">
        <span className="copyright-notice" id="year">&copy; {yearOfToday} waynelambert.dev</span>
        <span className="footer-links">Privacy</span>
      </Footer>
    );
  }
}

export default SiteFooter;
