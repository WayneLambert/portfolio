# Production Workflow

The request response cycle in production for a Django application

- Nginx is the web server
- Gunicorn is the application server
- WSGI is an interface between the application server and the web application (Django)
- Web application logic is handled by the programmer within the web framework

## Workflow

- Browser makes request by sending a URL of the application to the web server (Nginx).
- The web server (Nginx) is acting as a proxy which sends the request to Gunicorn (Python http server)
- Gunicorn receives the request and communicates with the web application via an interface called the Web Server Gateway Interface (WSGI)
- The web application (Django) processes the request using the business logic within the application's program and returns a response back to Gunicorn via the Web Server Gateway Interface (WSGI)
- Gunicorn receives the response from the web application (Django) via WSGI and forwards it on to the web server (Nginx)
- Nginx forwards the response back to the user in the browser

## Workflow Diagram

```text
Browser ==> Nginx ==> Gunicorn ==> WSGI ==> Django ==> WSGI ==> Gunicorn ==> Nginx ==> Browser
```
