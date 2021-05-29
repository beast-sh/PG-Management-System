from tkinter import *
import sqlite3,sys

def connection():
    try:
        conn=sqlite3.connect("pg.db")
    except:
        print("cannot connect to the database")
    return conn    


def verifier():
    a=b=c=d=e=f=g=0
    if not name.get():
        t1.insert(END,"<>Tenent name is required<>\n")
        a=1
    if not father.get():
        t1.insert(END,"<>Father name is required<>\n")
        b=1
    if not phone.get():
        t1.insert(END,"<>Phone number is requrired<>\n")
        c=1
    
    if not address.get():
        t1.insert(END,"<>Address is Required<>\n")
        d=1
    if not adharId.get():
        t1.insert(END,"<>AdharId is Required<>\n")
        e=1
    if not advance.get():
        t1.insert(END,"<>Advance is Required<>\n")
        f=1
    if not roomno.get():
        t1.insert(END,"<>Address is Required<>\n")
        g=1
    if a==1 or b==1 or c==1 or d==1 or e==1 or f==1 or g==1:
        return 1
    else:
        return 0


def add_tenents():
            ret=verifier()
            if ret==0:
                conn=connection()
                cur=conn.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS PGRENTALDETAILS(NAME TEXT,FATHERNAME TEXT,PHONE_NO INTEGER,ADDRESS TEXT,ADHARID INTEGER,ADVANCE INTEGER,RoomNo TEXT)")
                cur.execute("insert into PGRENTALDETAILS values(?,?,?,?,?,?,?)",(name.get(),father.get(),int(phone.get()),address.get(),int(adharId.get()),int(advance.get()),roomno.get()))
                conn.commit()
                conn.close()
                t1.insert(END,"ADDED SUCCESSFULLY\n")


def view_tenents():
    conn=connection()
    cur=conn.cursor()
    cur.execute("select * from PGRENTALDETAILS")
    data=cur.fetchall()
    conn.close()
    for i in data:
        t1.insert(END,str(i)+"\n")


def delete_tenents():
    
        conn=connection()
        cur=conn.cursor()
        cur.execute("DELETE FROM PGRENTALDETAILS WHERE ADHARID=?",(int(adharId.get()),))
        conn.commit()
        conn.close()
        t1.insert(END,"SUCCESSFULLY DELETED THE USER\n")

def update_tenents():
    ret=verifier()
    if ret==0:
        conn=connection()
        cur=conn.cursor()
        cur.execute("UPDATE PGRENTALDETAILS SET NAME=?,FATHERNAME=?,PHONE_NO=?,ADDRESS=?,ADHARID=?,ADVANCE=?,RoomNo=? where ADHARID=?",(name.get(),father.get(),int(phone.get()),address.get(),int(adharId.get()),int(advance.get()),roomno.get(),int(adharId.get())))
        conn.commit()
        conn.close()
        t1.insert(END,"UPDATED SUCCESSFULLY\n")


def clse():
    sys.exit() 


if __name__=="__main__":
    root=Tk()
    root.title("PG Management System")
     
    name=StringVar()
    father=StringVar()
    phone=StringVar()
    address=StringVar()
    adharId=StringVar()
    advance=StringVar()
    roomno=StringVar()
    
    label1=Label(root,text="Name:")
    label1.place(x=0,y=0)

    label2=Label(root,text="Father Name:")
    label2.place(x=0,y=30)

    label3=Label(root,text="Phone Number:")
    label3.place(x=0,y=60)

    label4=Label(root,text="Address:")
    label4.place(x=0,y=90)

    label5=Label(root,text="Adhar Id:")
    label5.place(x=0,y=120)

    label6=Label(root,text="Advance :")
    label6.place(x=0,y=150)

    label7=Label(root,text="Room No :")
    label7.place(x=0,y=180)

    e1=Entry(root,textvariable=name)
    e1.place(x=100,y=0)

    e2=Entry(root,textvariable=father)
    e2.place(x=100,y=30)
   
    e3=Entry(root,textvariable=phone)
    e3.place(x=100,y=60)
    
    e4=Entry(root,textvariable=address)
    e4.place(x=100,y=90)
    
    e5=Entry(root,textvariable=adharId)
    e5.place(x=100,y=120)
    
    e6=Entry(root,textvariable=advance)
    e6.place(x=100,y=150)

    e7=Entry(root,textvariable=roomno)
    e7.place(x=100,y=180)
    
    t1=Text(root,width=80,height=20)
    t1.grid(row=10,column=1)
   


    b1=Button(root,text="ADD Tenents",command=add_tenents,width=40)
    b1.grid(row=11,column=0)
    
    b2=Button(root,text="VIEW ALL Tenents",command=view_tenents,width=40)
    b2.grid(row=12,column=0)

    b3=Button(root,text="DELETE Tenents",command=delete_tenents,width=40)
    b3.grid(row=13,column=0)

    b4=Button(root,text="UPDATE INFO",command=update_tenents,width=40)
    b4.grid(row=14,column=0)

    b5=Button(root,text="CLOSE",command=clse,width=40)
    b5.grid(row=15,column=0)


    root.mainloop()
