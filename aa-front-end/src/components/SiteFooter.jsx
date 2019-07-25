import React,{ Component } from 'react';
import { Layout } from 'antd';
const { Footer } = Layout;

const yearOfToday = new Date().getFullYear()

class SiteFooter extends Component {
  render() { 
    return (
      <Footer className="footer" style={{ textAlign: 'left' }}>
        &copy; <span id="year">{yearOfToday} Copyright | waynelambert.co.uk</span>
      </Footer>
    );
  }
}
 
export default SiteFooter;