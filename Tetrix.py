from tkinter import *
import time,random,math

fall=True
nextTetra=random.randint(1,7)
curTetra=nextTetra
tetraSize=30
Key=''
Score=0
tetraPos=[0,5]

def TextOut(x,y,text,w):
    w.create_text(x+1,y+1,text=text,font=20,fill="black")
    w.create_text(x+1,y-1,text=text,font=20,fill="black")
    w.create_text(x-1,y+1,text=text,font=20,fill="black")
    w.create_text(x-1,y-1,text=text,font=20,fill="black")
    w.create_text(x,y,text=text,font=20,fill="white")
    
def GameScreen(w):
    Theme="black"
    global nextTetra
    global tTab
    x=1
    y=1
    color=""
    w.create_rectangle(1,1,tetraSize*10+270,tetraSize*20+2,fill="grey",outline="grey")
    w.create_rectangle(1,1,tetraSize*10+1,tetraSize*20+2,fill=Theme)
    for row in tTab:
        for el in row:
            if el%10==1:
                color="blue"
            if el%10==2:
                color="red"
            if el%10==3:
                color="green"
            if el%10==4:
                color="cyan"
            if el%10==5:
                color="yellow"
            if el%10==6:
                color="purple"
            if el%10==7:
                color="orange"
            if el%10<8 and el!=0:
                w.create_rectangle(x,y,x+tetraSize,y+tetraSize,fill=color,outline=Theme)
            x+=tetraSize
        x=1
        y+=tetraSize
    x=0
    Sc='Score = '+str(Score)
    TextOut(400,20,Sc,w)
    Next=NextTetra()
    for row in Next:
        for el in row:
            if el==1:
                color="blue"
            if el==2:
                color="red"
            if el==3:
                color="green"
            if el==4:
                color="cyan"
            if el==5:
                color="yellow"
            if el==6:
                color="purple"
            if el==7:
                color="orange"
            if el!=0:
                w.create_rectangle(x+400,y-500,x+400+tetraSize,y-500+tetraSize,fill=color,outline="grey")
            x+=tetraSize
        x=0
        y+=tetraSize 

def GenTetra(tet):
    global tTab
    if tet==1:
        tTab[0][5]=1
        tTab[1][5]=1
        tTab[2][5]=1
        tTab[2][6]=1
    if tet==2:
        tTab[0][5]=2
        tTab[0][6]=2
        tTab[1][5]=2
        tTab[1][6]=2
    if tet==3:
        tTab[0][4]=3
        tTab[0][5]=3
        tTab[0][6]=3
        tTab[1][5]=3
    if tet==4:
        tTab[0][5]=4
        tTab[1][5]=4
        tTab[2][5]=4
        tTab[3][5]=4
    if tet==5:
        tTab[0][5]=5
        tTab[1][5]=5
        tTab[2][5]=5
        tTab[2][4]=5
    if tet==6:
        tTab[0][5]=6
        tTab[1][5]=6
        tTab[1][4]=6
        tTab[2][4]=6
    if tet==7:
        tTab[0][5]=7
        tTab[1][5]=7
        tTab[1][6]=7
        tTab[2][6]=7
    return tTab

def NextTetra():
    global nextTetra
    tet=nextTetra
    Tab=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    if tet==1:
        Tab[0][0]=1
        Tab[1][0]=1
        Tab[2][0]=1
        Tab[2][1]=1
    if tet==2:
        Tab[0][0]=2
        Tab[0][1]=2
        Tab[1][0]=2
        Tab[1][1]=2
    if tet==3:
        Tab[0][0]=3
        Tab[0][1]=3
        Tab[0][2]=3
        Tab[1][1]=3
    if tet==4:
        Tab[0][0]=4
        Tab[1][0]=4
        Tab[2][0]=4
        Tab[3][0]=4
    if tet==5:
        Tab[0][1]=5
        Tab[1][1]=5
        Tab[2][1]=5
        Tab[2][0]=5
    if tet==6:
        Tab[0][1]=6
        Tab[1][1]=6
        Tab[1][0]=6
        Tab[2][0]=6
    if tet==7:
        Tab[0][0]=7
        Tab[1][0]=7
        Tab[1][1]=7
        Tab[2][1]=7
    return Tab

def TetraStop():
    global tTab
    x=0
    y=0
    for row in tTab:
        for el in row:
            if el<10 and el!=0:
                tTab[y][x]=el*10+el
            x+=1
        x=0
        y+=1
    global fall
    fall = True
    return tTab

def TetraDown():
    global tTab
    x=0
    y=19
    Tab=[]
    for i in range(20):
        Tab.append([])
        for j in range(10):
            Tab[i].append(0)
    for row in reversed(tTab):
        for el in row:
            if el<10 and el!=0:
                try:
                    if Tab[y+1][x]==0:
                        Tab[y][x]=0
                        Tab[y+1][x]=el
                    else:
                        Tab=TetraStop()
                        return Tab
                except Exception:
                    Tab=TetraStop()
                    return Tab
            if el>10:
                Tab[y][x]=el
            x+=1
        y-=1
        x=0
    global Score
    Score+=10
    return Tab

def TetraRight():
    global tTab
    x=9
    y=0
    Tab=[]
    for i in range(20):
        Tab.append([])
        for j in range(10):
            Tab[i].append(0)
    for row in tTab:
        for el in reversed(row):
            if el<10 and el!=0:
                try:
                    if Tab[y][x+1]==0:
                        Tab[y][x]=0
                        Tab[y][x+1]=el
                    else:
                        return tTab
                except Exception:
                    return tTab
            if el>10:
                Tab[y][x]=el
            x-=1
        y+=1
        x=9
    return Tab

def TetraLeft():
    global tTab
    x=0
    y=0
    Tab=[]
    for i in range(20):
        Tab.append([])
        for j in range(10):
            Tab[i].append(0)
    for row in tTab:
        for el in row:
            if el<10 and el!=0:
                if x==0:
                    return tTab
                if Tab[y][x-1]==0:
                    Tab[y][x]=0
                    Tab[y][x-1]=el
                else:
                    return tTab
            if el>10:
                Tab[y][x]=el
            x+=1
        y+=1
        x=0
    return Tab

def Rotate():
    global tTab
    coords=findTetra()
    sq=[[10,0],[20,0]]
    for i in range(4):
        if sq[0][0]>coords[0][i]:
            sq[0][0]=coords[0][i]
        if sq[0][1]<coords[0][i]:
            sq[0][1]=coords[0][i]
        if sq[1][0]>coords[1][i]:
            sq[1][0]=coords[1][i]
        if sq[1][0]<coords[1][i]:
            sq[1][1]=coords[1][i]
    temp=[]
    print(sq)
    x=0
    for j in range(sq[0][0],sq[0][1]+1):
        temp.append([])
    for i in range(sq[1][0],sq[1][1]+1):
        for j in range(sq[0][0],sq[0][1]+1):
            temp[x].append(tTab[i][j])
            tTab[i][j]=0
            x+=1
        x=0
    x=sq[0][1]
    y=sq[1][0]
    i=0
    j=0
    for row in temp:
        for el in row:
            tTab[y+i][x-j]=el
            j+=1
        j=0
        i+=1
    return tTab
def findTetra():
    x=0
    y=0
    global tTab
    coord=[[],[]]
    for row in tTab:
        for el in row:
            if el==curTetra:
                coord[0].append(x)
                coord[1].append(y)
            x+=1
        x=0
        y+=1
    return coord
def CleanedFill():
    global tTab
    y=19
    Row=[0,0,0,0,0,0,0,0,0,0]
    for row in reversed(tTab):
        if row==Row:
            for i in reversed(range(y+1)):
                tTab[i]=tTab[i-1]
                tTab[i-1]=Row
            break
        y-=1
    tTab[19]=tTab[0]
    tTab[0]=Row
    return tTab
    
def LineCheck():
    global tTab
    y=0
    Row=[0,0,0,0,0,0,0,0,0,0]
    RowCleaned=0
    RowClean=True
    global Score
    for row in tTab:
        RowClean=True
        for el in row:
            if el==0:
                RowClean=False
                break
        if RowClean:
            tTab[y]=Row
            RowCleaned+=1
            Score+=1000
        y+=1
    for i in range(RowCleaned):
        tTab = CleanedFill()
    return tTab

def key(event):
    global Key
    Key = event.keysym
    
root = Tk()
root.title("Tetrix")
window = Canvas(root, width = tetraSize * 10 + 270,height = tetraSize * 20+2)
window.pack()
tTab=[]
for i in range(20):
    tTab.append([])
    for j in range(10):
        tTab[i].append(0)
zero=time.time()
PervFrame=zero
root.bind_all('<Key>', key)
FrameTime=1
while True:
    window.delete("all")
    if fall:
        tTab = LineCheck()
        tTab = GenTetra(nextTetra)
        curTetra=nextTetra
        while nextTetra==curTetra:
            nextTetra=random.randint(1,7)
        fall=False
    if Key!='':
        if Key=='Right':
            tTab = TetraRight()
            Key=''
        if Key=='Left':
            tTab = TetraLeft()
            Key=''
        if Key=='space':
            tTab = TetraDown()
            Key=''
        if Key=='r':
            tTab = Rotate()
            Key=''
    GameScreen(window)
    root.update()
    if time.time()-PervFrame>FrameTime:
        tTab = TetraDown()
        GameScreen(window)
        root.update()
        PervFrame = time.time()
        FrameTime=1/math.sqrt(time.time()-zero)
