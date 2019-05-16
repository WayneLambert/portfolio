# Learnings

## Django / Python

- Viewsets can be used to make code tidy in cases where each of the HTTP methods will be used. Blog posts makes a good use case for this as it is likely that you would want to be able to create, read, update and delete blog posts.

## React / JavaScript

- Classes are used to define components by extending them
- JSX combines HTML and JavaScript to define the output within the Render method
- Axios is a library used to read data from my back ends API endpoint
- Ant is a styling library used for React (in a similar way to Bootstrap for HTML/CSS sites)
- Bootstrap can still be used within React and it needs the library installing
- Props is used to pass an object's code around React components so that it can be rendered
- The 'Map' function can be used to render a list of items as HTML elements/items
- The state needs to be set within a ComponentDidMount object
- A BrowserRouter (aliased as Router) can be used to render each of the items. For example, this could be to render each of the blog posts.
- Arrow functions should be used to make the code more readable and concise
- React is a view library concerned with dealing with the 'V' in the MVC model.
- React manages a virtual DOM which is reconciled against the Real DOM which is managed by the browser. Any React element that is different in the Virtual DOM is then refreshed in the Real DOM so that the two are always kept in sync and changes are inexpensive and lightweight. This gives responsive applications.
- Every application is composed of a tree of components which produces a complex markup. A component is a piece of the user interface. Every application contains at least the root component.
- Render describes what the UI should look like
- React is called 'React' because it reacts to state changes in the DOM
- If you do not want to stay with the default create-react-app build configuration when it comes to production, you can run the `npm run eject` command which enables for manual changes to the build.
- Babel is a modern JavaScript compiler
- "Hot module Reloading" is where the browser is automatically updated with any changes that are made within the IDE once the file has been saved.
- Use the 'const' keyword over 'let'. Only use 'let' when I need to reassign a variable.
- Arrow functions do not rebind the 'this' keyword
- The equivalent of f strings in JavaScript using ${var_name} between backtick operators
- In JavaScript, classes are objects because they are effectively syntactic sugar over constuctor functions. Functions are also objects in JavaScript and therefore classes are also objects.
- React.Fragment can be used in cases where you insert a div around some JSX elements that require an additional container for Babel to be able to compile it. If you use a standard <div></div> tag, then this may produce two div tags wrapping around the JSX elements (when you inspect the elements in Chrome Developer tools) which probably isn't the desired outcome.
- The notation += appends to an existing variable. This means that the variable should be 'let' rather than a 'const'
- The operator '?' reads as 'then' in a conditional statement
- The operator ':' reads as 'else' in a conditional statement
- '\n' is the new line escape character in JavaScript
- An <a href="https://medium.freecodecamp.org/seo-vs-react-is-it-neccessary-to-render-react-pages-in-the-backend-74ce5015c0c9" >article on medium.freecodecamp</a> found at  states that Google has stated in its own documentation that Google is able to crawl and therefore index web pages that are rendered from the client side so long as webmasters do not prevent Googlebot from crawling their JavaScript content. As long as Google can read what is being rendered to the DOM, then their search ranking will not be affected.
- props (short for “properties”) and state are both plain JavaScript objects. While both hold information that influences the output of render, they are different in one important way: props get passed to the component (similar to function parameters) whereas state is managed within the component (similar to variables declared within a function).
- Containers are very similar to components, the only difference is that containers are aware of application state. If part of your webpage is only used for displaying data (dumb) then make it a component.

### Questions to Get Answers To

- What is the difference between props and state?
- What is the lifecycle events? How do they work and what are they used for?
- What is a 'promise' in JavaScript?
