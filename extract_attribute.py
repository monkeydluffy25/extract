import csv
def find(v):
    for i in range(len(v)):
        if 'PRIMARY' in v[i]:
            return True,v[i]['PRIMARY']
    return False,'-'
def extract(x):
    a=x.strip().split()
    i=0
    while(i<len(a)):
        if(a[i]=='TABLE'):
            if(a[i+1]=='IF' and a[i+2]=='EXISTS'):
                return None
            else:
                cur=a[i+1].strip('(').strip('`')
                return cur
        i=i+1
    return None
file=open("create_schema.sql","r")
out=open("attributes.txt",'w')
lines=file.readlines()
actual=[]
for line in lines:
    actual.append(line)
i=0
print(len(actual))
glo={}
while(i<len(actual)):
    curr=extract(actual[i])
    if(curr!=None and ('(' in actual[i].strip().split())):
        lis=[]
        while(i<len(actual)-1):
            i=i+1
            line=actual[i].strip()
            key=actual[i].strip().strip(',').split()
            k=0
            while(k<len(key)-1):
                keys={}
                if(key[k]=='KEY' and (k>0 and key[k-1]=='PRIMARY')):
                    keys['PRIMARY']=str(key[k+1].strip('(').strip(')').strip('`'))
                    #print(key[k+1].strip('(').strip(')').strip('`'))
                if(key[k]=='KEY' and k<len(key)-2 and key[k+2]!='REFERENCES'):
                    keys['KEY']=key[k+2].strip('(').strip(')').strip('`')
                k=k+1
                if(len(keys)!=0):
                    lis.append(keys)
            if(len(line)>0 and line[0]=='`'):
                j=1
                while(line[j]!='`'):
                    j=j+1
                line1=line[1:j]
                lis.append(line1)
            if('TABLE' in actual[i].strip().split()):
                glo[curr]=lis
                break
    else:
        i=i+1
out.write(str(len(glo)))
for i in glo:
    out.write("\n")
    out.write(str(i)+"="+str(glo[i]))
file.close()
out.close()
with open('attribute.csv', 'w',newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Table Name','Column Name','Primary Key'])
    for key, value in glo.items():
        fa,pra=find(value)
        for i in range(len(value)):
            if isinstance(value[i], dict):
                continue
            else:
                if(fa):
                    writer.writerow([key, value[i],pra])
                else:
                    writer.writerow([key, value[i],pra])
