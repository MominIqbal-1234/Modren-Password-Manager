import sqlite3
import hidden
database_name = "pass_manager.dll"
class database:
    def create():
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS `auth_user` (id INTEGER PRIMARY KEY,username TEXT,password TEXT,status TEXT)")
        cursor.execute("CREATE TABLE IF NOT EXISTS `pass_info` (id INTEGER PRIMARY KEY,url TEXT,username TEXT,password TEXT)")
        cursor.execute("CREATE TABLE IF NOT EXISTS `webview` (id INTEGER PRIMARY KEY,runtimewebview TEXT)")
        cursor.close()
    def insert():
        conn = sqlite3.connect(database_name)
        command = (f"INSERT INTO auth_user (username,password,status) VALUES \
                         ('gAAAAABizLJcf-RvVa9v8X2wkGp8DYoH1SiuYvhhmW2Gin6MAlQfBba_mKhG5mXFRkjtRsX84cEiwJCXMhNOnvKz6LMWe9uOig==','gAAAAABizLJcf-RvVa9v8X2wkGp8DYoH1SiuYvhhmW2Gin6MAlQfBba_mKhG5mXFRkjtRsX84cEiwJCXMhNOnvKz6LMWe9uOig==','gAAAAABjc9o6O1PRUcQHFf2m8zrNxPs0JQw_6-ht6v2pM2o2RzUcqK55dw6CZn8Gfoi_YFaHDkfaOZ8YUb4cwPIVOddJB-7iCw==')")
        cursor = conn.cursor()
        conn.execute(command)    
        conn.commit()
        conn.close()
        print("username : admin")
        print("password : admin")
    def update_host(username1,password1):
        username = str(username1)
        password = str(password1)
        username_2 = username[1:].replace("'","")
        password_2 = password[1:].replace("'","")
        con = sqlite3.connect(database_name)
        cur = con.cursor()
        cur.execute(f'''UPDATE auth_user SET username = '{username_2}',password = '{password_2}' WHERE id = '1'; ''')                       
        con.commit()
        con.close()

    def update_status(status):
        status = str(status)
        status2 = status[1:].replace("'","")
        con = sqlite3.connect(database_name)
        cur = con.cursor()
        cur.execute(f'''UPDATE auth_user SET status = '{status2}' WHERE id = '1'; ''')                       
        con.commit()
        con.close()

    def updata_webview(boolen):
        con = sqlite3.connect(database_name)
        cur = con.cursor()
        cur.execute(f'''UPDATE webview SET runtimewebview = '{boolen}' WHERE id = '1' ''')                       
        con.commit()
        con.close()
    def insert2(url,username,password):
        try:

            url = str(url)
            username = str(username)
            password = str(password)

            url_2 = url[1:].replace("'","")
            username_2 = username[1:].replace("'","")
            password_2 = password[1:].replace("'","")

            conn = sqlite3.connect(database_name)
            cursor = conn.cursor()
            cursor.execute(f'''INSERT INTO pass_info (url,username,password) VALUES('{url_2}','{username_2}','{password_2}')''') 
            conn.commit()
            conn.close()
            return True
        except:
            return False
    def insert_login(username1,password1): 
        conn = sqlite3.connect(database_name)
        command = (f"INSERT INTO auth_user (username,password) VALUES \
                         ('{username1}','{password1}')")
        cursor = conn.cursor()
        conn.execute(command)    
        conn.commit()
        conn.close()
        
    def delete(id):
        conn = sqlite3.connect(database_name) 
        conn.execute(f'DELETE FROM pass_info WHERE id= {id}')
        conn.commit()
        conn.close()


    def update_info(url,username,password,id):
        try:
            url = str(url)
            username = str(username)
            password = str(password)

            url_2 = url[1:].replace("'","")
            username_2 = username[1:].replace("'","")
            password_2 = password[1:].replace("'","")

            conn = sqlite3.connect(database_name)
            cursor = conn.cursor()
            cursor.execute(f'''UPDATE pass_info SET url = '{url_2}',username = '{username_2}',password = '{password_2}'  WHERE id = '{id}'; ''') 
            conn.commit()
            conn.close()
            return True
        except:
            return False




if __name__ == '__main__':
    database.create()
    database.insert()

