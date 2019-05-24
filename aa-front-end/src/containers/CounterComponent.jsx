import React, { Component } from 'react';
import axios from 'axios';
import UpvoteButton from '../components/ButtonUpvote';
import DownvoteButton from '../components/ButtonDownvote';
import { connect } from 'react-redux';
import { addOne, minusOne } from '../actions/index';

class CounterComponent extends Component {

  state = {
    posts: [],
    upvotes: this.props.value,
    downvotes: this.props.value,
  };

  handleAddUpvote = async post => {
    this.setState({ upvotes: this.state.upvotes + 1 });
    await axios.patch('http://localhost:8000/api/blog{post.id}', { upvotes: post.upvotes })
    
    const posts = [...this.state.posts]
    const index = posts.indexOf(post);
    posts[index] = { ...post };
  };

  handleAddDownvote = event => {
    this.props.onMinusOne(this.props.count)
  }

  render() {
    return (
      <div>
        <span>Helpfulness Rating: {this.state.upvotes}     </span>
        <UpvoteButton
          buttonTitle="+"
          action={this.handleAddUpvote}
        />
        <DownvoteButton
          buttonTitle="-"
          action={this.handleAddDownvote}
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
    onAddOne: (count) => {
      dispatch(addOne(count))
    },
    onMinusOne: (count) => {
      if (count !== 0)
        dispatch(minusOne(count))
    }
  }
}

// export default connect(mapStateToProps,mapDispatchToProps)(CounterComponent);
export default CounterComponent;