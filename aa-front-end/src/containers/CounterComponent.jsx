import React, {Component} from 'react';
import UpvoteButton from '../components/ButtonUpvote';
import DownvoteButton from '../components/ButtonDownvote';
import { connect } from 'react-redux';
import { incrementCount,decrementCount } from '../actions/index';

class CounterComponent extends Component {

  handleBtnActionIncrement = () => {
    this.props.onIncrementClick(this.props.count)
  }
  
  handleBtnActionDecrement = () => {
    this.props.onDecrementClick(this.props.count)
  }

  render() {
    const {count} = this.props
    return (
      <div>
        <span>Helpfulness Rating: {count}</span>
        <UpvoteButton action={this.handleBtnActionIncrement} buttonTitle="+" />
        <DownvoteButton action={this.handleBtnActionDecrement} buttonTitle="-" />
      </div>
    )
  }
}


const mapStateToProps = (state) => {
  return {
    count: state.counter.count
  }
}

const mapDispatchToProps = (dispatch) => {
  return {
    onIncrementClick: (count) => {
      dispatch(incrementCount(count))
    },
    onDecrementClick: (count) => {
      if (count !== 0)
        dispatch(decrementCount(count))
    }
  }
}

export default connect(mapStateToProps,mapDispatchToProps)(CounterComponent);