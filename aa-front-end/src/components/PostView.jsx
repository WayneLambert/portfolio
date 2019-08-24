import React from 'react';
import { List } from 'antd';
import renderHTML from 'react-render-html';

const Posts = (props) => {
  return (
    <List
      itemLayout="vertical"
      size="small"
      pagination={{
        onChange: page => {
          console.log(page);
        },
        pageSize: 1,
      }}
      dataSource={props.data}

      renderItem={item => (
        <div>
          <List.Item>
            <a className="post-title" href={`/react/blog/posts/${item.id}`}>{item.title}</a>
            <div className="post-image"> 
              <img src={item.image} alt="" height="100px" width="100px"/>
            </div>
            <div className='content'>{renderHTML(item.content)}</div>
            <li><b>Author: </b> {item.author_first_name} {item.author_last_name}</li>
            <li><b>Categories: </b> {item.categories}</li>
            <li><b>Published: </b> {item.publish_date}</li>
            <li><b>Updated: </b> {item.updated_date}</li>
          </List.Item>
        </div>
      )}
    />
  )
}

export default Posts;
