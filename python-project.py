""" 
Howdy, we are group 7.
This python project is designed to parse and analyze log files from an Apache web server in order to provide insightful analytics to make business decisions.
Below is oue program design.
""" 

import http_access_log.txt

file = open("http_access_log.txt","r")
data = file.read()
total_occurences = data.count("get")
print("Number of total requests in the log:", total_occurences)
