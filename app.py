import json
import os
from flask import *
from google.oauth2.service_account import Credentials
import gspread

app = Flask(__name__)

@app.route("/<shorthand>")
def redirect_shorthand(shorthand):
    json_acc_info = json.loads(os.environ['GOOGLE_SHEETS_CREDENTIALS'])
    scopes = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
    credentials = Credentials.from_service_account_info(json_acc_info, scopes=scopes)
    client = gspread.authorize(credentials)
    sheet_data = client.open('Link Shorthands').worksheet('Mappings').get_all_values()
    mappings = {row[0]: row[1] for row in sheet_data}

    if shorthand not in mappings:
        abort(404)

    return redirect(mappings[shorthand])
