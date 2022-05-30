import os
from pathlib2 import Path

dir='channel_281/priority'
files=os.listdir(dir)


def replacetext(search,replace,cfile):
  cfile=str(os.path.join(dir,cfile))
  '''file=Path(file)
  
  data=file.read_text()
  data=data.replace(search,replace)
  file.write_text(data)
  print("replaced")
 '''

  with open(cfile, 'r') as file:
  
   
        data = file.read()
  
        data = data.replace(search, replace)

  with open(cfile, 'w') as file:
        file.write(data)
        file.flush()  

offset=2
replace=""
search=""
def find_date(file):
    with open(os.path.join(dir,file),'r') as f:
        data=f.readlines()
        temp="<SmpteDateTime broadcastDate="
        for line in data:
            if(temp in line):
                search=line.strip()
                date=int(str("".join(search.rsplit(temp)))[-4:-2])
                date=date+offset
                replace=search[0:-4]+str(date)+"\">"
                print(replace,search)
                break

file='DOC0871647107_SEQ0310901658_CH281_20220503_ID00000000_add_a321a182-ebf3-4285-9afe-d993a9f62337.xml'
find_date(file)
replacetext(replace,search,file)