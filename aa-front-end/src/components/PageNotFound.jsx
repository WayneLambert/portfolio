import React from 'react';


class PageNotFoundView extends React.Component {
  render() {
    return (
      <div>
        <span>
          <h5 className="error-message">The page that you have tried to navigate to does not exist.</h5>
        </span>
      </div>
    )
  }
}

export default PageNotFoundView;
