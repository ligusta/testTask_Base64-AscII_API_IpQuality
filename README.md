# Test Task: Working with Base64 encoding and IpQuality API

Task:
<br/>
1. In the file you need to take a list of base64-encoded ip addresses
2. Register on www.ipqualityscore.com , get api access (free)
3. Write a script that will run all ip through this service, collect all data in a csv file.

# Decision

1. TaskBASE64.py decodes the contents of cells in the file "b64.csv" and writes the decoded values to the file "list_ip.csv". As a result: the file "list_ip.csv" has a list of ip addresses.
2. Task API.py passes the value from the cells of the "list.ip.csv" file through the Ip Quality API and writes all the collected data to "list.csv". As a result: the file "list.csv" has a list of ip addresses and all the information on them.
