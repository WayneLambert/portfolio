`
Creates immediate information about the various projects for the user, so they
can preview what the project is about as well as the skills and technologies
involved.
`

function aboutProject(context) {
  showElement();
  const aboutHeading = getAboutProjectTitle(context);
  const aboutProject = getAboutProjectText(context);
  populateAboutProject(aboutHeading,aboutProject);
}

function getAboutProjectTitle(context) {
  if (context === 'count') {
    return 'About ' + context + 'ing Project';
  }
  if (context === 'blog-api') {
    return 'About Blog Project: API Endpoints';
  }
  if (context === 'blog-react') {
    return 'About Blog Project: React';
  }
  else
    return 'About ' + context + ' Project';
}

function getAboutProjectText(context) {
  if (context === 'blog') {
    return blogDescription
  } else if (context === 'blog-api') {
    return blogAPIDescription
  } else if (context === 'blog-react') {
    return blogReactDescription
  } else if (context === 'scraping') {
    return scrapingDescription
  } else if (context === 'count') {
    return countDescription
  } else if (context === 'countdown') {
    return countdownDescription
  } else
    return 'The context is unknown'
}

function populateAboutProject(aboutHeading,aboutProject) {
  const elemProjectTitle = document.getElementById('about-project-title');
  elemProjectTitle.innerHTML = aboutHeading;
  const elemProjectBody = document.getElementById('about-project-body');
  elemProjectBody.innerHTML = aboutProject;
}

function showElement() {
  var elem = document.getElementById('about-project');
  elem.style.display = 'block';
}

function hideElement() {
  var elem = document.getElementById('about-project');
  elem.style.display = 'None';
}

const blogDescription =
`
The blog project is built with Django and uses a PostgreSQL database. It is a
full CRUD application with the ability to create, update and delete posts. Views
within the application are total posts, posts by author, and posts by category.<br><br>

A comprehensive list of features can be found on the project's <a href="https://github.com/WayneLambert/portfolio">README file on GitHub</a>
<br><br>

<b>Languages: </b>Python, HTML / CSS, JavaScript, SQL<br>
<b>Frameworks: </b>Django, Django REST, Bootstrap, FontAwesome<br>
<b>Other: </b>PostgreSQL, GitHub, Docker, Heroku, S3, Simple Email Service<br><br>

The blog also comes with an API built with Django Rest Framework. The endpoints can be found at:<br><br>

- <a href="https://waynelambert.dev/api/blog/posts">List View</a><br>
- <a href="https://waynelambert.dev/api/blog/posts/1">Detail View</a>
`;


const blogAPIDescription =
`
The blog API is built using Django REST Framework. In addition to standard serializers, some of
data points have been transformed to give the front end developer something more useful than the ID.<br><br>

A comprehensive list of features can be found on the project's <a href="https://github.com/WayneLambert/portfolio">README file on GitHub</a>
<br><br>

<b>Languages: </b>Python, HTML / CSS, JavaScript, SQL<br>
<b>Frameworks: </b>Django, Django REST, CSS<br>
<b>Other: </b>PostgreSQL, GitHub, Docker<br><br>

The endpoints can be found using the following links:<br><br>

- <a href="https://waynelambert.dev/api/blog/posts">List View</a><br>
- <a href="https://waynelambert.dev/api/blog/posts/1">Detail View</a>
`;


const blogReactDescription =
`
The React version of the blog utilises the API endpoints developed in the 'Blog Project: API Endpoints'
<br><br>

A comprehensive list of features can be found on the project's <a href="https://github.com/WayneLambert/portfolio">README file on GitHub</a>
<br><br>

<b>Languages: </b>Python, HTML / CSS, JavaScript<br>
<b>Frameworks: </b>React, Django, Django REST, CSS, Bootstrap, Ant<br>
<b>Other: </b>PostgreSQL, GitHub, Docker, Axios<br><br>

`;

const countdownDescription =
`
The countdown project uses the logic from the letters game on Countdown to enable a player to
play against the computer attempting to get the longest word that they can.
<br><br>

<b>Features</b><br><br>

&bull; Uses a functional programming style to implement the game's rules logic into the program<br>
&bull; The list of 113,809 english words is stored in a text file on the server<br>
&bull; Validates that the word chosen by the player is one within the list of words<br>
&bull; Validates that the word chosen by the player uses only the randomly generated selection of letters<br>
&bull; Returns a game result displaying the winner<br>
&bull; Looks up the dictionary definition of the word using the Oxford English Dictionaries API<br>
&bull; There is no 30 second clock like there is on the actual game of Countdown<br><br>

<b>Languages: </b>Python, HTML / CSS<br>
<b>Frameworks: </b>Django, Bootstrap, FontAwesome<br>
<b>Other: </b>GitHub, Docker, Oxford Dictionary API<br>
`;

const countDescription =
`
The counting project uses core Python functionality in addition to Django to count the number   
of occurences that each word and letter appears within the textbox.<br><br>

<b>Features</b><br><br>

&bull; Uses Python lists to store results from logic<br>
&bull; Uses Pythonic for [each] loop to iterate over every letter of the alphabet
to test for presence<br>
&bull; Uses Python's string interpolation (i.e. f strings) to make readable sentances<br>
&bull; Creates a context dictionary with several elements used within the Django
template to give the user rich information about their request<br>
&bull; JavaScript code in conjunction with a Django HTML template and CSS means
that you can see this 'About' page<br><br>

<b>Languages: </b>Python, HTML / CSS, JavaScript<br>
<b>Frameworks: </b>Django, Bootstrap, FontAwesome<br>
<b>Other: </b>GitHub, Docker<br>
`;


const scrapingDescription =
`
The scraping project is built using Python's third party libraries,
<b><em>requests</em></b> and <b><em>Beautiful Soup</em></b>.<br><br>

<b>Features</b><br><br>

&bull; Uses the <em>Requests</em> library to get the response from the speech's web page<br>
&bull; Uses <em>Beautiful Soup</em> library to extract the appropriate content from the response<br>
&bull; Uses built-in Python text manipulation methods such as .split() and .strip() to transform parsed HTML into a human-friendly and readable form<br>
&bull; Uses context within Django templates to render the parsed and manipulated speech<br>
&bull; Quantum's developer tools were used to ascertain the DOM elements to manipulate<br><br>

<b>Languages: </b>Python, HTML / CSS, JavaScript<br>
<b>Frameworks: </b>Django, Bootstrap, FontAwesome<br>
<b>Other: </b>GitHub, Docker<br>
`;
