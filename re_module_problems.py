import re

string="My DOB is 17/11/2003"
string1="My DOB is 18/11/2003"
string2="My DOB is 19/11/2003"

with open("sample.txt","w") as f:
    f.write(string+"\n"+ string1 + "\n" +string2)

with open("sample.txt","r") as f:
    list=f.read()
    print(list)

print(re.findall(r"\d{4}",list))