# I am covering same concept of string
banner = "FreeFloat FTP Server"
# convert data in upper case
print(banner.upper())

# convert data in lower case
print(banner.lower())

# replace data with other data
print(banner.replace('FreeFloat', 'Hacking'))

# traverse of data at exact position
print(banner.find('FTP'))

# traverse of file location
logFile = "/var/log/message"
print(logFile[3])
print(logFile[1:4])
print(logFile[-8])
print(logFile.split("/"))

# string	Concatenation
server_name = "https://"
website_name = "github"
domain_name = ".com"
website = server_name + website_name + domain_name
print(website)

server = "https:"
portNumber = "80"
url = "".join([server, "port number", portNumber])
print(url)
