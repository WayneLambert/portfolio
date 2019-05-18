import React from 'react';
import { render } from 'react-dom';
import { Provider } from 'react-redux';
import CounterComponent from '../containers/CounterComponent';
import store from '../store';
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
                  <Provider store={store}>
                    <CounterComponent />
                  </Provider>
                </React.Fragment>
            </div>
          </List.Item>
        </div>
      )}
    />
  )
}

export default Posts;