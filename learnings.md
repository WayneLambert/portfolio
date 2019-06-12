# Learnings

## Programmimg

- An 'asynchronous call' is something that will happen in the future.

## Django / Python

- Viewsets can be used to make code tidy in cases where each of the HTTP methods will be used. Blog posts makes a good use case for this as it is likely that you would want to be able to create, read, update and delete blog posts.

## React / JSX / JavaScript

- React is called _'React'_ because it reacts to state changes in the DOM
- React manages a virtual DOM which is reconciled against the Real DOM which is managed by the browser. Any React element that is different in the Virtual DOM is then refreshed in the Real DOM so that the two are always kept in sync and changes are inexpensive and lightweight. This gives responsive applications.
- React is a view library concerned with dealing with the 'V' in the MVC model.
- Every application is composed of a tree of components which produces a complex markup. A component is a piece of the user interface. Every application contains at least the root component.
- The Render() method is the only mandatory method within a React component. It describes what the UI should look like.
- If you do not want to stay with the default `create-react-app` build configuration when it comes to production, you can run the `npm run eject` command which enables for manual changes to the build.
- `React.Fragment` can be used in cases where you insert a div around some JSX elements that require an additional container for Babel to be able to compile it. If you use a standard `<div></div>` tag, then this may produce two div tags wrapping around the JSX elements when you inspect the elements in Chrome Developer tools. This mosty likely isn't the desired outcome.
- Code written inside of curly braces is regular JavaScript code
- React components don’t automatically bind _this_ to the instance. I have to explicitly use `.bind(this)` within the constructor lifecycle method. This will take the following format where the classMethodName is replaced with the name given to my class method.
  - `this.classMethodName. = this.classMethodName.bind(this);`
  - _Formik_ is a JavaScript library that enables better building of React forms. It is the equivalent of Crispy Forms for Django. It handles things such as formatting in addition to data validation.

### Components

- React components are small, reusable pieces of code that return a React element to be rendered to the page.
- Components are not aware of application state. If my webpage is only going to be used for displaying data, then make it a component.
- The component that **owns** a piece of the state should be the one **modifying** it.
- **Controlled Components**
  - An input form element whose value is controlled by React is called a controlled component.
  - When a user enters data into a controlled component, a change event handler is triggered and my code decides whether the input is valid (by re-rendering with the updated value).
  - If I do not re-render then the form element will remain unchanged.
- **Uncontrolled Components**
  - An uncontrolled component works like form elements do outside of React.
  - When a user inputs data into a form field (an input box, dropdown, etc) the updated information is reflected without React needing to do anything.
- In most cases, I should use controlled components.

### Containers

- Containers are very similar to components. The only difference is that containers are aware of application state. If my webpage needs to be aware of application state, then make it a container.
- This means that `props` is used to handle updates within the virtual DOM for a component whereas `state` is used to handle updates within the virtual DOM for a container.

### Vanilla JavaScript

- _Axios_ is a library used to read data from my back ends API endpoint
- The _Map_ function can be used to render a list of items as HTML elements/items. This is useful in any scenario where I need to render elements in a _for each_ scenario
- The notation += appends to an existing variable. This means that the variable should be _'let'_ rather than a _'const'_
- The operator _'?'_ reads as _'then'_ in a conditional statement
- The operator _':'_ reads as _'else'_ in a conditional statement
- _'\n'_ is the new line escape character in JavaScript
- Use the _'const'_ keyword over _'let'_. Only use _'let'_ when I need to reassign a variable.
- The equivalent of Python's f strings (string interpolation) in JavaScript is using `${var_name}` between backtick operators
- A _'promise'_ is a state that this temporarily 'pending' until an outcome is either _'resolved'_ or _'rejected'_. For example, this might be a call to an external API. If the API is programmed correctly and the server is reachable, then the promise will be successful (i.e. _'resolved'_), else it will be unsuccessful (i.e. _'rejected'_). The _'.then()'_ is method chained to the function to return a promise. The _'.catch()'_ method should be used to handle the scenario where the promise was not fulfilled (i.e. _'rejected'_).

### JSX

- JSX combines HTML and JavaScript to define the output within the `Render()` class method

### Compiling

- _Babel_ is a modern JavaScript compiler
- _"Hot module Reloading"_ is where the browser is automatically updated with any changes that are made within the IDE once the file has been saved.

### Classes

- Classes are used to define components by extending them
- In JavaScript, classes are objects because they are effectively syntactic sugar over constuctor functions. Functions are also objects in JavaScript and therefore classes are also objects.

### State

- The _state_ needs to be set within a `ComponentDidMount()` lifecycle method
- The _setState()_ function tells React that the component and all of its children need to be re-rendered with the updated state.
  - This is the primary method that is used to update the user interface in response to an event handler or server responses.
  - _setState()_ can be thought of as a **request** rather than an immediate command to update the component.

### Props

- _Props_ are inputs to a react component
  - They are passed from parent to child components
  - They are read-only and therefore cannot be modified
  - `props.children` is available on every component. It contains the content between the opening and closing tags of a component.
  - React event handlers are named using camelCase, rather than lowercase.
- _Props_ is used to pass an object's code around React components so that it can be rendered
- _Props_ (short for “properties”) and _state_ are both plain JavaScript objects.
- While both _props_ and _state_ both hold information that influences the output of render, they are different in one important way...
  - _props_ get passed to the component (similar to function parameters)
  - _state_ is managed within the component (similar to variables declared within a function)
- `props.children` is available on every component. It contains the content between the opening and closing tags of a component.

### Functions

- Arrow functions ( => ) should be used to make the code more readable and concise
- Arrow functions do not rebind the _this_ keyword
- When a function is assigned to a constant, the _this_ binding is not transferred to the constant.
  - When the function is a raw function, the _this_ binding is in the context of the function.
  - The function's context is lost once the function has been assigned to a constant.

### Styling

- Ant is a styling library used for React
- Bootstrap can still be used within React and it needs the library installing

### Reconciliation

- When a component’s _props_ or _state_ change, React decides whether an actual DOM update is necessary by comparing the newly returned element with the previously rendered one. When they are not equal, React will update the DOM.

### Lifecycle Methods

- Lifecycle methods are custom functionality that gets executed during the different phases of a component.
- There are methods available when the component gets...
  - created and inserted into the DOM (mounting)
  - when the component updates
  - when the component gets unmounted or removed from the DOM
  - With JSX you pass a function as the event handler, rather than a string.
- _ComponentDidUpdate()_ is a useful method to use when I want to figure out when my component's data has changed.
- _ComponentDidUpdate()_ will be used for when we want to save data based upon user actions.
- _ComponentDidMount()_ will be used for when we want to fetch the last saved data.

  - The example below tries to fetch the last known data from the options variable. If it cannot get the data from the variable, then it will handle the exception within the catch block and just pass over the error silently by not doing anything.
  - If the options variable is returned, then the state is set.

```javascript
componentDidMount()
    try {
        const json = localstorage.getItem('options')
        const options = JSON.parse(json);
    }
    if {options} {
        this.setState(() => ({ options }));
    }
    catch(error) {
        // Do nothing at all
    }
```

### Routers

- A BrowserRouter (aliased as Router) can be used to render each of the items. For example, this could be to render each of the blog posts.

### Keys

- A “key” is a special string attribute you need to include when creating arrays of elements.
  - Keys help React identify which items have changed, are added, or are removed.
  - Keys should be given to the elements inside an array to give the elements a _“stable identity”_.
  - Keys only need to be unique among sibling elements in the same array. They don’t need to be unique across the whole application or even a single component.
  - Ideally, keys should correspond to unique and stable identifiers coming from your data, such as _post.id_

### Refs

- React supports a special attribute that you can attach to any component. The ref attribute can be an object created by React.createRef() function or a callback function, or a string (in legacy API).
- When the ref attribute is a callback function, the function receives the underlying DOM element or class instance (depending on the type of element) as its argument. This allows you to have direct access to the DOM element or component instance.
- Use refs sparingly. If you find yourself often using refs to “make things happen” in your app, consider getting more familiar with top-down data flow.

### SEO

- An <a href="https://medium.freecodecamp.org/seo-vs-react-is-it-neccessary-to-render-react-pages-in-the-backend-74ce5015c0c9" >article on medium.freecodecamp</a> reports that Google has stated in its own documentation that Google is able to crawl and therefore index web pages that are rendered from the client side so long as webmasters do not prevent Googlebot from crawling their JavaScript content. As long as Google can read what is being rendered to the DOM, then their search ranking will not be affected.

### Questions to Get Answers To

- Research setState()
- A Redux implmentation within my React project consists of actions, components, containers, reducers and store. Research in more detail what each of these are in the context of a Redux project
- What is a 'payload'?
