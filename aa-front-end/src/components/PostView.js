import React from 'react';
import { List,Icon } from 'antd';

const IconText = ({ type,text }) => (
  <span>
    <Icon type={type} style={{ marginRight: 6 }} />
    {text}
  </span>
);

const Posts = (props) => {      
  return (
    <List
      itemLayout="vertical"
      size="large"
      pagination={{
        onChange: page => {
          console.log(page);
        },
        pageSize: 3,
      }}
      dataSource={props.data}
      renderItem={item => (
        <React.Fragment>        
          <List.Item key={item.title} />
          <List.Item.Meta
            title={<a href={`/blog/${item.id}`}>{item.title}</a>}
            body={item.body}
          />
          <div className="body">{item.body}</div>
          <List.Item>
            <div>
              Publish Date: {item.publish_date}<br />
              Updated Date: {item.updated_date}<br />
              <br />
                <React.Fragment>                
                  <IconText type="caret-up" text="1" />
                  <IconText type="caret-down" text="1" />
                </React.Fragment>
            </div>
          </List.Item>
        </React.Fragment>
      )}
    />
  )
}

export default Posts;
