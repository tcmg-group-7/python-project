import http_access_log.txt

file = open("http_access_log.txt","r")
data = file.read()
total_occurences = data.count("get")
print("Number of total requests in the log:", total_occurences)
