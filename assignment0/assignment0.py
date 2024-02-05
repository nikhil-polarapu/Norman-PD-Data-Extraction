import urllib.request
import io
import re
from pypdf import PdfReader
import sqlite3
import os

def fetchincidents(url):
       url = (url)
       headers = {}
       headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"                          

       data = urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read()  
       return io.BytesIO(data)                                                                         

def extractincidents(data):
        row_list = []
        reader = PdfReader(data)
        for page_num in range(len(reader.pages)):
            page = reader._get_page(page_num)
            page_text = page.extract_text(extraction_mode='layout')
            lines = page_text.split("\n")
            for line in lines:
                line = line.strip()
                if("NORMAN POLICE DEPARTMENT" in line):
                    line = line.replace("NORMAN POLICE DEPARTMENT", '')
                if("Daily Incident Summary (Public)" in line):
                    line = line.replace("Daily Incident Summary (Public)", '')
                if("Date / Time Incident Number Location Nature Incident ORI" in line):
                    line = line.replace("Date / Time Incident Number Location Nature Incident ORI", '')
                
                output = []
                
                datetime_pattern = r'\d{1,2}/\d{1,2}/\d{4} \d{1,2}:\d{2}'
                datetime_match = re.search(datetime_pattern, line)

                if datetime_match:
                    datetime_result = datetime_match.group()
                    output.append(datetime_result)
                    line = line.replace(datetime_result, '')
                    
                incident_number_pattern = r'\d{4}-\d+'
                incident_number_match = re.search(incident_number_pattern, line)

                if incident_number_match:
                    incident_number_result = incident_number_match.group()
                    output.append(incident_number_result)
                    line = line.replace(incident_number_result, '')
                if(line):
                    remaining_line = re.split(r'\s{2,}', line.strip())
                    if(len(remaining_line) == 3):
                        location = remaining_line[0]
                        output.append(location)
                        nature = remaining_line[1]
                        output.append(nature)
                        incident_ori = remaining_line[2]
                        output.append(incident_ori)

                if(not (len(output) < 5)):
                    row_list.append(output)
        return row_list

def createdb():
    database_path = os.path.join('resources', 'normanpd.db')
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    drop_table = ''' DROP TABLE IF EXISTS incidents; '''
    create_table = '''
        CREATE TABLE  incidents (
            incident_time TEXT,
            incident_number TEXT,
            incident_location TEXT,
            nature TEXT,
            incident_ori TEXT
        );
    '''
    cursor.execute(drop_table)
    cursor.execute(create_table)
    connection.commit()
    connection.close()

def populatedb(db, incidents):
    database_path = os.path.join('resources', 'normanpd.db')
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    for row in incidents:
        print(row)
        cursor.execute('INSERT INTO incidents (incident_time, incident_number, incident_location, nature, incident_ori) VALUES (?, ?, ?, ?, ?)', row)
    connection.commit()
    connection.close()

def status(db):
    database_path = os.path.join('resources', 'normanpd.db')
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    cursor.execute('''
        SELECT nature, COUNT(*) as count
        FROM incidents
        GROUP BY nature
        ORDER BY count DESC, nature
    ''')
    print("Nature|Count")
    for row in cursor.fetchall():
        nature, count = row
        print(f"{nature}|{count}")
    connection.close()
