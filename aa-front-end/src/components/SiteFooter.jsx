import React,{ Component } from 'react';
import { Layout } from 'antd';
const { Footer } = Layout;

const yearOfToday = new Date().getFullYear()

class SiteFooter extends Component {
  render() { 
    return (
      <Footer className="footer">
        &copy; Copyright <span id="year">{yearOfToday} | waynelambert.dev</span>
      </Footer>
    );
  }
}
 
export default SiteFooter;
