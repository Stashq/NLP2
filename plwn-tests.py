import plwn
from sqlalchemy import create_engine
engine = create_engine("mysqldb://wordnet:wordnet@localhost/wordnet_new?charset=utf8")

print(help(plwn))

api = plwn.load("/home/stachu/Downloads/wordnet-work.LATEST.sql", "sqlite3")#("connection.txt", "database", "plwn-new.db", "sqlite3")
print(api)