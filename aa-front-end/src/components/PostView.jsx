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
        pageSize: 3,
      }}
      dataSource={props.data}

      renderItem={item => (
        <div>
          <div className="title">
            <List.Item key={item.title} />
            <List.Item.Meta
              title={<a href={`/blog/posts/${item.id}`}>{item.title}</a>}
              />
          </div>
          <List.Item>
            <div className='content'>
              {renderHTML(item.content)}
            </div>
            Categories: {item.categories}<br />
            Author: {item.author_first_name} {item.author_last_name}<br />
            Publish Date: {item.publish_date}<br />
            Updated Date: {item.updated_date}<br />
            Image URL: {item.image}<br />
            <br />
          </List.Item>
        </div>
      )}
    />
  )
}

export default Posts;
