import React from 'react';

const ButtonDownvote = (props) => {
  return (
    <React.Fragment>
      <button onClick={props.action} >{props.buttonTitle}</button>
    </React.Fragment>
  )
}

export default ButtonDownvote;
