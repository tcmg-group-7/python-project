# import http_access_log.txt

from urllib.request import urlretrieve

url='https://s3.amazonaws.com/tcmg476/http_access_log'
local='localcopy.log'

local, headers=urlretrieve(url, local)
file=open('local',r)

sixmonths=0
count=0

may="May"
jun="Jun"
jul="Jul"
aug="Aug"
sep="Sep"
october="Oct"
date="1995
nov="Nov"
dec="Dec"
jan="Jan"
mar="Mar"
apr="Apr"

data=file.read()
datalines=data.split('\n')


for line in datalines:
  if len(datalines) < 5:
    continue
  else:
    if may in datalines[count]:
      sixmonths +=1
    if jun in datalines[count]:
      sixmonths +=1
    if jul in datalines[count]:
      sixmonths +=1
    if aug in datalines[count]:
      sixmonths +=1
    if sep in datalines[count]:
      sixmonths +=1
    if october in datalines[count]:
      if date in datelines[count]:
        sixmonths +=1
    if nov in datalines[count]:
    if dec in datalines[count]:
    if jan in datalines[count]:
    if mar in datalines[count]:
    if apr in datalines[count]:
    count +=1
    
print("There were" + str(count) + "requests in total.")
print("There were" +str(sixmonths) + "requests in the last six months.")
    
