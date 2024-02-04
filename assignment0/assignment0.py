import urllib.request
import io
import re
from pypdf import PdfReader

def fetchincidents(url):
       url = (url)
       headers = {}
       headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"                          

       data = urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read()  
       return io.BytesIO(data)                                                                         

def extractincidents(data):
        row_list = []
        reader = PdfReader(data)
        print(len(reader.pages))
        for page_num in range(len(reader.pages)):
            page = reader._get_page(page_num)
            page_text = page.extract_text()
            lines = page_text.split("\n")
            for line in lines:
                pattern = r'([\d/]+ [\d:]+) (\S+) (\S+) (.+?) ([^\s]+) (\S+) (\S+)'
                match = re.match(pattern, line.strip())
                if match:
                    groups = match.groups()
                    groups = list(groups)
                    groups[4] = ' '.join(groups[4:6])
                    groups.pop(5) 
                    row_list.append(groups)
        print(row_list)
        #page = reader.pages[0]
        #print(page.extract_text()) # Shows the extracted text