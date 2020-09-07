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
<Overtime Hours> - overtime in hours
make sure to use format only include dates eg, 20,22,24 etc. only and only separate by ","commas"


separation symbol #

full in format: with index

         01            02             03               04              05            06           07           08             09
<name of employee>#<designation>#<working days>#<rate of wages>#<rate of v.d.a>#<pf opted? >#<esi opted ?>#<leaves data>#<Overtime Hours>




'''

list_main=[] #primary raw list
listcpy=[] # main meaningfull list
total_emp=0 #total employees
list_holiday=[] #list of holidays dates
no_of_holidays=0 # eligible no of holidays
max_days_of_month=0 # month's max days e.g for feb it;s 28 and july it;s 31
one_day_work_hour=0 # no of hours of work in a day
#function to read holiday list from text file 
with open("holidays.txt") as f:
    a=f.read()
    list_holiday=a.split(",")
    
#function to calculate actual holidays awarded to the employee
def U_leave_holiday(lst_hol,lst_leav): # passing list of holiday and list of leave to find intersection of leaves into holiday
    lst_hol=set(lst_hol)
    lst_leav=set(lst_leav)
    lst_common=list(lst_leav&lst_hol)
    if lst_common:
        return len(lst_common)
    else:
        return 0


#function to convert and calculate things and convert into required meaningful format    
def copyToListCPY():
    with open("eout.txt") as f :
        a=f.read()
        temp=a.split("#")
        #print(temp)
        listcpy.insert(0,temp)
        for i in range(total_emp):
            listcpy[i][0]=i+1 #s.no-
            listcpy[i][1]=list_main[i][0] #@name-

            #NO OF DAYS
            listcpy[i][2]=list_main[i][2] #@working days-

            #check holidays 
            
            
            while("" in list_holiday) : #loop to remove empty items
                list_holiday.remove("")
            no_of_holidays=len(list_holiday) # total no of valid eligible holiday
            


            temp_leave_list = list_main[i][8]
            if int(list_main[i][8])==0:
                listcpy[i][3]=no_of_holidays # if there are no leaves i.e all eligible holidays will be given
            else:
                listcpy[i][3]=U_leave_holiday(list_main[i][8]),list_holiday) #@holidays-
                #check how many leaves matches holidays
                
          
            listcpy[i][4]=int(listcpy[i][2])+ int(listcpy[i][3]) #@total days-

            #POSITION 
            listcpy[i][5]=list_main[i][2] #@designation-

            #WAGES
            listcpy[i][6]=list_main[i][4] #@rate of wages-
            listcpy[i][7]=list_main[i][5] #@rate of vda-
            listcpy[i][8]=int(list_main[i][4])+int(list_main[i][5]) #@total wages/salary-

            #ESIC PF OT
            
            #check if pf opted
            if list_main[i][5]=='y' or list_main[i][5]=='Y':
                listcpy[i][9]=list_main[i][0]               #@pf wage

                #check if total salary is <=15000
                if int(list_cpy[i][8])<=15000:
                    list_cpy[i][8]=listcpy[i][4]/max_days_of_month*listcpy[i][8]
                else:
                    list_cpy[i][8]=15000
                    
                     
            
                
            

            #calculating overtime wages
            tmp_actual_otHours=int(list_main[i][9])*2
            #check if overtime is zero
            if tmp_actual_otHours==0:
                listcpy[i][11]=0
            else:                                         #@o.t wages
                listcpy[i][11]=tmp_actual_otHours/one_day_work_hour*(listcpy[i][8]/max_days_of_month)
                
            #after calculating ot wages then continue to calculate esic wages as esic wage = wages for work done + ot wages    
            listcpy[i][10]= (listcpy[i][4]/max_days_of_month*listcpy[i][8])+ listcpy[i][11] #@esic wage-
            
            listcpy[i][12]=list_main[i][0] #@total amount payable

            #DEDUCTIONS
            listcpy[i][13]=list_main[i][0] #@pf
            listcpy[i][14]=list_main[i][0] #@family pension
            listcpy[i][15]=list_main[i][0] #@total pf
            listcpy[i][16]=list_main[i][0] #@esi contribution .75%
            listcpy[i][17]=list_main[i][0] #@advance/loan
            listcpy[i][18]=list_main[i][0] #@total deductions
            
           
           
  


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

    
