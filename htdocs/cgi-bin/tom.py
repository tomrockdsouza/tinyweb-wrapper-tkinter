
# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 



print("Content-Type: text/html\n\n<!DOCTYPE html><html>Hello</html>")