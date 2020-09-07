from array import *

'''
REGISTER OF WAGES

WORK : MAKE SALARY OF ENTERPRISES FAST AND ACCURATE USING AI.


INPUT : IT TAKES INPUT FROM THE USER BY A TEXT FILE IN THE GIVEN FORMAT

<col1><col2>.... so explained below each column

<name of employee>
<designation>
<working days> - excluding OVER TIME
<rate of wages>
<rate of v.d.a>
<pf opted? > y for yes and n for no
<esi opted ?> y or n
<leaves data> - very important described below:

make sure to use format only include dates eg, 20,22,24 etc. only and only separate by ","commas"


separation symbol #

full in format: with index

         01            02             03               04              05            06           07           08
<name of employee>#<designation>#<working days>#<rate of wages>#<rate of v.d.a>#<pf opted? >#<esi opted ?>#<leaves data>




'''

list_main=[]
listcpy=[]
total_emp=0
list_holiday=0

#function to read holiday list from text file 
with open("holidays.txt") as f:
    a=f.read()
    list_holiday=a.split(",")

#function to convert and calculate things and convert into required meaningful format    
def copyToListCPY():
    with open("eout.txt") as f :
        a=f.read()
        temp=a.split("#")
        #print(temp)
        listcpy.insert(0,temp)
        for i in range(total_emp):
            listcpy[0]=i+1 #s.no-
            listcpy[1]=list_main[0] #name-

            #NO OF DAYS
            listcpy[2]=list_main[2] #working days-

            #check holidays
            list_holiday=
            listcpy[3]=list_main[0] #holidays
            listcpy[4]=list_main[0] #total days

            #POSITION 
            listcpy[5]=list_main[1] #designation-

            #WAGES
            listcpy[6]=list_main[3] #rate of wages-
            listcpy[7]=list_main[4] #rate of vda-
            listcpy[8]=int(list_main[3])+int(list_main[4]) #total wages/salary

            #ESIC PF OT
            
            #check if pf opted
            if list_main[5]=='y' or list_main[5]=='Y':
                listcpy[9]=list_main[0] #pf wage

                #check if total salary is <=15000
                if int(list_cpy[8])<=15000:
                    
                    # - to be calculated after calculating no of days working
               
                
            else:
                #cmd
            
                
            listcpy[10]=list_main[0] #esic wage
            listcpy[11]=list_main[0] #o.t wages
            listcpy[12]=list_main[0] #total amount payable

            #DEDUCTIONS
            listcpy[13]=list_main[0] #pf
            listcpy[14]=list_main[0] #family pension
            listcpy[15]=list_main[0] #total pf
            listcpy[16]=list_main[0] #esi contribution .75%
            listcpy[17]=list_main[0] #advance/loan
            listcpy[18]=list_main[0] #total deductions
            
           
           
  


copyToListCPY()
print(listcpy)
    
with open("data.txt") as f :
    
    a=f.read()
    list_data=(a.split("\n"))
   

    # using remove() to 
    # perform removal 
    while("" in list_data) :
        list_data.remove("")

    #COUNTING TOTAL NO OF EMPLOYEES IN THE LIST (READ FROM TEXT FILE)    
    total_emp=len(list_data)
    

    for i in range(total_emp):
        
        temp_list=list_data[i].split("#")
        list_main.insert(i,temp_list)
        
        
            
                  
    
        
   # print(list_main, "\n", list_main[0][2])

    
