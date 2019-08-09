import React, { Fragment } from 'react';
import SiteHeader from './SiteHeader';
import SiteContent from './SiteContent';
import SiteFooter from './SiteFooter';

const SiteLayout = (props) => {
    return(
      <Fragment>
        <SiteHeader />
        <SiteContent />
        <SiteFooter />
      </Fragment>
    );
}

export default SiteLayout;
