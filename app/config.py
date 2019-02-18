import MySQLdb 


#connecting to the DB
db = MySQLdb.connect(host="localhost",  # your host 
                     user="root",       # username
                     passwd='1234',     # password
                     db="cloudinn",     # name of the database
                     )  
