DEBUG = False

# Make this unique, and don't share it with anybody.
SECRET_KEY = ''

DATABASES = {
    # local database to serve api requests
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    },
    # master nskyc.com database
    'master': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': '', 
        'USER': '',      
        'PASSWORD': '', 
        'HOST': '', 
        'PORT': '',                       
    }
}

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)
