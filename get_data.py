import sqlite3
database_name = "pass_manager.dll"
def login():
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute(f'''SELECT * from auth_user''')
    result = cursor.fetchone()
    return result

def view_user():
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute('''SELECT * from pass_info''')
    result = cursor.fetchall()
    return result

def view(id):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute(f'''SELECT * from pass_info where id = '{id}' ''')
    result = cursor.fetchone()
    return result

def status():
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute(f'''SELECT * from auth_user ''')
    # cursor.execute(f'''SELECT * from auth_user where id = '1' ''')
    result = cursor.fetchone()
    return result

def webview():
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    # cursor.execute(f'''SELECT * from webview ''')
    cursor.execute(f'''SELECT * from webview where id = '1' ''')
    result = cursor.fetchone()
    return result

