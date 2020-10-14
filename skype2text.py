#!/usr/bin/env python3
# charset=utf-8
#
# author   : frostblue
# git repo : github.com/frostblue/skype2text
# license  : unlicense (public domain code, see unlicense.org)
#
#  ____  _                     ____ _____         _
# / ___|| | ___   _ _ __   ___|___ \_   _|____  _| |_
# \___ \| |/ / | | | '_ \ / _ \ __) || |/ _ \ \/ / __|
#  ___) |   <| |_| | |_) |  __// __/ | |  __/>  <| |_
# |____/|_|\_\\__, | .__/ \___|_____||_|\___/_/\_\\__|
#             |___/|_|
#
# TODO:
#   - Unfortunately so far there are issues with unicode characters
#     and the code might randomly fail if printed to stdout when invoked as $(./skype2text.py).
#     Will have to investigate further
#   - Ignore messages where body_xml is empty in the SQL query direcly
#   - Implement these fixes https://codereview.stackexchange.com/a/148316

import sys
import os.path
import datetime
import sqlite3
import html


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def eprint_use():
    eprint("usage : " + sys.argv[0] + " <file.db> <partner's skype ID> [output file]")

# Actual code begins here
# Print the use message in case of incorrect amount of arguments

if not len(sys.argv) in [3, 4]:
    eprint_use()

else:
    database_path = sys.argv[1]
    partner_id = sys.argv[2]
    output_path = sys.argv[3] if len(sys.argv) == 4 else partner_id + '.txt'

    if not os.path.isfile(database_path):
        sys.exit('the file %s does not exist' % (database_path))

    output_file = sys.stdout if output_path == '-' else open(output_path, 'w')
    connection = sqlite3.connect(database_path)

    cursor = connection.cursor()

    cursor.execute("""
    SELECT timestamp,from_dispname,body_xml
    FROM Messages
    WHERE dialog_partner='""" + partner_id + """'
    ORDER BY timestamp
    """)

    for row in cursor.fetchall():
        timestamp = datetime.datetime.utcfromtimestamp(int(row[0])).strftime('%Y-%m-%d %H:%M:%S')
        name_tag = row[1]
        message_body = html.unescape(row[2])

        output = "[%s] <%s> %s\n" % (timestamp, name_tag, message_body)

        output_file.write(output)

