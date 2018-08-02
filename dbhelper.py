import sqlite3


class DBHelper:

    def __init__(self, dbname="meddb.db"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)
       
    
    #tblstmt = "CREATE TABLE IF NOT EXISTS medicine(dis TEXT PRIMARY KEY, med TEXT)"

    def get_med(self, disease):
	#global sql
	con = sqlite3.connect("meddb.db")
    	cur = con.cursor()
        cur.execute("SELECT med FROM medicine WHERE dis = ?",(disease,))
    	rows = cur.fetchall()
	for row in rows:
		 return ' '.join(row)
