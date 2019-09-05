# Scraping Project

The `Scraping` project demonstrates the use of the Requests library to handle the request/response cycle for the GET requests that are required to retrieve data from another website.

Python's third party library, Beautiful Soup, is used to parse the required HTML from the response object. Python text functions are used to target, strip and append any required text so that it's in a suitable format.

Finally, the Django component of the application is the handling of the URLs to target a view which returns the required response to the Django template. In other words, there is no 'M' component used within this app, it just uses the 'V' and the 'T' components of the MVT architectural paradigm that Django uses.

The examples given are famous speeches scraped from the <https://www.goodreads.com> website or dad jokes from <https://icanhazdadjoke.com/>

The two sites give scraping examples using string manipulation of DOM elements and from reading JSON formatted data.
