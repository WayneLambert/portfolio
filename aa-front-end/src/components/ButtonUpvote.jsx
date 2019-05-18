import React from 'react';

const ButtonUpvote = (props) => {
  return (
    <React.Fragment>
      <Button variant="primary" size="xs"
      onClick={props.action} >{props.buttonTitle}</Button>
    </React.Fragment>
  )
}

export default ButtonUpvote;