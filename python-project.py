import http_access_log.txt

file = open("http_access_log.txt","r")
data = file.read()
total_occurences = data.count("get")
print("Number of total requests in the log:", total_occurences)

october= data.count("oct/1994")
november= data.count("nov/1994")
december= data.count("dec/1994")
january= data.count("jan/1995")
february= data.count("feb/1995")
march= data.count("mar/1995")

sixmonth= sum(october, november, december, january, february, march)

print("Number of requests during the first 6 months:", sixmonth)
