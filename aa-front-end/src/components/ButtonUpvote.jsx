import React from 'react';

const ButtonUpvote = (props) => {
  return (
    <React.Fragment>
      <button onClick={props.action} >{props.buttonTitle}</button>
    </React.Fragment>
  )
}

export default ButtonUpvote;