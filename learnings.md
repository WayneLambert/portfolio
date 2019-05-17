# Learnings

## Django / Python

- Viewsets can be used to make code tidy in cases where each of the HTTP methods will be used. Blog posts makes a good use case for this as it is likely that you would want to be able to create, read, update and delete blog posts.

## React / JSX / JavaScript

- React is a view library concerned with dealing with the 'V' in the MVC model.
- React manages a virtual DOM which is reconciled against the Real DOM which is managed by the browser. Any React element that is different in the Virtual DOM is then refreshed in the Real DOM so that the two are always kept in sync and changes are inexpensive and lightweight. This gives responsive applications.
- Every application is composed of a tree of components which produces a complex markup. A component is a piece of the user interface. Every application contains at least the root component.
- Render describes what the UI should look like
- React is called 'React' because it reacts to state changes in the DOM
- If you do not want to stay with the default create-react-app build configuration when it comes to production, you can run the `npm run eject` command which enables for manual changes to the build.
- React.Fragment can be used in cases where you insert a div around some JSX elements that require an additional container for Babel to be able to compile it. If you use a standard <div></div> tag, then this may produce two div tags wrapping around the JSX elements (when you inspect the elements in Chrome Developer tools) which probably isn't the desired outcome.

### Components

- React components are small, reusable pieces of code that return a React element to be rendered to the page.
- Components are not aware of application state. If my webpage is only going to be used for displaying data, then make it a components.
- Controlled Components
  - An input form element whose value is controlled by React is called a controlled component.
  - When a user enters data into a controlled component a change event handler is triggered and your code decides whether the input is valid (by re-rendering with the updated value).
  - If you do not re-render then the form element will remain unchanged.
- Uncontrolled Components
  - An uncontrolled component works like form elements do outside of React.
  - When a user inputs data into a form field (an input box, dropdown, etc) the updated information is reflected without React needing to do anything.
- In most cases you should use controlled components.

### Containers

- Containers are very similar to components, the only difference is that containers are aware of application state. If my webpage needs to be aware of application state, then make it a container.

### Vanilla JavaScript

- Axios is a library used to read data from my back ends API endpoint
- The 'Map' function can be used to render a list of items as HTML elements/items
- The notation += appends to an existing variable. This means that the variable should be 'let' rather than a 'const'
- The operator '?' reads as 'then' in a conditional statement
- The operator ':' reads as 'else' in a conditional statement
- '\n' is the new line escape character in JavaScript
- Use the 'const' keyword over 'let'. Only use 'let' when I need to reassign a variable.
- The equivalent of f strings in JavaScript using ${var_name} between backtick operators

### JSX

- JSX combines HTML and JavaScript to define the output within the Render method

### Compiling

- Babel is a modern JavaScript compiler
- "Hot module Reloading" is where the browser is automatically updated with any changes that are made within the IDE once the file has been saved.

### Classes

- Classes are used to define components by extending them
- In JavaScript, classes are objects because they are effectively syntactic sugar over constuctor functions. Functions are also objects in JavaScript and therefore classes are also objects.

### State

- The state needs to be set within a ComponentDidMount object

### Props

- Props are inputs to a react component
  - Passed from parent to child
  - Are read-only, therefore they cannot be modified
  - props.children is available on every component. It contains the content between the opening and closing tags of a component.
  - React event handlers are named using camelCase, rather than lowercase.
- Props is used to pass an object's code around React components so that it can be rendered
- props (short for “properties”) and state are both plain JavaScript objects. While both hold information that influences the output of render, they are different in one important way: props get passed to the component (similar to function parameters) whereas state is managed within the component (similar to variables declared within a function).
- props.children is available on every component. It contains the content between the opening and closing tags of a component.

### Functions

- Arrow functions should be used to make the code more readable and concise
- Arrow functions do not rebind the 'this' keyword

### Styling

- Ant is a styling library used for React (in a similar way to Bootstrap for HTML/CSS sites)
- Bootstrap can still be used within React and it needs the library installing

### Reconciliation

- When a component’s props or state change, React decides whether an actual DOM update is necessary by comparing the newly returned element with the previously rendered one. When they are not equal, React will update the DOM.

### Lifecycle Methods

- Lifecycle methods are custom functionality that gets executed during the different phases of a component.
- There are methods available when the component gets...
  - created and inserted into the DOM (mounting)
  - when the component updates
  - when the component gets unmounted or removed from the DOM
  - With JSX you pass a function as the event handler, rather than a string.

### Routers

- A BrowserRouter (aliased as Router) can be used to render each of the items. For example, this could be to render each of the blog posts.

### Keys

- A “key” is a special string attribute you need to include when creating arrays of elements.
  - Keys help React identify which items have changed, are added, or are removed.
  - Keys should be given to the elements inside an array to give the elements a “stable identity”.
  - Keys only need to be unique among sibling elements in the same array. They don’t need to be unique across the whole application or even a single component.
  - Ideally, keys should correspond to unique and stable identifiers coming from your data, such as post.id

### Refs

- React supports a special attribute that you can attach to any component. The ref attribute can be an object created by React.createRef() function or a callback function, or a string (in legacy API).
- When the ref attribute is a callback function, the function receives the underlying DOM element or class instance (depending on the type of element) as its argument. This allows you to have direct access to the DOM element or component instance.
- Use refs sparingly. If you find yourself often using refs to “make things happen” in your app, consider getting more familiar with top-down data flow.

### SEO

- An <a href="https://medium.freecodecamp.org/seo-vs-react-is-it-neccessary-to-render-react-pages-in-the-backend-74ce5015c0c9" >article on medium.freecodecamp</a> reports that Google has stated in its own documentation that Google is able to crawl and therefore index web pages that are rendered from the client side so long as webmasters do not prevent Googlebot from crawling their JavaScript content. As long as Google can read what is being rendered to the DOM, then their search ranking will not be affected.


### Questions to Get Answers To

- What is a 'promise' in JavaScript?

## Sources

- Official React documentation
- The Road to Learn React Book - by Robin Wieruch
- Mastering React - by Mosh Hamedani
- The Complete React Developer Course (w/ Hooks and Redux) - by Andrew Mead