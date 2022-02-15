# import http_access_log.txt

from urllib.request import urlretrieve

url='https://s3.amazonaws.com/tcmg476/http_access_log'
local='localcopy.log'

local, headers=urlretrieve(url, local)
file=open(local,'r')

sixmonths=0
count=0

may="May"
jun="Jun"
jul="Jul"
aug="Aug"
sep="Sep"
october="Oct"
date="1995"
nov="Nov"
dec="Dec"
jan="Jan"
feb="Feb"
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
      sixmonths +=1
    if nov in datalines[count]:
      sixmonths +=1
    if dec in datalines[count]:
      sixmonths +=1
    if jan in datalines[count]:
      sixmonths +=1
    if feb in datalines[count]:
      sixmonths +=1
    if mar in datalines[count]:
      sixmonths +=1
    if apr in datalines[count]:
      sixmonths +=1
    count +=1
    
print(f"There were {count} requests in total.")
print(f"There were {sixmonths} requests in the last six months.")

