# BART PROJECT
```
BartProj/
    - config/
        - base.py          # Stores most settings
        - local.py         # Stores settings only for local dev
        - production.py    # Stores settings only used by production (e.g. Heroku)
    - urls.py              # Global urls.py -> routes to apps.urls.py for "" and accounts.urls.py for "account/"

- apps/                    
    - accounts/                 # app for managing users
        - models.py             # FavoriteStation model for storing favorited stations by users
        - urls.py               
            - accounts/login    # calls log_in() for django form to login -> redirect to /home
            - accounts/signup   # calls sign_up() for django form to signup -> redirect to /home
            - accounts/logout   # calls logout_view() -> redirect to /
            - accounts/favorites # calls favorites() for django form to edit favorite stations -> redirect to /home
        - views.py         
            - log_in()          # login stuff
            - sign_up()         # passes signup form based on User class
            - logout_view()     # logout stuff
            - favorites()     # passes edit user form based on User class
        - forms.py         # UserEditForm and SignupForm for views
        - templates/       # Templates for user profile stuff
            - accounts.html     # extends base -> template for accounts/ pages
            - login.html        # extends accounts -> login page
            - signup            # extends accounts -> signup page
            - favorites         # extends accounts -> favorites (ie, preferences) page
    - core/                # app for displaying station information
        - static/          # Static files
        - templates/       # Core templates, including base templates
            - base.html    # base for all pages
            - pages/
                - homepage.html                 # extends base -> template for homepages
                - homepage_logged_in.html       # extends homepage -> shows 'signup' and 'login' 
                - homepage_logged_out.html      # extends homepage -> shows 'logout' and 'favorites'
        - urls.py
            - /              # URL for homepage -> drop down of possible stations and displays schedule choice -> homepage_logged_out.html
            - /home          # URL for homepage of logged in user -> shows favorited stations with schedules -> homepage_logged_in.html
        - views.py
            - homepage()    # function for homepage (logged out user)
            - home()        # function for home (logged in user with favorite stations)
- manage.py                # Entry point
- Pipfile                  # Development requirements

```




### Name ideas???
* BART ETAs
* Run BART
* We <3 BART
* BART's okay
* BART's not great but it's what we've got

## Milestone 1

### Collaborators
* Chad
* Josh
* Marby

### Software Goal & Concept
* Easily see timing of next train
* Quickly understand traffic at favorite stations (e.g., recent trends on timing for trains at station)
* Know if you need to run, walk or wait based on your current location and next trian

### Project Specifications
* API Consumed
    * BART API for live train ETAs for specific stations and routes
* Work Involved
    * Frontend
        * Templates
        * CSS
        * Bootstrap
    * Backend
        * API 
            * Getting data from BART
            * Calculations
            * Store to database
        * Django
            * User profiles to create your favorite routes
            * Render website with most recent data from database

### Challenges and Unkowns
* BART API may not provide the data we expect it to
* Complications getting the data to update regularly in the database

### Group Roles
* Front-end: Marby
* Back-end: Chad
* API/Models: Josh
