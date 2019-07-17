# ab_back_end.conf
server {
  listen 80;
  server_name localhost;

  # serve static files
  location /static/ {
    alias /static/;
  }

  # serve media files
  location /media/ {
    alias /media/;
  }

  # pass requests for dynamic content to gunicorn
  location / {
    proxy_pass http://web:8080;
  }
}