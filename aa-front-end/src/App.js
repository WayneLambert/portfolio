import React, { Component } from 'react'
import axios from 'axios'

class App extends Component {
	state = {
		posts: []
	}

	componentDidMount () {
		this.getPosts()
	}

	getPosts () {
		axios
			.get('http://localhost:8000/api/blog/')
			.then((res) => {
				this.setState({
					posts: res.data
				})
			})
			.catch((err) => {
				console.log(err)
			})
	}

	render () {
		return (
			<div id="items" className="posts">
				{this.state.posts.map((item) => (
          < div key = { item.id } >
            <h3 className="item_title"> {item.title} </h3>
            <h5 className="item_author"> {item.author} </h5>
            <h5 className="item_publish_date"> {item.publish_date} </h5>
            <h5 className="item_updated_date"> {item.updated_date} </h5>
            <span className="item_body"> {item.body} </span>
					</div>
				))}
			</div>
		)
	}
}

export default App
