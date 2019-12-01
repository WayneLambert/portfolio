# Scraping Project

The `Scraping` project demonstrates the use of the `Requests` library to handle the request/response cycle for the GET requests that are required to retrieve data from another website.

Python's third party library, `Beautiful Soup`, is used to parse the required HTML from the response object. Python text functions are used to target, strip and split any required text so that it's in a suitable format to render for human readability.

Finally, the Django component of the application is the handling of the URLs to target a view which returns the required response to the Django template. In other words, there is no 'M' component used within this app, it just uses the 'V' and the 'T' components of the MVT architectural paradigm that Django uses.

The examples give scraping examples using string manipulation of DOM elements and from reading JSON formatted data.

The most comprehensive example is the **EU Membership Referendum Results** as it consists of scraping the voting results from the BBC website. Other fields are calculated elements within the logic of the application.

## Technologies Used

- Languages: Python, HTML / CSS
- Frameworks: Django, Bootstrap, FontAwesome
- Libraries: Requests, BeautifulSoup
- Other: GitHub, Docker, Firefox Developer Tools

## Sources

- EU Referendum Results: <https://www.bbc.co.uk/news/politics/eu_referendum/results/local/a>
- Famous speeches: <https://www.goodreads.com>
- Word of the Day: <https://www.dictionary.com/e/word-of-the-day/>
- Dad jokes: <https://icanhazdadjoke.com/>

## Disclaimer

The speeches and jokes are no indication of any particular political viewpoint or affiliation. They are merely used to demonstrate the project's objectives.
