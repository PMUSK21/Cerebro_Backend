import database.actions.query as query
import database.actions.create as create
import sqlite3

con = sqlite3.connect("database/commits.db")
con.row_factory = sqlite3.Row

CUR = con.cursor()
query.CUR = CUR
create.CUR = CUR

def commit() -> None:
    con.commit()