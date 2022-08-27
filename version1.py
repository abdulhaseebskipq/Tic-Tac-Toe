

#ABDUL HASEEB 1801009


#ZAKIR ULLAH 1801027



from numpy import*
def mark(x,list,m):
               if x==1:
                   list[0][0]=m
               elif x==2:
                   list[0][1]=m
               elif x==3:
                   list[0][2]=m
               elif x==4:
                   list[1][0]=m
               elif x==5:
                   list[1][1]=m
               elif x==6:
                   list[1][2]=m
               elif x==7:
                   list[2][0]=m
               elif x==8:
                   list[2][1]=m
               elif x==9:
                   list[2][2]=m
def illegal_moves(x,list):
    while x in list:
        print("It seems to be a illegal move")
        x=int(input("enter again where you want to mark!!!"))
    return(x)
def legal_moves(x):
    legal=[1,2,3,4,5,6,7,8,9]
    while x not in legal:
        print("It seems out of range")
        x=int(input("enter again where you want to mark!!!!"))
    return(x)
        
rmoves=[]
am=[1,2,3,4,5,6,7,8,9]
print("WELCOME BOTH PLAYERS TO THE WORLD OF TIC TAC TOE")
print("PLAYER ONE HAS SIGN 0 AND PLAYER TWO HAS SIGN 1")
dis=array([[1,2,3],[4,5,6],[7,8,9]])
print(dis)
n1=str(input("what is player one name?"))
n2=str(input("what is player two name?"))
s=len(rmoves)
while s!=9:
    if dis[0][0]==dis[0][1]==dis[0][2] or dis[1][0]==dis[1][1]==dis[1][2] or dis[2][0]==dis[2][1]==dis[2][2] or dis[0][0]==dis[1][0]==dis[2][0] or dis[0][1]==dis[1][1]==dis[2][1] or dis[0][2]==dis[1][2]==dis[2][2] or dis[0][0]==dis[1][1]==dis[2][2] or dis[0][2]==dis[1][1]==dis[2][0] or s==9:
                    break
                    
    else:
        print("                                        ",n1,"IS PLAYING!!!!...                          ")
        print("avialiable moves are:",am)
        y=int(input("Where you want to mark????"))
        o=illegal_moves(y,rmoves)
        g=legal_moves(o)
        rmoves.append(g)
        am.remove(g)
        m=0
        mark(g,dis,m)
        print(dis)
        s=len(rmoves)
        print("--------------------------------------------------------------------------------------------------------------------------------------------------")
        
    if  dis[0][0]==dis[0][1]==dis[0][2] or dis[1][0]==dis[1][1]==dis[1][2] or dis[2][0]==dis[2][1]==dis[2][2] or dis[0][0]==dis[1][0]==dis[2][0] or dis[0][1]==dis[1][1]==dis[2][1] or dis[0][2]==dis[1][2]==dis[2][2] or dis[0][0]==dis[1][1]==dis[2][2] or dis[0][2]==dis[1][1]==dis[2][0] or s==9: 
                    break

    else:
        print("                                       ",n2,"IS PLAYING!!!...                              ")
        print("avialiable moves are:",am)
        t=int(input("Where you want to mark???"))
        u=illegal_moves(t,rmoves)
        h=legal_moves(u)
        rmoves.append(h)
        am.remove(h)
        m=1
        mark(h,dis,m)
        print(dis)
        s=len(rmoves)
        print("--------------------------------------------------------------------------------------------------------------------------------------------------")
if dis[0][0]==dis[0][1]==dis[0][2]==0 or dis[1][0]==dis[1][1]==dis[1][2]==0 or dis[2][0]==dis[2][1]==dis[2][2]==0 or dis[0][0]==dis[1][0]==dis[2][0]==0 or dis[0][1]==dis[1][1]==dis[2][1]==0 or dis[0][2]==dis[1][2]==dis[2][2]==0 or dis[0][0]==dis[1][1]==dis[2][2]==0 or dis[0][2]==dis[1][1]==dis[2][0]==0:
       print(n1, "CONGRATULATIONS YOU WIN")
       print(n2,"BETTER LUCK NEXT TIME")
elif dis[0][0]==dis[0][1]==dis[0][2]==1 or dis[1][0]==dis[1][1]==dis[1][2]==1 or dis[2][0]==dis[2][1]==dis[2][2]==1 or dis[0][0]==dis[1][0]==dis[2][0]==1 or dis[0][1]==dis[1][1]==dis[2][1]==1 or dis[0][2]==dis[1][2]==dis[2][2]==1 or dis[0][0]==dis[1][1]==dis[2][2]==1 or dis[0][2]==dis[1][1]==dis[2][0]==1:
    print(n2,"CONGRATULATION YOU WIN")
    print(n1,"BETTER LUCK NEXT TIME")
elif s==9:
    print("Match Draw")
    print("IT WAS A NICE MATCH!!!!",n1,"and",n2,"BETTER LUCK NEXT TIME")
print("IT IS A COMBINE EFFORT OF:-\n ABDUL HASEEB \n ZAKIR ULLAH YOUSAFZAI")
