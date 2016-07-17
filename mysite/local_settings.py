
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'blogengine',
        'USER': 'mugambi',
        'PASSWORD': '327140002Hm',
        'HOST': 'localhost',
        'PORT': '',
    }
}
Debug = True