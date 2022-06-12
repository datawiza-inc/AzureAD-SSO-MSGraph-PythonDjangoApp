# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

# <FirstCodeSnippet>
import yaml
import msal
import os
import time

from tutorial.graph_helper import get_user_mailbox_settings

# Load the oauth_settings.yml file
stream = open('oauth_settings.yml', 'r')
settings = yaml.load(stream, yaml.SafeLoader)

def get_url(api):
  return settings[api]
# </FirstCodeSnippet>

# <SecondCodeSnippet>
def get_user(request):
  user = {
    'is_authenticated': False,
  }
  try:
    headers = request.headers
    if 'X-Dw-User' in headers:
      info = get_user_mailbox_settings(get_token(request))
      user = {
        'is_authenticated': True,
        'name': headers['name'],
        'email': headers['email'],
        'timeZone': info['mailboxSettings']['timeZone'] if ('timeZone' in info['mailboxSettings']) else 'UTC'
      }
  except Exception as e:
    print(e)
  return user

def get_token(request):
  return request.headers['X_DATAWIZA_TOKEN_AAD_ACCESS_TOKEN']
# </SecondCodeSnippet>
