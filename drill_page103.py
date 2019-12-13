
import sqlite3

import os



conn = sqlite3.connect("test.db")

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_info( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_txt TEXT)")
    conn.commit()
conn.close()




conn = sqlite3.connect("test.db")

with conn:
    fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
    for file in fileList:
        name,ext = os.path.splitext(file)
        if ext == ".txt":
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_info (col_txt) VALUES (?)", (file,))
conn.commit()

cur.execute("SELECT col_txt FROM tbl_info")
txtList = cur.fetchall()
i=1
for sub in txtList:
    string = "The file {} is: ".format(i) +''.join(sub)
    print(string)
    i+=1
conn.close()



