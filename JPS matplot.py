from ast import Import
from operator import index
from re import L
from tkinter import N
from typing import List
import numpy as np
import math
import matplotlib.pyplot as plt

startX=0
startY=0
endY=19
endX=19


plot1=np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])

               
visited=np.copy(plot1)###########################
preNode=[[(11,11) for i in range(plot1.shape[1])] for j in range(plot1.shape[0])]#########
#print(preNode)
obstacle=np.copy(plot1)##############################
Hcost=np.copy(plot1)################################################
Gcost=np.copy(plot1)##################################################
cost=[]
List1=[]
List2=[]
List3=[]
List4=[]
ImportL=[]
ImportLnotSame=[]
ListCost=[]
PickList=[]
inputY=0
inputX=0
preX=0
PreY=0
dy=[-1,-1,0,1,1,1,0,-1]###########################
dx=[0,1,1,1,0,-1,-1,-1]#############################
plotX = []###########################################
plotY = []##############################################
visited2=np.copy(plot1)###########################








# for y in range(plot1.shape[0]):
#     for x in range(plot1.shape[1]):
#         if(plot1[y][x]>0):
#             plot1[y][x]=1
#             plotX.append(x)
#             plotY.append(y)

# plotX=np.array(plotX)
# plotY=np.array(plotY)

ObstacleRange = 1
for y in range(plot1.shape[0]):
    for x in range(plot1.shape[1]):
        if(plot1[y][x] == 1):
            visited2[y][x] = 1
            for i in range(1, ObstacleRange + 1):
                for j in range(i+1):
                    if(y + j >= 0 and y + j < plot1.shape[0] and x + i-j >= 0 and x + i-j < plot1.shape[1] and visited2[y+j][x+i-j] == 0):
                        obstacle[y+j][x+i-j] = 8
                        plot1[y+j][x+i-j] = 8
                        visited2[y+j][x+i-j] = 1
                        
                    if(y + j >= 0 and y + j < plot1.shape[0] and x - (i-j) >= 0 and x - (i-j) < plot1.shape[1] and visited2[y+j][x-(i-j)] == 0):
                        obstacle[y+j][x-(i-j)] = 8
                        plot1[y+j][x-(i-j)] = 8
                        visited2[y+j][x-(i-j)] = 1
                        
                    if(y-j >= 0 and y-j < plot1.shape[0] and x+i-j >= 0 and x+i-j < plot1.shape[1] and visited2[y-j][x+i-j] == 0):
                        obstacle[y-j][x+i-j] = 8
                        plot1[y-j][x+i-j] = 8
                        visited2[y-j][x+i-j] = 1
                        
                    if(y-j >= 0 and y-j < plot1.shape[0] and x-(i-j) >= 0 and x-(i-j) < plot1.shape[1] and visited2[y-j][x-(i-j)] == 0):
                        obstacle[y-j][x-(i-j)] = 8
                        plot1[y-j][x-(i-j)] = 8
                        visited2[y-j][x-(i-j)] = 1
plotX = []###################
plotY = []###################

for y in range(plot1.shape[0]):
    for x in range(plot1.shape[1]):
        if(plot1[y][x]>0):
            plot1[y][x]=1
            plotX.append(x)
            plotY.append(y)


plotX = np.array(plotX) ######################     
plotY = np.array(plotY)##############################
def go1(y,x,i,PY,PX):
    searchN=0
    PreX=PX
    PreY=PY
    ny=y
    nx=x

    while (ny >= 0 and ny < plot1.shape[0] and nx >= 0 and nx < plot1.shape[1]): 
            ny=ny+dy[i]
            nx=nx+dx[i]
            if (ny  >= 0 and ny < plot1.shape[0] and nx >= 0 and nx < plot1.shape[1] and obstacle[ny, nx]== 0):
                searchN+=1
                if preNode[ny][nx]==(11,11):
                    preNode[ny][nx]=(y,x)
                    #visited[ny][nx]=1

            else:
                ny=ny-dy[i]
                nx=nx-dx[i]
                break
            if(ny==endY and nx==endX):
                ImportLnotSame.insert(0,(ny,nx))
                break
            #visited[ny][nx]=1
    #visited[ny][nx]=0
    if (ny >= 0 and ny < plot1.shape[0] and nx >= 0 and nx < plot1.shape[1]): 
        ny=y
        nx=x
        if i==0:
            List1.append((searchN,(ny,nx),(PreY,PreX)))
        if i==2:
            List2.append((searchN,(ny,nx),(PreY,PreX)))
        if i==4:
            List3.append((searchN,(ny,nx),(PreY,PreX)))
        if i==6:
            List4.append((searchN,(ny,nx),(PreY,PreX)))
    if(ny==endY and nx==endX):
        ImportLnotSame.insert(0,(ny,nx)) 





def go3(y,x,i,PY,PX):
    searchN=0
    PreX=PX
    PreY=PY
    ny=y
    nx=x  
    while ny >= 0 and ny < plot1.shape[0] and nx >= 0 and nx < plot1.shape[1]: 
            ny=ny+dy[i]
            nx=nx+dx[i]
            if ( ny >= 0 and ny < plot1.shape[0] and nx >= 0 and nx < plot1.shape[1] and obstacle[ny, nx]== 0):               
                    searchN+=1
                    if preNode[ny][nx]==(11,11):
                        preNode[ny][nx]=(y,x)
                    #visited[ny][nx]=1

            else:
                ny=ny-dy[i]
                nx=nx-dx[i]
                break
    #visited[ny][nx]=0
    if (ny >= 0 and ny < plot1.shape[0] and nx >= 0 and nx < plot1.shape[1]): 
        ny=y
        nx=x  
        if i==0:
            List1.insert(0,(searchN,(ny,nx),(PreY,PreX)))
        if i==2:
            List2.insert(0,(searchN,(ny,nx),(PreY,PreX)))
        if i==4:
            List3.insert(0,(searchN,(ny,nx),(PreY,PreX)))
        if i==6:
            List4.insert(0,(searchN,(ny,nx),(PreY,PreX)))







def go2(y,x,i):
    PreX=x
    PreY=y
    ny=y
    nx=x
    while (ny >= 0 and ny < plot1.shape[0] and nx >= 0 and nx < plot1.shape[1]):
            ny+=dy[i]
            nx+=dx[i]
            if (ny>=0 and ny < plot1.shape[0] and nx >= 0 and nx < plot1.shape[1] and obstacle[ny, nx]== 0):
                # if (visited[ny, nx] == 1):
                #     break         
                if preNode[ny][nx]==(11,11):
                    preNode[ny][nx]=(PreY,PreX)
                if i==1:
                    go1(ny,nx,0,PreY,PreX)
                    go1(ny,nx,2,PreY,PreX)
                if i==3:
                    #print('a')
                    go3(ny,nx,2,PreY,PreX)
                    go1(ny,nx,4,PreY,PreX)
                if i==5:
                    go3(ny,nx,4,PreY,PreX)
                    go1(ny,nx,6,PreY,PreX)
                if i==7:
                    go3(ny,nx,6,PreY,PreX)
                    go3(ny,nx,0,PreY,PreX)
                #visited[ny][nx]=1
            elif (ny>=0 and ny < plot1.shape[0] and nx >= 0 and nx < plot1.shape[1] and obstacle[ny, nx]== 1):
                if i==1:
                    List1.append((-1,(ny,nx),(PreY,PreX)))
                    List2.append((-1,(ny,nx),(PreY,PreX)))
                elif i==3:
                    List2.insert(0,(-1,(ny,nx),(PreY,PreX)))
                    List3.append((-1,(ny,nx),(PreY,PreX)))
                elif i==5:
                    List3.insert(0,(-1,(ny,nx),(PreY,PreX)))
                    List4.append((-1,(ny,nx),(PreY,PreX)))
                else:
                    List4.insert(0,(-1,(ny,nx),(PreY,PreX)))
                    List1.insert(0,(-1,(ny,nx),(PreY,PreX)))
                break
            else:
                ny=ny-dy[i]
                nx=nx-dx[i]
                if preNode[ny][nx]==(11,11):
                    preNode[ny][nx]=(PreY,PreX)
                    #visited[ny][nx]=1
                # ImportLX.append(nx)
                # ImportLY.append(ny)
                break






def jps(y,x):
    visited[y][x]=1
    if(y >= 0 and y < plot1.shape[0] and x >= 0 and x < plot1.shape[1]):
        go1(y,x,0,y,x)
        go1(y,x,2,y,x)
        go1(y,x,4,y,x)
        go1(y,x,6,y,x)
        go2(y,x,1)
        go2(y,x,3)
        go2(y,x,5)
        go2(y,x,7)






def ImportantNode():
    for i in range(len(List1)-1):
        if List1[i][0]-List1[i+1][0]>1 and visited[List1[i+1][1][0]-List1[i+1][0]-1][List1[i][1][1]]==0 and obstacle[List1[i+1][1][0]-List1[i+1][0]-1][List1[i][1][1]]==0:
            ImportL.append((List1[i+1][1][0]-List1[i+1][0]-1,List1[i][1][1]))
        elif List1[i][0]-List1[i+1][0]<-1 and visited[List1[i][1][0]-List1[i][0]-1][List1[i+1][1][1]]==0 and obstacle[List1[i][1][0]-List1[i][0]-1][List1[i+1][1][1]]==0:
            ImportL.append((List1[i][1][0]-List1[i][0]-1,List1[i+1][1][1]))
            #print(i)
    for i in range(0,len(List1)):
        List1.pop(0)
        
    for i in range(len(List2)-1):
        #print(i)
        if List2[i][0]-List2[i+1][0]>1 and visited[List2[i][1][0]][List2[i+1][1][1]+List2[i+1][0]+1]==0 and obstacle[List2[i][1][0]][List2[i+1][1][1]+List2[i+1][0]+1]==0:
            ImportL.append((List2[i][1][0],List2[i+1][1][1]+List2[i+1][0]+1))
        elif List2[i][0]-List2[i+1][0]<-1 and visited[List2[i+1][1][0]][List2[i][1][1]+List2[i][0]+1]==0 and obstacle[List2[i+1][1][0]][List2[i][1][1]+List2[i][0]+1]==0:
            ImportL.append((List2[i+1][1][0],List2[i][1][1]+List2[i][0]+1))
    for i in range(0,len(List2)):
        List2.pop(0)
    
    for i in range(len(List3)-1):
        if List3[i][0]-List3[i+1][0]>1 and visited[List3[i+1][1][0]+List3[i+1][0]+1][List3[i][1][1]]==0 and obstacle[List3[i+1][1][0]+List3[i+1][0]+1][List3[i][1][1]]==0:
            ImportL.append((List3[i+1][1][0]+List3[i+1][0]+1,List3[i][1][1]))
        elif List3[i][0]-List3[i+1][0]<-1 and visited[List3[i][1][0]+List3[i][0]+1][List3[i+1][1][1]]==0 and obstacle[List3[i][1][0]+List3[i][0]+1][List3[i+1][1][1]]==0:
            ImportL.append((List3[i][1][0]+List3[i][0]+1,List3[i+1][1][1]))
    for i in range(0,len(List3)):
        List3.pop(0)

    for i in range(len(List4)-1):
        if List4[i][0]-List4[i+1][0]>1 and visited[List4[i][1][0]][List4[i+1][1][1]-List4[i+1][0]-1]==0 and obstacle[List4[i][1][0]][List4[i+1][1][1]-List4[i+1][0]-1]==0:
            ImportL.append((List4[i][1][0],List4[i+1][1][1]-List4[i+1][0]-1))
        elif List4[i][0]-List4[i+1][0]<-1 and visited[List4[i+1][1][0]][List4[i][1][1]-List4[i][0]-1]==0 and obstacle[List4[i+1][1][0]][List4[i][1][1]-List4[i][0]-1]==0:
            ImportL.append((List4[i+1][1][0],List4[i][1][1]-List4[i][0]-1))
    for i in range(0,len(List4)):
        List4.pop(0)
    for value in ImportL:
        if value not in ImportLnotSame:
            if visited[value[0]][value[1]]==0:
                ImportLnotSame.append(value)
    for i in range(0,len(ImportLnotSame)-1):
        if ImportLnotSame[i]==(endY,endX):
            ImportLnotSame[0],ImportLnotSame[i]=ImportLnotSame[i],ImportLnotSame[0]





            
def search(y,x):
    if(y >= 0 and y < plot1.shape[0] and x >= 0 and x < plot1.shape[1]):   
        a = abs(endY - (y))
        b = abs(endX - (x))
        if(a >= b):
            Hcost[y][x]= b*14 + (a-b)*10
        else:
            Hcost[y][x]= a*14 + (b-a)*10
        c=abs(preNode[y][x][0]-y)
        d=abs(preNode[y][x][1]-x)
        if(c >= d):
            Gcost[y][x]= d*14 + (c-d)*10
        else:
            Gcost[y][x]= c*14 + (d-c)*10
        cost.append(Hcost[y][x]+ Gcost[y][x])







def RealMain(y,x):
    jps(y,x)
    print(List3)
    ImportantNode()
    # print(List3)
    # print(List4)
    print(ImportLnotSame)
    inputY=ImportLnotSame[0][0]
    inputX=ImportLnotSame[0][1]
    PickList.append((inputY,inputX))
    print(PickList)
    PreX=x
    PreY=y
    while inputY!=endY or inputX!=endX:
        jps(inputY,inputX)
        ImportantNode()
        for i in range(len(ImportLnotSame)):
            search(ImportLnotSame[i][0],ImportLnotSame[i][1])
            ListCost.append(cost[i])
        for i in range(len(ImportLnotSame)-1):
            if ListCost[i]>ListCost[i+1]:
                ListCost[i+1],ListCost[i]=ListCost[i],ListCost[i+1]
                ImportLnotSame[i+1],ImportLnotSame[i]=ImportLnotSame[i],ImportLnotSame[i+1]
                for j in range(i+1,0,-1):
                    if ListCost[j]<ListCost[j-1]:
                        ListCost[j],ListCost[j-1]=ListCost[j+1],ListCost[j]
                        ImportLnotSame[j],ImportLnotSame[j-1]=ImportLnotSame[j-1],ImportLnotSame[j]
                        
        PreY=inputY
        PreX=inputX
        try:                
            PickList.append((inputY,inputX))
            inputY=ImportLnotSame[0][0]
            inputX=ImportLnotSame[0][1]
        # print(ImportLnotSame)
        # print(inputY)
        # print(inputX)
        # print(visited)
            ImportLnotSame.pop(0)
        except:
            break
        # print(cost)
        if inputY==endY and inputX==endX:
            visited[inputY][inputX]=1    





            
              
RealMain(0,0)
pathX=[]
pathY=[]
def backtracking(y,x):
    #print(preNode)
    print('s')
    print(y)
    print(x)
    ny=preNode[y][x][0]
    nx=preNode[y][x][1]
    #print("ny:%d  /\   nx:%d",(ny,nx))
    pathX.append(nx)
    pathY.append(ny)
    plot1[ny][nx]=88
    plot1[endY][endY]=88
    if ny==startY and nx==startX:
        return 100
    backtracking(ny,nx)

pathX.append(endX)
pathY.append(endY)
backtracking(endY,endX)

pathX=np.array(pathX)
pathY=np.array(pathY)
# print(preNode)
mapsize=plot1.shape[0]#############################y축으로의 맵의 크기

plt.figure(figsize=(12,12)) ##########################띄우는 창의 크기를 지정
#print("pathX:",pathX)
#print("pathY:",pathY)
plt.plot(pathX,mapsize-pathY,'bo')#####################경로를 점으로 표현해줌
plt.plot(plotX,mapsize-plotY,'bo',color='red',markersize=10)
#plt.plot(endX,mapsize-endY,'bo')########################목적지 점 찍기


plt.axis([-1,mapsize,0,mapsize+1])####################################맵의 눈금을 어디서부터 시작하고 어디서 끝낼지
plt.xticks(range(mapsize+1))#######################################x축으로의 칸을 몇 칸으로 나눌지
plt.yticks(range(mapsize+1))#########################################y축으로의 칸을 몇 칸으로 나눌지
plt.grid()########################################################눈금 표현
#plt.plot(opennodeX,opennodeY,'bo')
plt.show()