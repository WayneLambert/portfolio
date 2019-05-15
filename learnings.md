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

### Resources

- <a href="https://www.youtube.com/watch?v=uZgRbnIsgrA&list=WL&index=38&t=0s">JustDjango Django and React - Tutorial 1</a>
- <a href="https://www.youtube.com/watch?v=w-QJiQwlZzU&list=WL&index=35&t=0s">JustDjango Django and React - Tutorial 2</a>


### Questions to Get Answers To

- How does SEO work in React applications?
- What is the difference between props and state?
- What is the lifecycle events? How do they work and what are they used for?
- What is a 'promise' in JavaScript?
