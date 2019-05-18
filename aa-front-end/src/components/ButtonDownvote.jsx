import React from 'react';

const ButtonDownvote = (props) => {
  return (
    <button type="button" class="btn btn-danger btn-xs" onClick={props.action} >{props.buttonTitle}</button>
  )
}

export default ButtonDownvote;
