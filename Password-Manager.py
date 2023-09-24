import subprocess
from flask import Flask,render_template,request,redirect,flash
import webview
import get_data
import hidden
import database
import pyperclip
from tkinter import *
from tkinter import messagebox
import os
from tkinter import filedialog
import shutil

# pip install pythonnet==3.0.0a2
# pip install clr-loader==0.1.7



software_id = 98402
software_version = 1.0
software_name = "Password Manager"

app = Flask(__name__, static_folder='./static',template_folder='./templete')
app.secret_key = "__secret_key__"  





@app.route('/import_backup' , methods =["GET", "POST"])
def import_backup():
    gui_win = Tk()
    gui_win.withdraw()
    gui_win.iconbitmap('icon.ico')
    try:
        filename = filedialog.askopenfilename(filetypes=[('Dll', '*.dll')])
        shutil.copy(filename,"pass_manager.dll")
        msg = messagebox.showinfo("Success", "Import Backup successful \t")
    except:
        pass
    gui_win.destroy()
    gui_win.mainloop()
    return redirect('/')

@app.route('/export_backup' , methods =["GET", "POST"])
def export_backup():
    gui_win = Tk()
    gui_win.withdraw()
    gui_win.iconbitmap('icon.ico')
    try:
        folder_selected = filedialog.askdirectory()
        shutil.copy("pass_manager.dll",folder_selected)
        msg = messagebox.askquestion("Success", "Open Back-up Folder \t")
        if msg == "yes":
            os.startfile(folder_selected)
    except:
        pass
    gui_win.destroy()
    gui_win.mainloop()
    return redirect('/')


  



@app.route('/change_password' , methods =["GET", "POST"])
def change_password():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        username1 = hidden.hide.encode_message(username)
        password1 = hidden.hide.encode_message(password)
        database.database.update_host(username1, password1)
        message = 'User Update Successful'
        return render_template('change_password.html',message=message,username=username,password=password)
       
        
    user = get_data.login()

    username = hidden.hide.decode_message(user[1])
    password = hidden.hide.decode_message(user[2])

    return render_template('change_password.html',username=username,password=password)



@app.route('/logout' , methods =["GET", "POST"])
def logout():
    value = hidden.hide.encode_message('2193037900')
    database.database.update_status(value)
    return redirect('/')



@app.route('/' , methods =["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        data = get_data.login()
        encode_data1 = str(data[1])
        encode_data2 = str(data[2])
        username1 = hidden.hide.decode_message(encode_data1)
        password1 = hidden.hide.decode_message(encode_data2)
    
        if username == username1 and password == password1:
            value = hidden.hide.encode_message('1979598841')
            database.database.update_status(value)
            return render_template("index.html")
           
        message = 'Wrong Username and Password'
        return render_template("login.html",message=message)
        
    status = get_data.status()
    value = hidden.hide.decode_message(status[3])
    if value == '1979598841':
        return redirect('/save_data')
    return render_template("login.html")


@app.route('/save_data' , methods =["GET", "POST"])
def save_data():
    if request.method == 'POST':
        url = request.form['url']
        username = request.form['username']
        password = request.form['password']
        
        url1 = hidden.hide.encode_message(url)
        username1 = hidden.hide.encode_message(username)
        password1 = hidden.hide.encode_message(password)

        value = database.database.insert2(url1, username1, password1)
        if value == True:
            message = 'Data Submit'
        else:
            message = 'Data Not Sibmit'

        return render_template("index.html",message=message)
        
    return render_template("index.html")
   




@app.route('/view_user')
def view_user():
    value = get_data.view_user()
    mydict  = {}
    for i in value:
        encode_data2 = str(i[1])
        id = str(i[0])
        value1 = hidden.hide.decode_message(encode_data2)
        mydict1 = {id:value1}
        mydict.update(mydict1)
        parent_list = [mydict]
    if value == []:
        
        return render_template("view_user.html")
   

    return render_template("view_user.html",parent_list=parent_list)

    


@app.route('/view/<user_id>')
def view(user_id):
    
    value = get_data.view(user_id)
    
    url = hidden.hide.decode_message(value[1])
    username = hidden.hide.decode_message(value[2])
    password = hidden.hide.decode_message(value[3])
    return render_template("view.html",url=url,username=username,password=password,user_id=user_id)
    
  



@app.route('/copy' , methods =["GET", "POST"])
def copy():
    if request.method == 'POST':
        copy_value = request.form['copy_value']
        user_id = request.form['user_id']
       

        value = get_data.view(user_id)
        url = hidden.hide.decode_message(value[1])
        username = hidden.hide.decode_message(value[2])
        password = hidden.hide.decode_message(value[3])
        pyperclip.copy(copy_value)
        message = 'Copied!'
        return render_template("view.html",
                               url=url,
                               username=username,
                               password=password,
                               user_id=user_id,
                               message=message)
      


@app.route('/delete/<myid>')
def delete(myid):
    gui_win = Tk()
    gui_win.withdraw()
    gui_win.iconbitmap('icon.ico')
    
    msg  = messagebox.askquestion("Message", "Are You Sure Delete Password \t")
    if msg =='yes':
        database.database.delete(myid)
    gui_win.destroy()
    gui_win.mainloop()
    return redirect('/view_user')
    

@app.route('/mission')
def mission():
    return render_template("mission.html")
    



@app.route('/edit_info/view/<user_id>',methods =["GET"])
def edit_info_view(user_id):
    value = get_data.view(user_id)
    url = hidden.hide.decode_message(value[1])
    username = hidden.hide.decode_message(value[2])
    password = hidden.hide.decode_message(value[3])
    return render_template("edit_info.html",url=url,username=username,password=password,user_id=user_id)
   

@app.route('/edit_info/update',methods =["GET", "POST"])
def edit_info_update():
    if request.method == 'POST':
        url = request.form['url']
        username = request.form['username']
        password = request.form['password']
        id = request.form['id']
        url1 = hidden.hide.encode_message(url)
        username1 = hidden.hide.encode_message(username)
        password1 = hidden.hide.encode_message(password)

        value = database.database.update_info(url1, username1, password1,id)
        if value == True:
            flash("Data Submit")
        else:
            flash("Data Not Sibmit")
        
        return redirect(f'/edit_info/view/{id}')



if __name__ == '__main__':
    window = webview.create_window('Password-Manager - Save and Secure | mefiz.com', app,resizable=False,text_select=False,min_size=(800, 600))
    webview.start(debug=False,http_server=False)
