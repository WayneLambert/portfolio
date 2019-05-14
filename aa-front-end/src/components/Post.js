import React from 'react';
import { List, Avatar, Icon } from 'antd';

const IconText = ({ type, text }) => (
  <span>
    <Icon type={type} style={{ marginRight: 8 }} />
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
          <List.Item
            key={item.title}
            actions={[
              <IconText type="star-o" text="156" />,
              <IconText type="like-o" text="156" />,
              <IconText type="message" text="2" />,
            ]}

            extra={
              <img width={272} alt="logo" src={item.image} />
            }
          >
            <List.Item.Meta
              title={<a href={`/${item.id}`}>{item.title}</a>}
              body={item.body}
              publish_date={item.publish_date}
              updated_date={item.updated_date}
              image={<Avatar src={item.image} />}
            />
            <div className="body">{item.body}</div>
            <div>
              <br />
              <p>
                Publish Date: {item.publish_date}<br />
                Updated Date: {item.updated_date}
              </p>
            </div>
          </List.Item>
        )}
      />
  )
}

export default Posts;
