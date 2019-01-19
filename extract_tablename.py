def extract(x,ta):
    a=x.strip().split()
    i=0
    while(i<len(a)):
        if(a[i]=='TABLE'):
            if(a[i+1]=='IF' and a[i+2]=='EXISTS'):
                cur=a[i+3].strip(';').strip('`')
                ta.append(cur)
                break
            else:
                cur=a[i+1].strip('(').strip('`')
                ta.append(cur)
                break
        i=i+1
ta=[]
file=open("create_schema.sql","r")
out=open("out.txt",'w')
lines=file.readlines()
for line in lines:
    extract(line,ta)
ta=list(set(ta))
out.write(str(len(ta)))
for i in range(len(ta)):
    out.write("\n")
    out.write((ta[i]))
file.close()
out.close()

"""if 'k_advisor_info' in ta:
    print("FOUND")
else:
    print("NOT found")"""
