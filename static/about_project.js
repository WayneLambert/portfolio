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
  else
    return 'About ' + context + ' Project';  
  }

function getAboutProjectText(context) {
  if (context === 'blog') {
    return blogDescription
  } else if (context === 'scraping') {
    return scrapingDescription
  } else if (context === 'count') {
    return countDescription
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

<b>Features</b><br><br>

&bull; Full user registration and login with author-level permissions<br>
&bull; Profile creation in line with user creation using Django signals<br>
&bull; Django Crispy Forms is used to handle form applications<br>
&bull; Category selector in the sidebar gives a view of posts by category<br>
&bull; Clicking the link for an author gives a view of posts written by the author<br>
&bull; Pagination is implemented to speed up page loading and assist with navigation<br>
&bull; A read-only view of profile details for the logged in user<br>
&bull; Django template code is in easily maintainable files<br>
&bull; A many-to-many database relationship between blog posts and categories<br>
&bull; Static file management is implemented with the third party Django package, WhiteNoise<br>
&bull; JavaScript code in conjunction with a Django HTML template and CSS means that you can see this 'About' page<br><br>

<b>Languages: </b>Python, HTML / CSS, JavaScript<br>
<b>Frameworks: </b>Django, Bootstrap, FontAwesome<br>
<b>Other: </b>PostgreSQL, GitHub<br><br>

<b>Disclaimer: </b>The posts written within the blog are purely copied from the
relevant documentation sites. They are only intended for a visual representation
of content and, in my opinion, give a better representation of the final product
that is intended by the blog's design than just using some standard
<em>lorem ipsum</em> text.
`;


const scrapingDescription =
`
The scraping project is built using Python's third party libraries,
<b><em>requests</em></b> and <b><em>Beautiful Soup</em></b>.<br><br>

The speeches scraped for the app can be found from the following links: <br><br>
<a href="https://www.goodreads.com/quotes/55276-i-have-nothing-to-offer-but-blood-toil-tears-and">Churchill Speech</a>
<br>
<a href="https://www.goodreads.com/work/quotes/4694-the-illustrated-gettysburg-address">Gettysburg Speech</a>
<br><br>

<b>Features</b><br><br>

&bull; Uses the <em>Requests</em> library to get the response from the speech's web page<br>
&bull; Uses <em>Beautiful Soup</em> library to extract the appropriate content from the response<br>
&bull; Uses Python text manipulation built-in methods such as .split() and .strip() to transform parsed HTML into human-friendly readable format.<br>
&bull; Uses context within Django templates to render the parsed and manipulated speech<br>
&bull; Quantum's developer tools were used to ascertain the HTML components to manipulate<br>
&bull; JavaScript code in conjunction with a Django HTML template and CSS means that you can see this 'About' page<br><br>

<b>Languages: </b>Python, HTML / CSS, JavaScript<br>
<b>Frameworks: </b>Django, Bootstrap, FontAwesome<br>
<b>Other: </b>GitHub<br>
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
<b>Other: </b>GitHub<br>
`;