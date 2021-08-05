from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter.ttk import *
import sqlite3
import os.path
from os import path
import time
import datetime
from dateutil.parser import parse
from tkcalendar import Calendar, DateEntry
def bank():	
	


	splash=Tk()
	splash.geometry("500x520+500+100")
	splash.config(bg="#000000")
	splash.overrideredirect(True)
	splash_label=Label(splash,background="black",foreground="#ffffff",text="SCAM BANK",font=("Helvatica",20)).pack(pady=20)
	splash_label=Label(splash,background="black",foreground="#ffffff",text="+888,000 had been scammed ",font=("Helvatica",10)).pack(pady=20)
	splash_label=Label(splash,background="black",foreground="#ffffff",text="FOUNDER/CEO: Mayank Kumar",font=("Helvatica",10)).pack(pady=20)
	splash_label=Label(splash,background="black",foreground="#ffffff",text="MANAGER:Aniket Shandilya",font=("Helvatica",10)).pack(pady=20)
	splash_label=Label(splash,background="black",foreground="#ffffff",text="LICENCE:Aryan Aman",font=("Helvatica",10)).pack(pady=20)
	splash_label=Label(splash,background="black",foreground="#ffffff",text="INVESTMENT:Akash Gupta",font=("Helvatica",10)).pack(pady=20)
	splash_label=Label(splash,background="black",foreground="#ffffff",text="MARKETED BY:Raju Kumar",font=("Helvatica",10)).pack(pady=20)
	splash_label=Label(splash,background="black",foreground="#ffffff",text="TOTAL  $SCAMED:  $948,459,298,749.73",font=("Comic Sans Ms",15)).pack(pady=20)

	def main_21():
			#splash.destroy()
			screen_size = Tk()

			screen_size.title("SCAM INTERNATIONAL BANK")
			screen_size.geometry("500x500+500+100")
			screen_size.resizable(width=False, height=False)
			#screen_size.iconphoto(False, PhotoImage(file='icon.ico.png'))
			screen_size.config(bg='#99ffcc')


			if (os.access('Account123456_detail.db', os.F_OK)== False):#check database exist or not(action -->true & false)
			#database
				conn=sqlite3.connect('Account123456_detail.db')
				

				c=conn.cursor()

				#create table
				c.execute(""" CREATE TABLE account_holder(
									name text NOT NULL,
									phone_num integer NOT NULL ,
									dob integer NOT NULL,
									aadhar integer NOT NULL,
									acc_typ text NOT NULL,
									open integer NOT NULL,
									acc_num_id text PRIMARY KEY
									)""")

				conn.commit()
				conn.close()

			#open account


			def on_clicked():
			    new=Tk()
			    new.geometry("350x300+500+100")
			    new.resizable(width=False, height=False)
			   
			    name=Entry(new,width=30)
			    name.grid(row=0,column=1,padx=20)

			    phone=Entry(new,width=30)
			    phone.grid(row=1,column=1,padx=20)

			    dob=DateEntry(new,width=27,bg="darkblue",fg="white")
			    dob.grid(row=2,column=1,padx=20)

			    account_type=ttk.Combobox(new,width=27)
			    account_type['values']=("saving","current")
			    account_type.grid(row=3,column=1,padx=20)

			    Open_deposite=Entry(new,width=30)
			    Open_deposite.grid(row=4,column=1,padx=20)

			    aadhar_num=Entry(new,width=30)
			    aadhar_num.grid(row=5,column=1,padx=20)



			    name_label=Label(new,text="name")
			    name_label.grid(row=0,column=0)

			    phone_label=Label(new,text="phone number")
			    phone_label.grid(row=1,column=0)

			    dob_label=Label(new,text="date of birth")
			    dob_label.grid(row=2,column=0)

			    acc_type_label=Label(new,text="account type")
			    acc_type_label.grid(row=3,column=0)

			    op_dep_label=Label(new,text="Open deposite")
			    op_dep_label.grid(row=4,column=0)

			    aadhar_label=Label(new,text="aadhar")
			    aadhar_label.grid(row=5,column=0)
				    #print(mydate.strftime("%b").upper()+mydate.strftime("%d")+mydate.strftime("%Y")+mydate.strftime("%H")+mydate.strftime("%M")+mydate.strftime("%S")+mydate.strftime("%f"))
			    account_label=Label(new,text="Your Account Number")
			    account_label.grid(row=6,column=0)

			    mydate = datetime.datetime.now()
			    a1=(mydate.strftime("%b").upper())
			    a2=(mydate.strftime("%d"))
			    a3=(mydate.strftime("%Y"))
			    a4=(mydate.strftime("%H"))
			    a5=(mydate.strftime("%M"))
			    a6=(mydate.strftime("%S"))
			   # print("-------------------")
			    a7=(mydate.strftime("%f")[0:3])
			    a8=(mydate.strftime("%f"))
			    global af
			    af=str(a1+a2+a3+a4+a5+a6+a7+a8)
			    
			    account_number_label=Label(new,text=af).grid(row=6,column=1)
			    
			    def submit():
			    	#print(af)
			    	print(af)
			    	def is_date(string,fuzzy=False):
			    	 	try:
			    	 		parse(string,fuzzy=fuzzy)
			    	 		return True
			    	 	except ValueError:
			    	 		return messagebox.showwarning("date","invalid date")
			    	 		
			    	def is_type():
			    		lists=["saving","current"]
			    		if(account_type.get().lower() ==lists[0] or account_type.get().lower()==lists[1] ):
			    			return True
		    			else:
		    				messagebox.showwarning("error","choose either 'saving' or 'current' ")
			    	def adhr():
			    		if (len(aadhar_num.get())==12 and aadhar_num.get().isnumeric()):
			    			return True
		    			else:
		    				#print("addhar false")
		    				messagebox.showwarning("invalid","invalid aadhar number")
		    		def dep():
		    			if(Open_deposite.get().isnumeric()==True):
		    				#if(Open_deposite>1000):
		    					return True
	    					#else:
	    						#messagebox.showwarning("amount","deposite atleast 1000")
	    				else:
	    					messagebox.showwarning("invalid","incorrect amount")
			    	def is_phone():
			    		if (len(phone.get())==10):
			    			if((phone.get().isnumeric())==True):
			    				return True
		    			else:
		    				messagebox.showwarning("phone","invalid phone number")
			    	def is_name():
			    		if((any(map(str.isdigit,name.get())))==False):
			    			return False
			    		else:
			    			messagebox.showwarning("name","invalid name")
			    	if ((not name.get()) or (not phone.get()) or (not dob.get()) or (not account_type.get()) or (not Open_deposite.get()) or (not aadhar_num.get())):
			    		messagebox.showwarning("Warnning","Required fields might be empty")
			    		
			    	
			    	elif(is_date(dob.get())==True and is_name()==False and is_phone()==True and is_type()==True and adhr()==True and dep()==True):		    
				    	conn=sqlite3.connect('Account123456_detail.db')
				    	c=conn.cursor()

				    	'''c.execute(""" CREATE TABLE account_holder(
									name text,
									phone_num integer,
									dob integer,
									aadhar integer,
									acc_typ text,
									open integer
									)""")'''

				    	c.execute("INSERT INTO  account_holder VALUES(:name, :phone, :dob, :aadhar, :acc_typ, :open, :acc_num_id)",

				    			{
				    				'name':name.get(),
				    				'phone':phone.get(),
				    				'dob':dob.get(),
				    				'acc_typ':account_type.get().lower(),
				    				'open':Open_deposite.get(),
				    				'aadhar':aadhar_num.get(),
				    				'acc_num_id':af


				    			}
				    		)
				    	c.execute("SELECT *,oid FROM account_holder")
				    	a=c.fetchall()
				    	#print(a)
				    	name.delete(0,END)
				    	phone.delete(0,END)
				    	dob.delete(0,END)
				    	aadhar_num.delete(0,END)
				    	account_type.delete(0,END)
				    	Open_deposite.delete(0,END)
				    	conn.commit()
				    	conn.close()

			    '''def fetch():
			    	conn=sqlite3.connect('Account123456_detail.db')
			    	c=conn.cursor()
			    	c.execute("SELECT *,oid FROM account_holder")
			    	records=c.fetchall()
			    	

			    	print_records=''

			    	for record in records:
			    		print_records += str(record[6])+"\n"
			    		print(print_records)

			    	q_l=Label(new, text=print_records)
			    	q_l.grid(row=8,column=0,columnspan=2)
			    	conn.commit()
			    	conn.close()'''

			    btn=Button(new,text="submit",command=submit)
			    btn.grid(row=7,column=1,columnspan=2,ipadx=100,pady=10,padx=10)

			    '''fetch1=Button(new,text="fetch",command=fetch)
			    fetch1.grid(row=7,column=1,columnspan=2,ipadx=100,pady=10)'''

			# delete account
			def close_account():
				new1=Tk()
				new1.geometry("300x300+500+100")
				new1.resizable(width=False, height=False)
				global acc_id


				delete_label=Label(new1,text="account number")
				delete_label.grid(row=0,column=0)

				delet_account=Entry(new1)
				delet_account.grid(row=0,column=1)


				

				def delete():
					conn=sqlite3.connect('Account123456_detail.db')
					c=conn.cursor()

					#c.execute("DELETE FROM  account_holder WHERE oid= "+delet_account.get())
					x=("DELETE FROM account_holder WHERE acc_num_id=?")
					c.execute(x,[(delet_account.get())])



					conn.commit()
					conn.close()
					delet_account.delete(0,END)

				delete_button=Button(new1,text="delete account",command=delete)
				delete_button.grid(row=1,column=0)
			#account detail

			def account_detail():
				acc=Tk()
				acc.geometry("300x300+500+100")
				acc.resizable(width=False,height=False)


				acc_label=Label(acc,text="Account Number")
				acc_label.grid(row=0,column=0)
				acc_entry=Entry(acc)
				acc_entry.grid(row=0,column=1)
				def fetch():
				
					conn=sqlite3.connect('Account123456_detail.db')
					c=conn.cursor()
					#c.execute("SELECT * FROM account_holder WHERE oid="+acc_entry.get())
					y=("SELECT * FROM account_holder WHERE acc_num_id=?")
					c.execute(y,[(acc_entry.get())])
					records=c.fetchall()
					print_records=''
					for record in records:
						print_records+=str(record[0])+" "+str(record[3])+"\n"
						
					q_l=Label(acc, text=print_records)
					q_l.grid(row=3,column=0,columnspan=3)	
					conn.commit()
					conn.close() 

					#p_label=Label(acc,text=acc_entry.get())
					#p_label.grid(row=1,column=1)
				acc_sub_btn=Button(acc,text="Get Detail",command=fetch)
				acc_sub_btn.grid(row=0,column=2)

				
				


			    

			#update
			def up_date():
				update=Tk()
				update.geometry("400x300+500+100")
				update.resizable(width=False,height=False)




				def ma_in():
					conn=sqlite3.connect('Account123456_detail.db')
					c=conn.cursor()
					#c.execute("SELECT * FROM account_holder WHERE oid="+select_entry.get())
					y=("SELECT * FROM account_holder WHERE acc_num_id=?")
					c.execute(y,[(select_entry.get())])
					records=c.fetchall()

					global a
					global b
					global cd
					global d

					
					update_name_label=Label(update,text="Name",width=20).grid(row=1,column=0)
					a=Entry(update,width=30)
					a.grid(row=1,column=1)
					update_name_label=Label(update,text="Phone number",width=20).grid(row=2,column=0)
					b=Entry(update,width=30)
					b.grid(row=2,column=1)
					update_dob_label=Label(update,text="DOB",width=20).grid(row=3,column=0)
					cd=Entry(update,width=30)
					cd.grid(row=3,column=1)
					update_acc_type_label=Label(update,text="Account Type",width=20).grid(row=4,column=0)
					d=Entry(update,width=30)
					d.grid(row=4,column=1)
					print(select_entry.get())


					#conn=sqlite3.connect('Account123456_detail.db')
					#c=conn.cursor()
					
					for record in records:
						a.insert(0,record[0])
						b.insert(0,record[1])
						cd.insert(0,record[2])
						d.insert(0,record[4])

					
					
						
					conn.commit()
					conn.close()
					#label=Label(update,text=print_records).grid(row=4,column=1)
					def save_up():
						
						
						
						
						
						
						conn=sqlite3.connect('Account123456_detail.db')
						c=conn.cursor()

						c.execute("""UPDATE account_holder SET
							name= :a_name,
							phone_num= :b_phone,
							dob= :c_dob,
							acc_typ= :d_acc


							WHERE acc_num_id= :acc_num_id""",

							{

							'a_name':a.get(),
							'b_phone':b.get(),
							'c_dob':cd.get(),
							'd_acc':d.get(),
							'acc_num_id':select_entry.get()

							})

						conn.commit()
						conn.close()

					save_btn=Button(update,text='update',command=save_up).grid(row=6,column=2)

				select_label=Label(update,text="account number",width=20).grid(row=0,column=0,pady=10)
				global select_entry
				select_entry=Entry(update,width=30)
				select_entry.grid(row=0,column=1,pady=10)
					
				select_button=Button(update,text="edit",command=ma_in,width=10).grid(row=0,column=2,padx=10,pady=10)

			def deposite():
				update=Tk()
				update.geometry("400x300+500+100")
				update.resizable(width=False,height=False)




				def ma_in():

					conn=sqlite3.connect('Account123456_detail.db')
					c=conn.cursor()
					#x=("DELETE FROM account_holder WHERE acc_num_id=?")
					y=("SELECT * FROM account_holder WHERE acc_num_id=?")
					c.execute(y,[(select_entry.get())])
					records=c.fetchall()

					

					global cd
					#update_name_label=Label(update,text="Name",width=20).grid(row=1,column=0)
					#a=Entry(update,width=30)
					#a.grid(row=1,column=1)
					#update_name_label=Label(update,text="Phone number",width=20).grid(row=2,column=0)
					#b=Entry(update,width=30)
					#b.grid(row=2,column=1)
					update_dob_label=Label(update,text="amount",width=20).grid(row=3,column=0)
					cd=Entry(update,width=30)
					cd.grid(row=3,column=1)
					#update_acc_type_label=Label(update,text="Deposite Amount",width=20).grid(row=4,column=0)
					#d=Entry(update,width=30)
					#d.grid(row=4,column=1)
					print(select_entry.get())
					add=Label(update,text="deposite amount",width=20).grid(row=4,column=0)
					add1=Entry(update,width=30)
					add1.grid(row=4,column=1)

					


					#conn=sqlite3.connect('Account123456_detail.db')
					#c=conn.cursor()
					
					for record in records:
						#a.insert(0,record[0])
						#b.insert(0,record[1])
						cd.insert(0,record[5])
						#d.insert(0,record[4])

					
					
						
					conn.commit()
					conn.close()
					#label=Label(update,text=print_records).grid(row=4,column=1)
					def save_up():
						
						
						
						
						print(cd.get())
						print(add1.get())
						total=(float(cd.get())+float(add1.get()))
						print(total)
						q=select_entry.get()
						conn=sqlite3.connect('Account123456_detail.db')
						c=conn.cursor()

						c.execute("""UPDATE account_holder SET
							open= :a_name
							
							
							


							WHERE acc_num_id= :acc_num_id""",

							{

							
							
							'a_name':total,
							
							'acc_num_id':select_entry.get()

							})




							



						conn.commit()
						conn.close()

					save_btn=Button(update,text='deposite',command=save_up).grid(row=6,column=2)





				select_label=Label(update,text="account number",width=20).grid(row=0,column=0,pady=10)
				global select_entry
				select_entry=Entry(update,width=30)
				select_entry.grid(row=0,column=1,pady=10)
					
				select_button=Button(update,text="go",command=ma_in,width=10).grid(row=0,column=2,padx=10,pady=10)
						
						
						
						
							
						
						
						
						
					#sub3=Button(deposite,text='deposite',command=addition).grid(row=3,column=1)	#level=Label(deposite,text=c).grid(row=4,column=1)
					#print(sub1.get())
					#print(records+sub1.get())

			def withdraw():
				update=Tk()
				update.geometry("400x300+500+100")
				update.resizable(width=False,height=False)




				def ma_in():
					conn=sqlite3.connect('Account123456_detail.db')
					c=conn.cursor()
					#c.execute("SELECT * FROM account_holder WHERE oid="+select_entry.get())
					y=("SELECT * FROM account_holder WHERE acc_num_id=?")
					c.execute(y,[(select_entry.get())])
					records=c.fetchall()

					global a
					global b
					global cd
					global d

					
					#update_name_label=Label(update,text="Name",width=20).grid(row=1,column=0)
					#a=Entry(update,width=30)
					#a.grid(row=1,column=1)
					#update_name_label=Label(update,text="Phone number",width=20).grid(row=2,column=0)
					#b=Entry(update,width=30)
					#b.grid(row=2,column=1)
					update_dob_label=Label(update,text="amount",width=20).grid(row=3,column=0)
					cd=Entry(update,width=30)
					cd.grid(row=3,column=1)
					#update_acc_type_label=Label(update,text="Deposite Amount",width=20).grid(row=4,column=0)
					#d=Entry(update,width=30)
					#d.grid(row=4,column=1)
					print(select_entry.get())
					add=Label(update,text="withdraw amount",width=20).grid(row=4,column=0)
					add1=Entry(update,width=30)
					add1.grid(row=4,column=1)

					


					#conn=sqlite3.connect('Account123456_detail.db')
					#c=conn.cursor()
					
					for record in records:
						#a.insert(0,record[0])
						#b.insert(0,record[1])
						cd.insert(0,record[5])
						#d.insert(0,record[4])

					
					
						
					conn.commit()
					conn.close()
					#label=Label(update,text=print_records).grid(row=4,column=1)
					def save_up():
						
						
						
						
						print(cd.get())
						print(add1.get())
						if(float(cd.get())>float(add1.get())):
							total=(float(cd.get())-float(add1.get()))
							print(total)
						else:
							messagebox.showwarning("!Warnning","Insufficient Balance")
						conn=sqlite3.connect('Account123456_detail.db')
						c=conn.cursor()

						c.execute("""UPDATE account_holder SET
							open= :a_name
							
							
							


							WHERE acc_num_id= :acc_num_id""",

							{

							
							
							'a_name':total,
							
							'acc_num_id':select_entry.get()

							})




							



						conn.commit()
						conn.close()
						#update.destroy()

					save_btn=Button(update,text='withdraw',command=save_up).grid(row=6,column=2)






				select_label=Label(update,text="account number",width=20).grid(row=0,column=0,pady=10)
				global select_entry
				select_entry=Entry(update,width=30)
				select_entry.grid(row=0,column=1,pady=10)
					
				select_button=Button(update,text="go",command=ma_in,width=10).grid(row=0,column=2,padx=10,pady=10)
						
						
						
						
							
						
						
						
						
					#sub3=Button(deposite,text='deposite',command=addition).grid(row=3,column=1)	#level=Label(deposite,text=c).grid(row=4,column=1)
					#print(sub1.get())
					#print(records+sub1.get())

			button = Button(screen_size, text="Open New Account", command=on_clicked)
			button.grid(column=0, row=0,padx=10,pady=10)
			button.config(width=20)

			button_1 = Button(screen_size, text='Withdraw Amount',command=withdraw)
			button_1.config(width=20)
			button_1.grid(column=0, row=2,padx=10,pady=10)

			button_2 = Button(screen_size, text='Account Deatails',command=account_detail)
			button_2.config(width=20)
			button_2.grid(column=0, row=1,padx=10)

			button_2 = Button(screen_size, text='Update Account',command=up_date)
			button_2.config(width=20)
			button_2.grid(column=0, row=3,padx=10)

			button_3=Button(screen_size,text='Deposite Money',command=deposite)
			button_3.config(width=20)
			button_3.grid(column=0,row=4,padx=10,pady=10)

			button_4=Button(screen_size,text='Close Account',command=close_account)
			button_4.config(width=20)
			button_4.grid(column=0,row=5,padx=10)

			#show all record
			def all_garbage():
				

				garbage=Tk()
				garbage.geometry("1050x100+00+100")
				garbage.resizable(width=False,height=False)

				main_frame=Frame(garbage)
				main_frame.pack(fill=BOTH,expand=1)
				my_canvas=Canvas(main_frame)
				my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
				my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
				my_scrollbar.pack(side=RIGHT,fill=Y)
				my_canvas.configure(yscrollcommand=my_scrollbar.set)
				my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
				second_frame=Frame(my_canvas)
				my_canvas.create_window((0,0),window=second_frame,anchor="nw")

				conn=sqlite3.connect('Account123456_detail.db')
				c=conn.cursor()
				c.execute("SELECT *,oid FROM account_holder")
				records=c.fetchall()
				print_records=''
				print_records_1=''
				print_records_2=''
				print_records_3=''
				print_records_4=''
				print_records_5=''
				print_records_6=''
				print_records_7=''
				for record in records:
					print_records+=str(record[0])+"\n"
					print_records_1+=str(record[1])+"\n"
					print_records_2+=str(record[2])+"\n"
					print_records_3+=str(record[4])+"\n"
					print_records_4+=str(record[5])+"\n"
					print_records_5+=str(record[3])+"\n"
					print_records_6+=str(record[6])+"\n"
					print_records_7+=str(record[7])+"\n"
					

				q2_l=Label(second_frame, text='name',width=20).grid(row=0,column=0)	
				q2_l=Label(second_frame, text='phone_num',width=20).grid(row=0,column=1)
				q2_l=Label(second_frame, text='date_of_birth',width=20).grid(row=0,column=2)
				q2_l=Label(second_frame, text='account_type',width=20).grid(row=0,column=3)
				q2_l=Label(second_frame, text='amount',width=20).grid(row=0,column=4)
				q2_l=Label(second_frame, text='aadhar',width=20).grid(row=0,column=5)
				q2_l=Label(second_frame, text='account_number',width=40).grid(row=0,column=6)
				q2_l=Label(second_frame, text='data_id').grid(row=0,column=7)
				q_l=Label(second_frame, text=print_records,width=20)
				q_l.grid(row=1,column=0)
				q_l=Label(second_frame, text=print_records_1,width=20)
				q_l.grid(row=1,column=1)
				q_l=Label(second_frame, text=print_records_2,width=20)
				q_l.grid(row=1,column=2)
				q_l=Label(second_frame, text=print_records_3,width=20)
				q_l.grid(row=1,column=3)
				q_l=Label(second_frame, text=print_records_4,width=20)
				q_l.grid(row=1,column=4)
				q_l=Label(second_frame, text=print_records_5,width=20)
				q_l.grid(row=1,column=5)
				q_l=Label(second_frame, text=print_records_6,width=40)
				q_l.grid(row=1,column=6)
				q_l=Label(second_frame, text=print_records_7)
				q_l.grid(row=1,column=7)
				conn.commit()
				conn.close()	

			button_5=Button(screen_size,text='show all record',command=all_garbage)
			button_5.config(width=20)
			button_5.grid(column=0,row=6,padx=10,pady=10)

	#def main_login():
	#login and logup is done no need to interfare

	if (os.access('bird.db', os.F_OK)== False):
		con=sqlite3.connect('bird.db')
		c=con.cursor()
		c.execute("""CREATE TABLE bat(email text PRIMARY KEY NOT NULL,password text NOT NULL)""") 
		con.commit()
		con.close()
	def happen():
		
		insrt=Tk()
		insrt.geometry("400x400+500+100")
		insrt.resizable(width=False, height=False)
		global enter
		global enters

		label=Label(insrt,text="email",width=20).grid(row=0,column=0,pady=10,padx=10)
		enter=Entry(insrt,width=20)
		enter.grid(row=0,column=1)
		labels=Label(insrt,text="password",width=20).grid(row=1,column=0,pady=10,padx=10)
		enters=Entry(insrt,width=20,show="*")
		enters.grid(row=1,column=1)
		def save():
			#test
			t1=enter.get()
			t2=enters.get()
			print(t1," ",t2)
			a="@"
			b=[".com",".in"]
			if a in t1:
				if b[0] in t1 or b[1] in t1 :
					print(True)
					if len(t2)>=8:
						if(len(enter.get())!=0 and len(enters.get())!=0):
							con=sqlite3.connect('bird.db')
							c=con.cursor()
							c.execute("INSERT INTO bat VALUES(:email,:password)",
								{'email':enter.get(),'password':enters.get()})
							con.commit()
							con.close()
							insrt.destroy()
						else:
							messagebox.showwarning("!Warnning","Fields may be empty")	
					else:
						messagebox.showwarning("password","password length is less than 8")
			else:
				messagebox.showinfo("inavlid email","invalid email")
		submit=Button(insrt,text="save",command=save).grid(row=2,column=1)

	def logged():
		splash.destroy()
		log=Tk()
		log.geometry("300x300+500+100")
		log.resizable(width=False, height=False)
		enter=Entry(log,width=30)
		label=Label(log,text="email",width=10).grid(row=0,column=0)
		enter.grid(row=0,column=1)

		enters=Entry(log,width=30,show="*")
		label=Label(log,text="pass",width=10).grid(row=1,column=0)
		enters.grid(row=1,column=1)
		def click():
			if(len(enter.get())!=0 and len(enters.get())!=0):
				conn=sqlite3.connect('bird.db')
				c=conn.cursor()
				a=("SELECT password FROM bat WHERE email=?")
				c.execute(a,[(enter.get())])
				result=c.fetchall()
				print_records=''
				for record in result:
					print_records+=str(record[0])
				
				if(print_records==str(enters.get())):
					
					main_21()
					log.destroy()
				elif(not (enter.get()) and (not len(enters.get()))):
					messagebox.showwarning("!Warnning","Email or password may empty")
				else:
					messagebox.showwarning("!Warnning","wrong credential \n check email and password")	
			else:
				messagebox.showwarning("!Warnning","Fields may be empty")		
					
					
		b=Button(log,text="login",command=click).grid(row=2,column=0)
		b=Button(log,text="signup",command=happen).grid(row=3,column=0)	
		#btn=Button(root,text="login",command=logged).grid(row=1,column=0)
		#root.after(1000,logged)

	splash.after(5000,logged)
	mainloop()
bank()