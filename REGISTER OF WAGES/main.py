

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

separation symbol #

full in format:

<name of employee>#<designation>#<working days>#<rate of wages>#<rate of v.d.a>#<pf opted? >#<esi opted ?>




'''

with open("data.txt") as f :
    a=f.read()
    b=a.split("$")
    print("list is : \n",b)
    print("Name : {} \n Age: {} \n Language : {} \n ".format(b[0],b[1],b[2]))

