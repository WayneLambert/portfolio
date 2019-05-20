import React,{ Component } from 'react';
import axios from 'axios';
import UpvoteButton from '../components/ButtonUpvote';
import DownvoteButton from '../components/ButtonDownvote';
import { connect } from 'react-redux';
import { incrementCount,decrementCount } from '../actions/index';

class CounterComponent extends Component {

  constructor(props) {
    super(props);
    this.state = {
      posts: {},
      upvotes: this.downvotes,
      downvotes: this.props.downvotes,
    };
  }

  async incCount() {
    const postID = this.props.match.params.postID
    const upvotes = this.state.upvotes
    const { data } = await axios.put(`http://localhost:8000/api/blog/${postID}`,upvotes)
    const currentState = this.state.posts
    this.setState({ posts: currentState.concat(upvotes) })
  }

  handleBtnActionIncrement = () => {
    this.props.onIncrementClick(this.props.count)
  }
  
  handleBtnActionDecrement = () => {
    this.props.onDecrementClick(this.props.count)
  }

  render() {
    const { count } = this.props
    return (
      <div>
        <span>Helpfulness Rating: {count}     </span>
        <UpvoteButton
          buttonTitle="+"
          action={this.handleBtnActionIncrement}
        />
        <DownvoteButton
          buttonTitle="-"
          action={this.handleBtnActionDecrement}
        />
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