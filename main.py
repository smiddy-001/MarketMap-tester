#
# UNDERSTANDING SHIT I WROTE BELOW
#
# https://docs.google.com/spreadsheets/d/    SPREADSHEET_ID    /edit#gid=    SHEET_ID
#                                                ***                           ***
# and the file_name is for the other code to see and use, **do not change**

import subprocess

# https://docs.google.com/spreadsheets/d/13sjYPtkIxm79vFJ8Mz1uQJ94AIi8n7FoLCokQpN8wo8/edit#gid=0


def simplifyGoogleLink(text):
    spreadsheet_id = []
    sheet_id = []
    id_of_identifier = []
    for i in range(len(text)):
        if text[i] == '/':
            id_of_identifier.append(i)
    # print(id_of_identifier)
    # print(f'{id_of_identifier[4]} to {id_of_identifier[5]}')
    for v in range(id_of_identifier[5]-id_of_identifier[4] - 1):
        # print(f'n = {v+id_of_identifier[4]+1} : {text[v+id_of_identifier[4]+1]}')
        spreadsheet_id.append(text[v+id_of_identifier[4]+1])
    # print(
        # f'{id_of_identifier}, {id_of_identifier[-1]}, {len(text) - id_of_identifier[-1]}')
    hit_gid_identifier = False
    for c in range(len(text) - id_of_identifier[-1] - 1):
        # print(f'{text[c + id_of_identifier[-1] + 1]}')
        if (hit_gid_identifier):
            sheet_id.append(text[c + id_of_identifier[-1] + 1])
        if text[c + id_of_identifier[-1] + 1] == '=':
            hit_gid_identifier = True
    ssid = ''.join(spreadsheet_id)
    sid = ''.join(sheet_id)

# speadsheet id[0], sheet id[1]
    return (ssid, sid)


sheets_data = simplifyGoogleLink(
    'https://docs.google.com/spreadsheets/d/13sjYPtkIxm79vFJ8Mz1uQJ94AIi8n7FoLCokQpN8wo8/edit#gid=0')

SPREADSHEET_ID = sheets_data[0]
SHEET_ID = sheets_data[1]
FILE_NAME = 'data.csv'

# gets the data from google sheets using info above, downloads it as data.csv
bashCommand = f'wget --output-file=logs.txt https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}/export?format=csv&gid={SHEET_ID} -O {FILE_NAME}'
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
