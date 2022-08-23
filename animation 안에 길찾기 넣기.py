import numpy as np
import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation


startY=30
startX=0
fig,ax=plt.subplots()


plot1 = np.zeros([60,60])
def update(i):
    plt.cla()
    plot=plot1.copy()
    for i in range(10):
        plot[3* random.randint(2,18)][3* random.randint(2,18)] = 1

        
    endY=plot.shape[0]-1
    endX=plot.shape[1]-1
    endY, endX = 0, 59

    preNode = [[(11,11) for i in range(plot.shape[1])] for j in range(plot.shape[0])]
    visited = plot * 2 #PriorityQueue에 들어갔다 나온 노드를 방문처리
    Gcost = plot * 2
    Hcost = plot * 2
    Fcost = plot * 2
    path = plot * -1
    opennode=[]
    dfL=[]
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    plotX=[]
    plotY=[]

    for y in range(plot.shape[0]):
        for x in range(plot.shape[1]):
            if(plot[y][x]>0):
                plot[y][x]=1
                plotX.append(x)
                plotY.append(y)

    plotX=np.array(plotX)
    plotY=np.array(plotY)

    ObstacleRange = 3
    for y in range(plot.shape[0]):
        for x in range(plot.shape[1]):
            if(plot[y][x] == 1):
                visited[y][x] = 1
                for i in range(1, ObstacleRange + 1):
                    for j in range(i+1):
                        if(y + j >= 0 and y + j < plot.shape[0] and x + i-j >= 0 and x + i-j < plot.shape[1] and visited[y+j][x+i-j] == 0):
                            plot[y+j][x+i-j] = 8
                            visited[y+j][x+i-j] = 1
                            
                        if(y + j >= 0 and y + j < plot.shape[0] and x - (i-j) >= 0 and x - (i-j) < plot.shape[1] and visited[y+j][x-(i-j)] == 0):
                            plot[y+j][x-(i-j)] = 8
                            visited[y+j][x-(i-j)] = 1
                            
                        if(y-j >= 0 and y-j < plot.shape[0] and x+i-j >= 0 and x+i-j < plot.shape[1] and visited[y-j][x+i-j] == 0):
                            plot[y-j][x+i-j] = 8
                            visited[y-j][x+i-j] = 1
                            
                        if(y-j >= 0 and y-j < plot.shape[0] and x-(i-j) >= 0 and x-(i-j) < plot.shape[1] and visited[y-j][x-(i-j)] == 0):
                            plot[y-j][x-(i-j)] = 8
                            visited[y-j][x-(i-j)] = 1
    plotX = []
    plotY = []

    for y in range(plot.shape[0]):
        for x in range(plot.shape[1]):
            if(plot[y][x]>0):
                plot[y][x]=1
                plotX.append(x)
                plotY.append(y)


    plotX = np.array(plotX)      
    plotY = np.array(plotY)



    def search(y,x):
            if(y >= 0 and y < plot.shape[0] and x >= 0 and x < plot.shape[1]):
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
                    Gcost[y][x]= d*14 + (c-d)*10
                        

    ####################################Hcost와 Gcost를 더한 가격 Fcost를 구하는 함수
    def go(y,x,i):
            sY,sX=y,x
            ny=y+dy[i]
            nx=x+dx[i]
            while(ny >= 0 and ny < plot.shape[0] and nx >= 0 and nx < plot.shape[1]):
                    if plot[ny][nx]==1:
                            break
                    
                    if visited[ny][nx]==0:
                            visited[ny][nx]=1
                            if i%4==0:
                                    if nx-1<0:
                                            pass
                                    elif plot[ny][nx-1]==0 and plot[ny-dy[i]][nx-1]==1:
                                            opennode.append((ny-dy[i],nx))
                                    if nx+1>=plot.shape[1]:
                                            pass
                                    elif plot[ny][nx+1]==0 and plot[ny-dy[i]][nx+1]==1:
                                            opennode.append((ny-dy[i],nx))
                                    preNode[ny][nx]=(sY,sX)
                            else:
                                    if ny-1<0:
                                            pass
                                    elif plot[ny-1][nx]==0 and plot[ny-1][nx-dx[i]]==1 :
                                                    opennode.append((ny,nx-dx[i]))
                                    if ny+1 >=plot.shape[0]:
                                            pass
                                    elif plot[ny+1][nx]==0 and plot[ny+1][nx-dx[i]]==1:
                                                    opennode.append((ny,nx-dx[i]))
                                    preNode[ny][nx]=(sY,sX)
                    else:
                            break
                    ny+=dy[i]
                    nx+=dx[i]

                    
    def go2(y,x,i):
            X=x
            Y=y
            newy=y+dy[i]
            newx=x+dx[i]
            while(newy >= 0 and newy < plot.shape[0] and newx >= 0 and newx < plot.shape[1]):
                    if visited[newy][newx]==0:
                            visited[newy][newx]=1
                            preNode[newy][newx]=(Y,X)
                            if newy+dy[i]>=plot.shape[0] or newy+dy[i]<0 or newx+dx[i]>=plot.shape[1] or newx+dx[i]<0:
                                    pass
                            elif visited[newy+dy[i]][newx+dx[i]]==1:
                                    if visited[newy+dy[i]][newx]==0:
                                            opennode.append((newy,newx))
                                    if visited[newy+dy[i]][newx-dx[i]]==0:
                                            opennode.append((newy,newx))
                            else:
                                    pass
                            if i==7:
                                    go(newy,newx,0)
                                    go(newy,newx,6)
                            else:
                                    go(newy,newx,i-1)
                                    go(newy,newx,i+1)
                    else:
                            break

                    newx+=dx[i]
                    newy+=dy[i]
                    
    def jps(y,x):
            if(y >= 0 and y < plot.shape[0] and x >= 0 and x < plot.shape[1]):
                    for i in range(0,8):
                            if i%2==0:
                                    go(y,x,i)
                            else:
                                    go2(y,x,i)
                                    ########################################################jps 실행


    opennodeX=[]
    opennodeY=[]

    opennode.append((startY,startX))
    while len(opennode)>0:
            if opennode[0][0]==endY and opennode[0][1]==endX:
                    break
            jps(opennode[0][0],opennode[0][1])
            
            opennodeX.append(opennode[0][0])
            opennodeY.append(opennode[0][1])
            opennode.pop(0)
            for i in range(0,len(opennode)):
                    newy,newx=opennode[i]
                    search(newy,newx)
                    Fcost=Gcost+Hcost
                    dfL.append(Fcost[newy][newx])
                            ########Gcost,Hcost,Fcost를 구하는 부분
            for i in range(0,len(opennode)-1):
                    if dfL[i]>=dfL[i+1]:
                            dfL[i],dfL[i+1]=dfL[i+1],dfL[i]
                            opennode[i],opennode[i+1]=opennode[i+1],opennode[i]
                            for j in range(i+1,0,-1):
                                    if dfL[j]<dfL[j-1]:
                                            dfL[j],dfL[j-1]=dfL[j-1],dfL[j]
                                            opennode[j],opennode[j-1]=opennode[j-1],opennode[j]
                                            ##############Fcost가 큰 순서대로 opennode의 좌표들을 재배치하는 과정




    opennodeY2=[]
    for i in range(0,len(opennodeY)):
        opennodeY2.append(plot.shape[0])
        
    opennodeY=np.array(opennodeY)
    opennodeY2=np.array(opennodeY2)


        

    pathX=[]
    pathY=[]
    pathX.append(endX)
    pathY.append(endY)
    def backtracking(y,x):
        ny=preNode[y][x][0]
        nx=preNode[y][x][1]
        #print("ny:%d  /\   nx:%d",(ny,nx))
        
        pathX.append(nx)
        pathY.append(ny)
        if ny==startY and nx==startX:
            return 100
        backtracking(ny,nx)
    backtracking(endY,endX)


    pathX=np.array(pathX)
    pathY=np.array(pathY)

    mapsize=plot.shape[0]#############################y축으로의 맵의 크기

    #plt.figure(figsize=(12,12)) ##########################띄우는 창의 크기를 지정
    #print("pathX:",pathX)
    #print("pathY:",pathY)
    plt.plot(pathX,mapsize-pathY)#####################경로를 점으로 표현해줌
    plt.plot(plotX,mapsize-plotY,'s',color='red',markersize=10)
    #plt.plot(endX,mapsize-endY,'bo')########################목적지 점 찍기


    plt.axis([-1,mapsize,0,mapsize+1])####################################맵의 눈금을 어디서부터 시작하고 어디서 끝낼지
    plt.xticks(range(mapsize+1))#######################################x축으로의 칸을 몇 칸으로 나눌지
    plt.yticks(range(mapsize+1))#########################################y축으로의 칸을 몇 칸으로 나눌지
    plt.grid()########################################################눈금 표현
    #plt.plot(opennodeX,opennodeY,'bo')


ani=FuncAnimation(fig,update,interval=100)
plt.show()
