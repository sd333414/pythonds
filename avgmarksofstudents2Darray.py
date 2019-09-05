#2D array of students marks
ia = [['sai',100],['jeevan',200],['sai',200],['jeevan',700],['sai',900],['jeevan',2000],['sai',900]]
b = {}
c = {}
for i in a:
    name=i[0]
    score=i[1]
    if name in b:

        b[name]=(b[name]+score)
        c[name]=c[name]+1

    else:
        b[name]=score
        c[name]=1
print(b)
print(c)
