from openpyxl import *

def invert(x):
    out=[]
    for i in range(len(x)):
        out.append(255-int(x[i]))
    return out

def split(x):
    x = x.split('/')
    for i in range(len(x)):
        x[i] = x[i].split('.')
    return x

def dec2bin(x):
    x = bin(int(x)).replace('0b','')
    if(len(x)<8):
        for k in range(8-len(x)):
            x = str(x)+'0'
    return x

def prefix(x):
    out=0
    connect=''
    for i in range(len(x)):
        connect+=str(x[i])
    for i in range(len(connect)):
        out+=int(connect[i])
    return out

def getRange(x):
    count = 0
    for i in range(8):
        if(x[i]=='0'):
            count+=1 
    return square(2, count)-1

def square(x, y):
    out=1
    for i in range(y):
        out*=x
    return out

def checkCell(x):
    return x.count('.') == 6
    
def getIP(IP):
    print(checkCell(IP))
    IP=split(IP)
    allHosts = 1
    IP[1][3]=int(IP[0][3])+int(getRange(dec2bin(IP[1][3])))
    IPrange=IP[0][0]+'.'+IP[0][1]+'.'+IP[0][2]+'.'+str(int(IP[0][3])+allHosts)+' - '+IP[0][0]+'.'+IP[0][1]+'.'+IP[0][2]+'.'+str(IP[1][3]-allHosts)
    print(IPrange)

def getPosition(r,c):
    lis
    return str()

    
#getIP(str(input()))
IPfound = False

#fileName = str(input())
fileName = 'test.xlsx'

try:
    wb = load_workbook(fileName)
    ws = wb.active
except FileNotFoundError:
    wb = Workbook()
    ws = wb.active
    
while True:
    c,r=1,1
    if(ws.cell(row=r, column=c).value != None):
        if(checkCell(ws.cell(row=r, column=c).value)):
            print(ws.cell(row=r, column=c).value)
            print(getIP(ws.cell(row=r, column=c).value))
            break
        else:
            print('ne')
            r+=1
        
    IPfound=True
wb.save(fileName)
