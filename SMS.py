from tkinter import *
import random
from tkinter import messagebox
from tkinter import scrolledtext
root = Tk()
root.title("SMS")
root.geometry("500x400+500+200")
root.resizable(False,False)
#root.configure(background = "sky blue")

addsms = Toplevel(root)
addsms.title("Add")
addsms.geometry("500x400+500+200")
addsms.resizable(False,False)
addsms.withdraw()
lblrno = Label(addsms,text="Enter roll no",width=10)
lblrno.pack(pady=10)
entrno = Entry(addsms,bd=7)
entrno.pack(pady=5)
def f17():
	v1=entmarks.get()
	v2=entname.get()
	try:
		i = int(entrno.get())
		if i < 0:
			messagebox.showwarning("roll no","Wrong:Positive Integer expected")	
	except ValueError as e:
		messagebox.showwarning("roll no","Wrong:Integer expected")	
	if not v1.isdigit():
		messagebox.showwarning("marks","Wrong:Integer expected")
	try:
		if not 0 <= int(v1) <= 100:
			messagebox.showwarning("Marks","Wrong:Invalid data! Enter marks between(0-100)")		
	except ValueError as e:
		pass
	if not v2.isalpha():
		messagebox.showwarning("Name","Wrong:Only strings")
	
	if not len(v2) == 2:
		messagebox.showwarning("Name","Length should be 2 characters")	

rno1=addsms.register(f17)
entrno.config(validate="key",validatecommand=(rno1,'%P'))
lblname = Label(addsms,text="Enter name",width=10)
lblname.pack(pady=10)
entname = Entry(addsms,bd=7)
entname.pack(pady=5)
lblmarks = Label(addsms,text="Enter marks",width=10)
lblmarks.pack(pady=10)
entmarks = Entry(addsms,bd=7)
entmarks.pack(pady=10)
#entrno.focus_set()
def f2():
	entrno.delete(0,END)
	entname.delete(0,END)	
	entmarks.delete(0,END)
	addsms.withdraw()
	root.deiconify()
btnaddback = Button(addsms,text="Back",command=f2,width=10)
btnaddback.place(x=210,y=320)

def f1():
	addsms.deiconify()
	root.withdraw()
btnadd = Button(root,text ="Add",command = f1,width=10)
btnadd.pack(pady=20)

def f10():
	updatesms.deiconify()
	root.withdraw()
btnupdate = Button(root,text ="Update",command=f10,width=10)
btnupdate.pack(pady=20)

def f5():
	deletesms.deiconify()
	root.withdraw()
btndelete = Button(root,text ="Delete",command=f5,width=10)
btndelete.pack(pady=20)
def f8():
	graphsms.deiconify()
	root.withdraw()
btngraph = Button(root,text ="Graph",command=f8,width=10)
btngraph.pack(pady=20)

'''import bs4
import requests
res=requests.get("https://www.brainyquote.com/quotes_of_the_day.html")
soup = bs4.BeautifulSoup(res.text,'lxml')
quote = soup.find('img',{"class":"p-qotd"})'''
#print(quote)
#msg = quote['alt']
#print(msg)
lblquote = Label(root,text="Quote",width=10)
lblquote.place(x=10,y=340)
quotes =["Never stop looking up.","laughter is best medicine.","Dream bigger.","Your limitation- it's only your imagination.","Sometimes later becomes never.Do it now.","Dream it.Wish it.Do it.","Don't stop when you're tired.Stop when you're done."]
r = random.randrange(len(quotes))
lbltext = Label(root,text=quotes[r])
lbltext.place(x=70,y=340)

lbltemp = Label(root,text="Temp",width=10)
lbltemp.place(x=10,y=370)
import socket
import requests
try:
	socket.create_connection(("www.google.com",80))
	temperature=[]
	res = requests.get("https://ipinfo.io")
	data =res.json()
	city = data['city']
	a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
	a2 = "&q=" + city
	a3 = "&appid=c6e315d09197cec231495138183954bd"
	api_address = a1 + a2 + a3
	res = requests.get(api_address)
	data = res.json()
	temp = data['main']['temp']
	lbltext2 = Label(root,text=temp)
	lbltext2.place(x=70,y=370)
except OSError as e:
	print("check error",e)
#lbltext2.pack(pady=20)

def f3():

	import cx_Oracle
	con = None
	cursor = None
	try:
		con = cx_Oracle.connect("system/abc123")
		print("u r connected")
		cursor = con.cursor()
		sql = "insert into sms values('%d', '%s','%d')"
		rno = int(entrno.get())
		name = entname.get()
		marks = int(entmarks.get())
		args = (rno,name,marks)
		cursor.execute(sql % args)
		con.commit()
		msg = str(cursor.rowcount) + " records insrted "
		messagebox.showinfo("Success", msg )
		entrno.delete(0,END)
		entname.delete(0,END)	
		entmarks.delete(0,END)
	except cx_Oracle.DatabaseError as e:
		con.rollback()
		messagebox.showerror("Failure",e)
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
		
btnsave = Button(addsms,text="Save",width=10,command=f3)
btnsave.place(x=210,y=270)

viewsms = Toplevel(root)
viewsms.title("View S")
viewsms.geometry("500x400+500+200")
viewsms.resizable(False,False)
viewsms.withdraw()
def f5():
	viewsms.withdraw()
	root.deiconify()
	st.delete('1.0',END)
st = scrolledtext.ScrolledText(viewsms,width=60,height=5)
btnviewback = Button(viewsms,text="Back",command=f5,width=10)
st.pack(pady=10)
btnviewback.place(x=210,y=320)

def f4():
	viewsms.deiconify()
	root.withdraw()
	import cx_Oracle
	con = None
	cursor = None
	try:
		con = cx_Oracle.connect("system/abc123")
		#print("u r connected")
		cursor = con.cursor()
		sql = "select rno,name,marks from sms"
		cursor.execute(sql)
		data = cursor.fetchall()
		mdata = ""
		for d in data:
			mdata = mdata + str(d[0]) + " " + d[1] + " " + str(d[2]) + "\n"
		st.insert(INSERT, mdata)
	except cx_Oracle.DatabaseError as e:
		con.rollback()
		print("Issue ",e)
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
			print("ur disconnected")

btnview = Button(root,text ="View",width=10,command=f4)
btnview.pack(pady=20)

deletesms = Toplevel(root)
deletesms.title("View S")
deletesms.geometry("500x400+500+200")
deletesms.resizable(False,False)
deletesms.withdraw()
lbldelrno = Label(deletesms,text="Enter roll no",width=10)
lbldelrno.pack(pady=10)
entdelrno = Entry(deletesms,bd=7)
entdelrno.pack(pady=5)
def f6():
	deletesms.withdraw()
	root.deiconify()

def f7():
	ret=f19()
	if ret==0:
		import cx_Oracle
		con = None
		cursor = None
		try:
			con = cx_Oracle.connect("system/abc123")
			#print("u r connected")
			cursor = con.cursor()
			sql = "delete from sms where rno = %d"
			rno = int(entdelrno.get())
			data = (rno,)
			cursor.execute(sql%data)
			con.commit()
			msg = str(cursor.rowcount) + " record deleted "
			messagebox.showinfo("Success", msg )
			entdelrno.delete(0,END)
		except cx_Oracle.DatabaseError as e:
			print("Issue ",e)
		finally:
			if cursor is not None:
				cursor.close()
			if con is not None:
				con.close()
				print("ur disconnected")
	
btndel = Button(deletesms,text="Delete",command=f7,width=10)
btndel.pack(pady=10)	
btndelback = Button(deletesms,text="Back",command=f6,width=10)
btndelback.pack(pady=10)

updatesms = Toplevel(root)
updatesms.title("Update S")
updatesms.geometry("500x400+500+200")
updatesms.resizable(False,False)
updatesms.withdraw()
lblurno = Label(updatesms,text="Enter roll no",width=10)
lblurno.pack(pady=10)
enturno = Entry(updatesms,bd=7)
enturno.pack(pady=5)
lbluname = Label(updatesms,text="Enter name",width=10)
lbluname.pack(pady=10)
entuname = Entry(updatesms,bd=7)
entuname.pack(pady=5)
lblumarks = Label(updatesms,text="Enter marks",width=10)
lblumarks.pack(pady=10)
entumarks = Entry(updatesms,bd=7)
entumarks.pack(pady=10)

def f11():
	ret=f16()
	ret2=f18()
	if ret==0:
		if ret2==0:
			import cx_Oracle
			con = None
			cursor = None
			try:
				con = cx_Oracle.connect("system/abc123")
				print("u r connected")
				cursor = con.cursor()
				sql = "update sms set name='%s',marks=%d  where rno=%d "
				name = entuname.get()
				marks = int(entumarks.get())
				rno = int(enturno.get())
				data = (name,marks,rno)
				cursor.execute(sql%data)
				con.commit()
				msg = str(cursor.rowcount) + " record updated "
				messagebox.showinfo("Success", msg )
				enturno.delete(0,END)
				entuname.delete(0,END)	
				entumarks.delete(0,END)
			except cx_Oracle.DatabaseError as e:
				con.rollback()
				messagebox.showerror("Failure",e)
			finally:
				if cursor is not None:
					cursor.close()
				if con is not None:
					con.close()
		
btnusave = Button(updatesms,text="Save",command=f11,width=10)
btnusave.pack(pady=10)

def f9():
	root.deiconify()
	updatesms.withdraw()
btnuback = Button(updatesms,text="Back",command=f9,width=10)
btnuback.pack(pady=10)

def f13():
	import matplotlib.pyplot as plt
	import numpy as np
	import cx_Oracle
	con = None
	cursor = None
	try:
		con = cx_Oracle.connect("system/abc123")
		cursor = con.cursor()
		cursor.execute("select rno,marks from sms")
		r =[]
		m=[]
		for row in cursor.fetchall():
			r.append(row[0])
			m.append(row[1])
		plt.bar(r,m)
		plt.title("Performance Analysis")
		plt.xlabel("Roll No")
		plt.ylabel("Marks")
		plt.grid()
		plt.show()
		con.commit()
	except cx_Oracle.DatabaseError as e:
		con.rollback()
		messagebox.showerror("Failure",e)
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
def f14():
	import matplotlib.pyplot as plt
	import numpy as np
	import cx_Oracle
	con = None
	cursor = None
	try:
		con = cx_Oracle.connect("system/abc123")
		cursor = con.cursor()
		cursor.execute("select rno,marks from sms")
		r =[]
		m=[]
		for row in cursor.fetchall():
			r.append(row[0])
			m.append(row[1])
		plt.plot(r,m)
		plt.title("Performance Analysis")
		plt.xlabel("Roll No")
		plt.ylabel("Marks")
		plt.grid()
		plt.show()
		con.commit()
	except cx_Oracle.DatabaseError as e:
		con.rollback()
		messagebox.showerror("Failure",e)
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
	
	
graphsms = Toplevel(root)
graphsms.title("Graph S")
graphsms.geometry("500x400+500+200")
graphsms.resizable(False,False)
graphsms.withdraw()
btnline = Button(graphsms,text="Line",command=f14,width=10)
btnbar = Button(graphsms,text="Bar",command=f13,width=10)
btnline.pack(pady=10)
btnbar.pack(pady=10)
def f12():
	graphsms.withdraw()
	root.deiconify()
btngback = Button(graphsms,text="Back",command=f12,width=10)
btngback.pack(pady=40)
	
def f15():
	if not entrno.get():
        		messagebox.showwarning("Roll no","Roll no is required")
	
	if not entname.get():
        		messagebox.showwarning("Name","Name is required")
	
	if not entmarks.get():
        		messagebox.showwarning("Marks","Marks are required")
	
def f16():
	if not enturno.get():
        		messagebox.showwarning("Roll no","Roll no is required")
	
	if not entuname.get():
        		messagebox.showwarning("Name","Name is required")
	
	if not entumarks.get():
        		messagebox.showwarning("Marks","Marks are required")

		
def f18():
	v1=entumarks.get()
	v2=entuname.get()
	try:
		i = int(enturno.get())
		if i < 0:
			messagebox.showwarning("roll no","Wrong:Positive Integer expected")	
	except ValueError as e:
		messagebox.showwarning("roll no","Wrong:Integer expected")	
	if not v1.isdigit():
		messagebox.showwarning("marks","Wrong:Integer expected")
	try:
		if not 0 <= int(v1) <= 100:
			messagebox.showwarning("Marks","Wrong:Invalid data! Enter marks between(0-100)")		
	except ValueError as e:
		pass
	if not v2.isalpha():
		messagebox.showwarning("Name","Wrong:Only strings")
	
	if not len(v2) == 2:
		messagebox.showwarning("Name","Length should be 2 characters")	
		
def f19():
	try:
		i = int(entdelrno.get())
		if i < 0:
			messagebox.showwarning("roll no","Wrong:Positive Integer expected")	
	except ValueError as e:
		messagebox.showwarning("roll no","Wrong:Integer expected")	

'''def f20(entrno):
	try:
		v=entrno.get()
		if not len(v) == 0:
			messagebox.showwarning("Rno","This field is required")	
			entname.config(state='disabled')
			entrno.focus_set()
	
	except ValueError as e:
		pass
valid_f20=addsms.register(f20)
entrno.config(validate="key",validatecommand=(valid_f20,'%P'))'''
root.mainloop()