from __future__ import print_function
import os

from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage


def get_credentials():

    # If modifying these scopes, delete your previously saved credentials
    # at ~/.credentials/drive-python-quickstart.json
    SCOPES = 'https://www.googleapis.com/auth/drive.readonly'
    CLIENT_SECRET_FILE = 'client_secret.json'
    APPLICATION_NAME = 'GDriveRevisionDumper'

    flags=tools.argparser.parse_args(args=[])   #mimics no args specified

    home_dir = os.getcwd()
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'drive-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        
        credentials = tools.run_flow(flow, store, flags)
        print('Storing credentials to ' + credential_path)
   
    return credentials

