# import http_access_log.txt

file = open("http_access_log.txt","r")
data = file.read()
total_occurences = data.count("get")
print("Number of total requests in the log:", total_occurences)

october= data.count("Oct/1994")
november= data.count("Nov/1994")
december= data.count("Dec/1994")
january= data.count("Jan/1995")
february= data.count("Feb/1995")
march= data.count("Mar/1995")

sixmonth= (october + november + december + january + february + march)

print("Number of requests during the first 6 months:", sixmonth)
