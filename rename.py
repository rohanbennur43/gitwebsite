import os
dir='channel_281/priority'
files=os.listdir(dir)


def join_file(temp_file):
  temp=""
  for i in temp_file:
    temp=temp+i+'_'
  return temp[:-1]


def rename(file,showid):
    print('file:',file)
    temp_file=file.split('_')
    file=os.path.join(dir,file)
    temp_file[4]=showid
    renamed_file=join_file(temp_file)
    print('renamed_file:',renamed_file)
    renamed_file=os.path.join(dir,renamed_file)
    os.rename(file,renamed_file)

showid='ID00000000'
rename('DOC0872426442_SEQ0311072867_CH281_20220504_ID6061663703_add_c1cf37ec-22a3-4187-8ae6-d8f14870d9a7.xml',showid)