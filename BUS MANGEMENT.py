import mysql.connector as con
mycon=con.connect(host="localhost",user="root",password="123456")
mycur=mycon.cursor()
mycur.execute("create database  if not exists BUS_MANAGEMENT;")
mycur.execute("use BUS_MANAGEMENT;")
mycur.execute('create table  if not exists BUSDETAILS(bus_no varchar(4) primary key,DT date,form varchar(35), destination varchar(35), via varchar(35), drivercode varchar(5),conductorcode varchar(5), bustype varchar (3));')

def insert_bus():
    print("--------------------------------------------------[BUS DETAILS]----------------------------------------------")
    n=int(input("no. of buses enter: "))
    for i in range(n):
        busno=input("enter bus no. (only last 4digit):")
        date=input("enter date of journey(yyyy\mm\dd): ")
        form=input("starting station:")
        des=input("destination station:")
        via=input("jounrey via station:")
        diver=input("emp-code  of driver:")
        cond=input("emp-code of conductor:")
        print('buses type \n 1.gurjarnagri(GEN) \n 2.express(EXP)\n3.ordinary(ORD)\n 4.metrolink(MLS)\n 5. student spl(STU)')
        busty=input('bus type(only in code):')
        
        q="insert into BUSDETAILS values(%s,%s,%s,%s,%s,%s,%s,%s);"
        mycur.execute(q,(busno,date,form,des,via,diver,cond,busty))
        mycur.execute("commit")


mycur.execute('create table if not exists REVENUE(bus_no varchar(4) primary key, DT date,total_ticket varchar(200), total_revenue varchar(200),pass_ticket varchar(200),priced_ticket varchar(200),pass_revenue varchar(10) default 0, priced_revenue varchar(200),half_ticket varchar(200), half_revenue varchar(200));')
def revenue():
     print("-----------------------------------------------[REVENUE DETAILS]---------------------------------------------------")
     n=int(input("no. of buses enter: "))
     for i in range(n):
         busno=input("enter bus no. (only last 4digit):")
         date=input("enter date of journey(yyyy\mm\dd): ")        
         total_ticket=input("enter total ticket sold:")
         total_revenue=input("enter total revenue: ")
         passticket=input("enter pass/div/ews/other free ticket sold: ")
         passrev=input("revenue gained:")
         pricedticket=input("priced ticket sold:")
         pricedrev=input("revenue gained by it:")
         half_ticket=input("half ticket sold:")
         half_revenue=input("revenue gained by it:")
         q="insert into REVENUE values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
         a=(busno,date,total_ticket,total_revenue,passticket,pricedticket,passrev,pricedrev,half_ticket,half_revenue)
         mycur.execute(q,a)
         mycur.execute("commit")
def enter():
    print("---------------------------[DATA ENTERING]---------------------------------------------------------")
    while True:
        print("1. entering data in BUS DETAILS \n 2. entering data in REVENUE DETAILS \n 3.perious menu \n 4. exit")
        ch=int(input("enter your choice:"))
        if ch==1:
            insert_bus()
        elif ch==2:
            revenue()
        elif ch==3:
            project()
        else:
            break
def search():
     print("--------------------------------[SEARCHING PROCESS]---------------------------------------------------------")
     while True:
         
         print('1.search by bus no. \n 2. search by revenue \n 3.search by ticket sold \n 4. search by emp_code \n 5.previous menu \n 6.exit')
         choice=int (input("enter your choice:"))
         if choice==1:
             search_bus()
         elif choice==2:
            search_revenue()
         elif choice==3:
            search_ticket()
         elif choice==4:
            search_emp_code()
         elif choice==5:
            project()
         else:
            break
def search_bus():
     n=input("enter bus no. : ")
     mycur.execute('select * from BUSDETAILS,REVENUE where BUSDETAILS.bus_no =REVENUE.bus_no and BUSDETAILS.bus_no='+n)
     a=mycur.fetchall()
     print(a)
     mycur.close()
def  search_revenue():
    while True:
        print('1. search greater  than specific amount \n 2.search leaser than specific amount \n 3.previous menu \n 4.exit')
        n=int(input("enter your choice:"))
        if n==1:
            p=input("enter amount (in Rs.):")
            mycur.execute('select * from BUSDETAILS,REVENUE where BUSDETAILS.bus_no =REVENUE.bus_no and total_revenue >= '+p)
            a=mycur.fetchall()
            print(a) 
            mycur.close()
        elif  n==2:
            q=input("enter amount (in Rs.):")
            mycur.execute('select * from BUSDETAILS,REVENUE where BUSDETAILS.bus_no =REVENUE.bus_no and total_revenue <= '+q)
        elif n==3:
            search()
        else:
            break
def search_ticket():
    while True:
        print('1. search by pass ticket \n 2. search by priced ticket t')
        n=int(input("enter your choice:"))
        if n==1:
            s=0
            mycur.execute('select * from BUSDETAILS,REVENUE where BUSDETAILS.bus_no =REVENUE.bus_no and total_revenue >= '+s)
        elif n==2:
            k=0
            mycur.execute('select * from BUSDETAILS,REVENUE where BUSDETAILS.bus_no =REVENUE.bus_no and total_revenue <= '+k)
        elif n==3:
            search()
        else:
            break
def search_emp_code():
            while True:
                print("1. search by emp-code  of driver \n 2. emp-code of conductor  \n 3.previous menu \n 4.exit ")
                n=int(input("enter your choice:"))
                if n==1:
                    j=input("enter emp-code  of driver: ")
                    mycur.execute('select * from BUSDETAILS,REVENUE where BUSDETAILS.bus_no =REVENUE.bus_no and drivercode= '+j)
                elif n==2:
                    p=input("enter emp-code of conductor: ")
                    mycur.execute('select * from BUSDETAILS,REVENUE where BUSDETAILS.bus_no =REVENUE.bus_no and conductorcode= '+p)
                elif n==3:
                    search()
                else:
                    break
def updation():
    while True:
                          print("-------------------------------------[UPDATION]------------------------------------")
                          print("1.update bus- no \n 2.update date \n 3. update begining station \n 4.  update via station \n 5. update destination station \n 6.  update driver code \n 7. update conductor code \n 8'.  update bustype ")
                          print(" 9. update total ticket sold \n 10. update total revenue gained \n 11. update pass ticket sold \n 12. update priced ticket sold \n 13. update pass ticket revenue \n 14. update priced ticket sold ")
                          print("15.perious menu  \n 16. exit")
                          n=int (input("enter your choice:"))
                          if n==1:
                              p=input("enter incorrect bus no(only last four digit):")
                              q=input("enter correct bus no(only last four digit):")
                              mycur.execute("update BUSDETAILS set bus_no=%s where BUSDETAILS.bus_no= %s",(q,p))
                          elif n==2:
                              G=input("enter incorrect date(yyyy/mm/dd): ")
                              H=input("enter correct date(YYYY\MM\DD):")
                              mycur.execute("update  BUSDETAILS set DT=%s where BUSDETAILS.DT= %s",(H,G))
                          elif n==3:
                                G=input("enter incorrect begining station: ")
                                H=input("enter correct begining station:")
                                mycur.execute("update  BUSDETAILS set from=%s where BUSDETAILS.from=%s",(H,G))
                          elif n==4:
                              G=input("enter incorrect via station : ")
                              H=input("enter correct via station :")
                              mycur.execute("update  BUSDETAILS set via=%s where BUSDETAILS.via= %s",(H,G))
                          elif n==5:
                              G=input("enter incorrect destination station: ")
                              H=input("enter correct  destination station:")
                              mycur.execute("update  BUSDETAILS set destination=%s where BUSDETAILS.destination= %s",(H,G))
                          elif n==6:
                              G=input("enter incorrect driver code: ")
                              H=input("enter correct driver code :")
                              mycur.execute("update  BUSDETAILS set drivercode=%s where BUSDETAILS.drivercode= %s",(H,G))
                          elif n==7:
                              G=input("enter incorrect conductor code: ")
                              H=input("enter correct conductor code :")
                              mycur.execute("update  BUSDETAILS set conductorcode=%s where BUSDETAILS.conductorcode= %s",(H,G))
                          elif n==8:
                              print('buses type \n 1.gurjarnagri(GEN) \n 2.express(EXP)\n3.ordinary(ORD)\n 4.metrolink(MLS)\n 5. student spl(STU)')
                              G=input("enter incorrect bus type: ")
                              H=input("enter correct bus  type :")
                              mycur.execute("update  BUSDETAILS set bustype=%s where BUSDETAILS.bustype= %s",(H,G))
                          elif n==9:
                              G=input("enter incorrect total ticket sold: ")
                              H=input("enter correct total ticket sold :")
                              mycur.execute("update  REVENUE set total_ticket=%s where REVENUE.total_ticket= %s",(H,G))
                          elif n==10:
                              G=input("enter incorrect total revenue gained: ")
                              H=input("enter correct total revenue gained :")
                              mycur.execute("update  REVENUE set total_revenue=%s where REVENUE.total_revenue= %s",(H,G))
                          elif n==11:
                              G=input("enter incorrect pass ticket sold: ")
                              H=input("enter correct pass ticket sold :")
                              mycur.execute("update  REVENUE set pass_ticket=%s where REVENUE.pass_ticket= %s",(H,G))
                          elif n==12:
                              G=input("enter incorrect priced ticket sold: ")
                              H=input("enter correct priced ticket sold :")
                              mycur.execute("update  REVENUE set priced_ticket=%s where REVENUE.priced_ticket= %s",(H,G))
                          elif n==13:
                              G=input("enter incorrect pass ticket revenue: ")
                              H=input("enter correct pass ticket revenue :")
                              mycur.execute("update  REVENUE set pass_revenue=%s where REVENUE.pass_revenue= %s",(H,G))
                          elif n==14:
                              G=input("enter incorrect priced ticket revenue: ")
                              H=input("enter correct priced ticket revenue :")
                              mycur.execute("update  REVENUE set priced_revenue=%s where REVENUE.priced_revenue= %s",(H,G))
                          elif n==15:
                              project()

                          else:
                              break
            
def project():
                while True:
                          print("-----------------------------------------[PROJECT WORK] ----------------------------------------------")
                          print("1. data insert \n2. search data \n3. data updation \n4. deletion \n5. exit")
                          ch=int(input(" enter your choice: "))
                          if ch==1:
                              enter()
                          elif ch==2:
                              search()
                          elif ch==3:
                              updation()
                          elif ch==4:
                              print("sorry for in convension to avoid security issue we had not introduces deletion of and data.")
                              print("if it urgent then updation is possible and you can put noting value there.")
                              p=input("if  want update write YES :")
                              if p=="YES":
                                  updation()
                              else:
                                      break
                          else:
                              break
project()
