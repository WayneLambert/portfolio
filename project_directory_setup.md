# Project Directory Setup

The below illustrates the ideal directory structure that has a Django backend and a React frontend.

/Dev
    /{overall_project_name}
        /src
            **/aa-front-end**
                /build
                /node_modules
                /public
                /src
                    /app1
                    - App.css
                    - App.js
                    - App.test.js
                    - index.css
                    - logo.svg
                    - registerServiceWorker.js
                - package-lock.**json**
                - package.json
                - README.me
            **/ab_back_end**
                /templates
                    - base.html
                    - home.html
                    - about.html
                    - contact.html
                - settings.py
                - urls.py
                - wsgi.py
                /migrations
                    - 0001_initial.py
                /static
                    /images
                /templates
                    /app1
                        -app1.html
            /app1
                /templates
                    /app1
                        - template1.html
                - admin.py
                - apps.py
                - forms.py
                - models.py
                - permissions.py
                - serializers.py
                - tests.py
                - urls.py
                - utils.py
                - views.py
            /app2
            /app3
            - db.sqlite3
            **- manage.py**
            - Pipfile
            - Pipfile.lock
        .git *1
        .gitignore
        .README.md
        .LICENSE.md

## Implementation Notes

* Leaving the project names as just 1f and 2b are simple names to give the front and back end aspects of the overall project that allow for the project to grow because the naming doesn't tie the app down to its purpose. It is merely in place as a separation from the front ansd back end components of the project.

* The git init should be initialised at the top level src level so that all source code beneath it can be tracked.

* The virtual environment for Django should be created against the 2b folder so that it relates to any of the backend development.

* Recommended best practice is to do small migrations each time as the migrations being saved into the migrations folder can provide for an excellent debugging tool and also abides be the principles of iterative testing and development.
