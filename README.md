## Try uWSGI with flask and django

### 1. Without web framework
- service port: 3031
- nginx port: 8081
- url: 127.0.0.1:8081
- setup: `uwsgi --ini raw_uwsgi.ini`

### 2. Flask web app
- service port: 3032
- nginx port: 8082
- url: 127.0.0.1:8082
- setup: `uwsgi --ini flasgi.ini`

### 3. Django web app
- service port: 3033
- nginx port: 8083
- url: 127.0.0.1:8083
- setup: `uwsgi --ini djangi.ini`

