# ------------------------------------------------------------------------------------------------
#
#
#
#                                   ,_
#                                    :`.            .--._
#                                     `.`-.        /  ',-""""'
#                                       `. ``~-._.'_."/
#                                         `~-._ .` `~;
#                                              ;.    /
#                                             /     /
#                                        ,_.-';_,.'`
#                                         `"-;`/
#                                           ,'`
#
#
#                            Date: 11 dec 2022, Author Riley Smith
#             ____   ____  _        ___  __ __       _____ ___ ___  ____  ______  __ __
#           |    \ |    || |      /  _]|  |  |     / ___/|   |   ||    ||      ||  |  |
#           |  D  ) |  | | |     /  [_ |  |  |    (   \_ | _   _ | |  | |      ||  |  |
#           |    /  |  | | |___ |    _]|  ~  |     \__  ||  \_/  | |  | |_|  |_||  _  |
#           |    \  |  | |     ||   [_ |___, |     /  \ ||   |   | |  |   |  |  |  |  |
#           |  .  \ |  | |     ||     ||     |     \    ||   |   | |  |   |  |  |  |  |
#           |__|\_||____||_____||_____||____/       \___||___|___||____|  |__|  |__|__|
#
#
#
# ------------------------------------------------------------------------------------------------
#
# https://miro.com/app/board/uXjVP7dLv60=/
# https://docs.google.com/spreadsheets/d/13sjYPtkIxm79vFJ8Mz1uQJ94AIi8n7FoLCokQpN8wo8/edit#gid=0
# ^ test google sheet
# https://docs.google.com/spreadsheets/d/    SPREADSHEET_ID    /edit#gid=    SHEET_ID
#                                                ***                           ***
# and the file_name is for the other code to see and use, **do not change**
#
# ------------------------------------------------------------------------------------------------

import subprocess


def simplifyGoogleLink(text):
    spreadsheet_id = []
    sheet_id = []
    id_of_identifier = []
    # finds / in the https://docs.google ect ect and maps them out
    for i in range(len(text)):
        if text[i] == '/':
            id_of_identifier.append(i)
    # uses the mapped /'s and gets the one between 5 & 4 (where ssid is located) to pull them into a ssid list
    for v in range(id_of_identifier[5]-id_of_identifier[4] - 1):
        spreadsheet_id.append(text[v+id_of_identifier[4]+1])
    # hit gid just means the = sign to identify when the sid starts as it goes /edit#gid=2342 where 2342 is the sid and then pulls that number into a list
    hit_gid_identifier = False
    for c in range(len(text) - id_of_identifier[-1] - 1):
        if (hit_gid_identifier):
            sheet_id.append(text[c + id_of_identifier[-1] + 1])
        if text[c + id_of_identifier[-1] + 1] == '=':
            hit_gid_identifier = True
    # joins the lists and combines with '' (empty space)
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

# ------------------------------------------------------------------------------------------------
#
#
# GOT THE DATA, NOW WE NEED TO ORDER THEM IN A WAY THAT LEAVES THE PERMANENT STALLS AS ARE AND THE
# REST JOINS CLOSEST TO THEIR OWN, IE FOOD NEXT TO FOOD, CLOTHES NEXT TO CLOTHES, ECT ECT
#
#
# ------------------------------------------------------------------------------------------------
