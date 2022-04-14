"""
Overrides settings specific to the local environment.
If backend/Environ/Dev.env file exists.
"""

import os
from django.urls import path, include
from backend.settings import base_settings as bs

if __name__=='backend.settings.local_settings':

  bs.INSTALLED_APPS.extend((
    "django_extensions",
    "debug_toolbar",
  ))


  # debug_toolbar settings

  bs.MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')

  DEBUG_TOOLBAR_URLS = [path('__debug__/', include('debug_toolbar.urls'))]  
  INTERNAL_IPS = [
    "127.0.0.1",
  ]


  # django_extensions settings

  os.environ['JUPYTER_ALLOW_INSECURE_WRITES'] = 'true'
  os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = 'true'
  os.environ['JUPYTER_PATH'] = str(bs.BASE_DIR)

  SHELL_PLUS = 'notebook'
  NOTEBOOK_ARGUMENTS = ['--no-browser']


  # bs.STATIC_ROOT = None
  # STATICFILES_DIRS = [
  #   bs.BASE_DIR('contrib', 'static'),
  # ]


__all__ = [i for i in dir() if i.isupper()]
