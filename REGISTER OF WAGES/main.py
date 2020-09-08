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


         0            01             02               03              04            05           06           07             08
<name of employee>#<designation>#<working days>#<rate of wages>#<rate of v.d.a>#<pf opted? >#<esi opted ?>#<leaves data>#<Overtime Hours>




'''

list_main=[] #primary raw list
listcpy=[] # main meaningfull list
total_emp=0 #total employees
list_holiday=[] #list of holidays dates
no_of_holidays=0 # eligible no of holidays
max_days_of_month=31 # month's max days e.g for feb it;s 28 and july it;s 31
one_day_work_hour=8 # no of hours of work in a day
#function to read holiday list from text file


with open("holidays.txt") as f:
    a=f.read()
    list_holiday=a.split(",")
    
#function to calculate actual holidays awarded to the employee
def U_leave_holiday(lst_hol,lst_leav): # passing list of holiday and list of leave to find intersection of leaves into holiday

    lst_hol=set(lst_hol)
    
    if "," in lst_leav:
        lst_leav=lst_leav.split(",")
    else:
        lst_leav+=','
        lst_leav=lst_leav.split(",")
    lst_leav=set(lst_leav)
    
    
    lst_common=list(lst_leav&lst_hol)
   # print("common : " ,lst_common, "\n", "holiday list : ",lst_hol,"\nLeave List",lst_leav)
    
    if lst_common:
        return no_of_holidays-len(lst_common)      #bug fixed
    else:
        return no_of_holidays    #bug fixed

#FUNCTION TO EXPORT FINAL OUTPUT TO TEXT FILE
def exportData():
    final_export_data=""
    for i in range(0,len(listcpy)):
        for j in range (0,21):
            try:final_export_data+=str(listcpy[i][j])+"\t"
            except Exception as e:print(" i , j ", i,j)
        final_export_data+="\n"
    #print(final_export_data)

    #print("\n len : i,o ",len(listcpy),total_emp)


    try:
        tmp_file_out=open("salary.txt",'w+')
        tmp_file_out.write(final_export_data)
    except IOError:
        print("File not found or path is incorrect")
        
    finally:
        print("Done")
    
        
        
#function to round to always next possible int
#i.e round of 4.3 =5, or maybe general for future
def myRound(number):
    return int(round(number,0))
        
#function to add total row

'''
tmp_totals indexes

0  - working days
1 -  holidays
2- total days
3-rate of wage
4-rate of vda
5-total wages
6-pf wage
7-esi wage
8-ot wage
9-amt payable
10-pf
11-family pension
12-total pf
13-esic contribution
14-loan
15-total deduction
16-balance paid
'''
def addTotalrow():
    global listcpy
    tmp_totals=[0.0]*17
    for i in range(0,total_emp):
        tmp_totals[0]+=float(listcpy[i+1][2])
        tmp_totals[1]+=float(listcpy[i+1][3])
        tmp_totals[2]+=float(listcpy[i+1][4])
        tmp_totals[3]+=float(listcpy[i+1][6])
        tmp_totals[4]+=float(listcpy[i+1][7])
        tmp_totals[5]+=float(listcpy[i+1][8])
        tmp_totals[6]+=float(listcpy[i+1][9])
        tmp_totals[7]+=float(listcpy[i+1][10])
        tmp_totals[8]+=float(listcpy[i+1][11])
        tmp_totals[9]+=float(listcpy[i+1][12])
        tmp_totals[10]+=float(listcpy[i+1][13])
        tmp_totals[11]+=float(listcpy[i+1][14])
        tmp_totals[12]+=float(listcpy[i+1][15])
        tmp_totals[13]+=float(listcpy[i+1][16])
        tmp_totals[14]+=float(listcpy[i+1][17])
        tmp_totals[15]+=float(listcpy[i+1][18])
        tmp_totals[16]+=float(listcpy[i+1][19])
    #print(tmp_totals[11])
    for i in range(17):
        tmp_totals[i]=myRound(tmp_totals[i])
    list_toadd=['','']
    for i in range(3):
        list_toadd.append(tmp_totals[i])
    list_toadd.append('')
    for i in range(3,17):
         list_toadd.append(tmp_totals[i])
    list_toadd.append('')
    listcpy.insert(total_emp+1,list_toadd)
    #print(list_toadd)
   
   
    
   
        
'''
listcpy indexes


  0         01                   02          03          04         05       06            07                 08
<S.no>#<Name of Employees>#<Working Days>#<holida>#<Total Days>#<Desig.>#<Rate Wages>#<Rate of V.D.A>#<Total Wages/Salary>



    09         10           11                12          13           14            15                16                     17
<PF wages>#<Esi Wages>#<O.T wages>#<Total Amt. Payable># <P.F> #<Family Pension>#<Total P.F>#<E.S.I contribution (.75%)>#<Advance/Loan/I.T>


       18                 19                      20
#<Total Deductions>#<Balance Paid>#<Signature or Thumb Impression of Employee>
'''           
#function to use balanced ai in all the listcpy columns
def balance_the_sheet():
    #accessing global listcpy
    global listcpy

    #passing the values to the function
    
   
    for j in range (9,20):
                            
        #updating the listcpy through returned data
        tmp_bal_data = root_balance_helper(j)
        for i in range(1,len(listcpy)):
            #print(" index ",i," ", listcpy[i][j])
            #print(" index mod ",i," ", tmp_bal_data[i-1],"\n")
            listcpy[i][j]= tmp_bal_data[i-1]
        #print(tmp_bal_data)
        #listcpy[j][i]=tmp_bal_data[j]
        #print(" i , j : " , i , " , ", j)
    return "done"
    

#helper function : Find sum of all elements of a listbox
def sumList(lista):
    tmp_sum=0
    for i in range (len(lista)):
        tmp_sum+=float(lista[i])
    return tmp_sum
        

#function to balance things
def root_balance_helper(index_i):
   
    tmp_list=[] # list of a particular fiels of different me
    tmp_rounded_list=[] #stores rounded or final output of data
    for i in range (1,len(listcpy)):
        tmp_list.append(listcpy[i][index_i])
        tmp_rounded_list.append(round(listcpy[i][index_i],0))
    #print(tmp_list)

   
    
    tmp_dlist=[] #temporary data list to include differences list ie. 8.6 will list 0.6, 8.1 list 0.1

    p_list=[]
    n_list=[]
    sum_p_and_n=0
    for i in range(len(tmp_list)):
        tmp_item=float(tmp_list[i])-int(tmp_list[i])
        tmp_item=round(tmp_item,2)
        
        if tmp_item>=0.5:
            tmp_dlist.append(0)
            n_list.append(0)
            p_list.append(round((1-tmp_item),2))
            
        else:
            tmp_dlist.append((tmp_item))
            n_list.append(round((tmp_item),2))
            p_list.append(0)
    #print(" p list : " , n_list)
    #print(tmp_list)
    #print("\n\n\n\nP List : ",p_list,'\n N list : ', n_list," max p list, min p list: ", max(p_list), ',',min(p_list))
    
    #calculate how much to increase
    #print(p_list[3])
    sum_p_and_n=int(round(sumList(p_list)-sumList(n_list),0))
    #print(sum_p_and_n)
    if sum_p_and_n>0: #overall increament
        # deduct
       

        i=len(p_list)
        while(i>0):
            i-=1
            
            tmp_max=max(p_list)
            for j in range(len(p_list)):
               
                if p_list[j]==tmp_max:
                   # print(f"P list at {j} is {float(p_list[j])} and tmp_max is {tmp_max}")
                    #print(p_list[j])
                    
                    #print("before : ",tmp_rounded_list[j])
                    tmp_rounded_list[j]-=1
                   # print("after : ",tmp_rounded_list[j])
                    p_list[j]=0
                    tmp_sum=0
                    
                    for x in range(0,len(tmp_rounded_list)-1):
                        tmp_sum+=tmp_rounded_list[x]
                    
                    if tmp_rounded_list[-1]==tmp_sum:
                        #print("ddfsdfsdfasdfsd")
                        i=0
                        j=len(p_list)
                        break                   
                
                         
            
    elif sum_p_and_n<0:
        # addition
        
        i=len(n_list)
        while(i>0):
            i-=1
            tmp_max=max(n_list)
            for j in range(len(n_list)):
               
                if n_list[j]==tmp_max:
                    #print(f"P list at {j} is {float(p_list[j])} and tmp_max is {tmp_max}")
                    #print(p_list[j])
                    
                    #print("before : ",tmp_rounded_list[j])
                    tmp_rounded_list[j]+=1
                    #print("after : ",tmp_rounded_list[j])
                    n_list[j]=0
                    tmp_sum=0
                    
                    for x in range(0,len(tmp_rounded_list)-1):
                        tmp_sum+=tmp_rounded_list[x]
                    
                    if tmp_rounded_list[-1]==tmp_sum:
                        #print("ddfsdfsdfasdfsd")
                        i=0
                        j=len(n_list)
                        break
    elif sum_p_and_n==0:
        print("zero already done")
        
            
                    
                
                    
            
    
        
   
    
    #print("\n Increment : ", sum_p_and_n, "\n max , min : ", max(tmp_dlist),min(tmp_dlist))
     
    return tmp_rounded_list #returning the balanced sheet
        
  
    

        
        
    

#function to convert and calculate things and convert into required meaningful format    
def copyToListCPY():
    global listcpy
    global no_of_holidays
    global list_holiday
    global total_emp
    with open("eout.txt") as f :
        
        a=f.read()
        temp=a.split("#")
        #print(temp)
        listcpy.insert(0,temp)

        
        #function to initialize the array with some values then later update it
  
        for i in range(total_emp):
            listcpy.insert(i+1,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        
            
        
        for i in range(total_emp):
            

         
            #print("i ",i)    
            listcpy[i+1][0]=i+1 #@s.no-    
            listcpy[i+1][1]=list_main[i][0] #@name-

            #NO OF DAYS
            
            listcpy[i+1][2]=float(list_main[i][2]) #@working days-

            #check holidays 
            
            
            while("" in list_holiday) : #loop to remove empty items
                list_holiday.remove("")
            no_of_holidays=len(list_holiday) # total no of valid eligible holiday
            


            temp_leave_list = list_main[i][7] #temporary leave list
            if (list_main[i][7])=='0':
                listcpy[i+1][3]=no_of_holidays # if there are no leaves i.e all eligible holidays will be given
            else:
                listcpy[i+1][3]=U_leave_holiday(list_holiday,list_main[i][7]) #@holidays-  #make sure here we are sending direct data not splitted one
               # print("sending : leave list : ", list_main[i][7])

                #check how many leaves matches holidays
                
          
            listcpy[i+1][4]=(listcpy[i+1][2])+ (listcpy[i+1][3]) #@total days-

            #POSITION 
            listcpy[i+1][5]=list_main[i][1] #@designation-

            #WAGES
            listcpy[i+1][6]=list_main[i][3] #@rate of wages-
            listcpy[i+1][7]=list_main[i][4] #@rate of vda-
            listcpy[i+1][8]=int(list_main[i][3])+int(list_main[i][4]) #@total wages/salary-

            #ESIC PF OT
            
            #check if pf opted
            if list_main[i][5]=='y' or list_main[i][5]=='Y':
                                                                #@pf wage
                #check if total salary is <=15000
                tmp_wages=(listcpy[i+1][4]/max_days_of_month)*listcpy[i+1][8]
                if int(tmp_wages)<=15000:
                  listcpy[i+1][9]=round((listcpy[i+1][4]/max_days_of_month)*listcpy[i+1][8],2) #rounding upto 2 decimals 
                else:
                    listcpy[i+1][9]=15000
                    
            else:
                listcpy[i+1][9]=0
                
            
                
            

            #calculating overtime wages
            tmp_actual_otHours=int(list_main[i][8])*2
            #check if overtime is zero
            if tmp_actual_otHours==0:
                listcpy[i+1][11]=0
            else:                                         #@o.t wages
                listcpy[i+1][11]=round(tmp_actual_otHours/one_day_work_hour*(listcpy[i+1][8]/max_days_of_month),2)#rounding upto 2 decimals 
                
            #after calculating ot wages then continue to calculate esic wages as esic wage = wages for work done + ot wages
            if list_main[i][6]=='y' or list_main[i][6]=='Y':           
                                  
                listcpy[i+1][10]= round((listcpy[i+1][4]/max_days_of_month*listcpy[i+1][8])+ listcpy[i+1][11],2) #@esic wage-
            else:
                listcpy[i+1][10]=0
            
            listcpy[i+1][12]=round((listcpy[i+1][4]/max_days_of_month*listcpy[i+1][8])+ listcpy[i+1][11],2) #@total amount payable

            #DEDUCTIONS
            listcpy[i+1][13]=round(listcpy[i+1][9]/12,2) #@pf
            
            listcpy[i+1][15]=round(listcpy[i+1][9]/10,2) #@total pf
            
            listcpy[i+1][14]=(listcpy[i+1][15])-(listcpy[i+1][13]) #@family pension =>> total pf-pf
            
            listcpy[i+1][16]=round(3/4*listcpy[i+1][10]/100,2) #@esi contribution .75%
            
            listcpy[i+1][17]=0 #@advance/loan
            listcpy[i+1][18]=round(listcpy[i+1][15]+listcpy[i+1][16],2) #@total deductions
            listcpy[i+1][19]=round(listcpy[i+1][12]- listcpy[i+1][18],2) #@amount payable
            listcpy[i+1][20]="" #@signature
        addTotalrow()
        
           
           
  


   
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
    
        

    #copyToListCPY()

    
    copyToListCPY()
    balance_the_sheet()
    #print(root_balance_helper(10))
    
    exportData()
    
    #print(listcpy)
    #print("done : !  ")
    #print(list_main[15][7])    
    #print(listcpy)
        
    

    
            
                  
    
        
   # print(list_main, "\n", list_main[0][2])
   

    
