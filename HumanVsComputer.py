###HUMAN VERES COMPUTER
##SIR I AM FACING THAT ERROR SOME TIME(UnboundLocalError: local variable 'm1' referenced before assignment)


#ABDUL HASEEB 1801009


#ZAKIR ULLAH 1801027


from numpy import*
def hc(list,av):
    if list[0][1]==list[0][2]==0 or list[2][0]==list[1][0]==0 or list[1][1]==list[2][2]==0:
        if 1 in av:
            m1=1

    elif list[0][0]==list[0][1]==0 or list[2][1]==list[1][1]==0:
       if 2 in av:
             m1=2

    elif list[0][0]==list[0][1]==0 or list[2][0]==list[1][1]==0 or list[2][2]==list[1][2]==0:
       if 3 in av:
           m1=3
    elif list[2][0]==list[0][0]==0 or list[1][1]==list[1][2]==0:
       if 4 in av:
           m1=4

    elif list[0][2]==list[2][0]==0 or list[2][2]==list[0][0]==0 or list[2][1]==list[0][1]==0 or list[1][2]==list[1][0]==0:
        if 5 in av:
            m1=5
    elif list[0][2]==list[2][2]==0 or list[1][0]==list[1][1]==0:
      if 6 in av:
          m1=6
    elif list[0][0]==list[1][0]==0 or list[1][1]==list[0][2]==0 or list[2][1]==list[2][2]==0:
      if 7 in av:
          m1=7
    elif list[0][1]==list[1][1]==0 or list[2][0]==list[2][2]==0:
        if 8 in av:
            m1=8
 
    elif list[0][2]==list[1][2]==0 or list[0][0]==list[1][1]==0 or list[2][0]==list[2][1]==0:
        if 9 in av:
            m1=9
    else:
        if list[0][1]==list[0][2]==1 or list[2][0]==list[1][0]==1 or list[1][1]==list[2][2]==1:
           if 1 in av:
               m1=1
        elif list[0][0]==list[0][1]==1 or list[2][1]==list[1][1]==1:
            if 2 in av:
               m1=2
        elif list[0][0]==list[0][1]==1 or list[2][0]==list[1][1]==1 or list[2][2]==list[1][2]==1:
            if 3 in av:
               m1=3
        elif list[2][0]==list[0][0]==1 or list[1][1]==list[1][2]==1:
            if 4 in av:
               m1=4
        elif list[0][2]==list[2][0]==1 or list[2][2]==list[0][0]==1 or list[2][1]==list[0][1]==1 or list[1][2]==list[1][0]==1:
              if 5 in av:
                 m1=5
        elif list[0][2]==list[2][2]==1 or list[1][0]==list[1][1]==1:
             if 6 in av:
                m1=6
        elif list[0][0]==list[1][0]==1 or list[1][1]==list[0][2]==1 or list[2][1]==list[2][2]==1:
           if 7 in av:
                m1=7
        elif list[0][1]==list[1][1]==1 or list[2][0]==list[2][2]==1:
            if 8 in av:
               m1=8
        elif list[0][2]==list[1][2]==1 or list[0][0]==list[1][1]==1 or list[2][0]==list[2][1]==1:
             if 9 in av:
                m1=9
        elif True:
             m1=max(av)
        else:
             if 5 in av:
                 m1=5

    return m1
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
dis1=array([[1,2,3],[4,5,6],[7,8,9]])
print(dis1)
print("HUMAN!!! I AM GIVING YOU FIRST TURN")
av=[1,2,3,4,5,6,7,8,9]
rmove=[]
n1=(str(input("BY THE WAY HUMAN WHAT IS YOUR NAME!!")))
s=len(rmove)
while s!=9:
     if dis1[0][0]==dis1[0][1]==dis1[0][2] or dis1[1][0]==dis1[1][1]==dis1[1][2] or dis1[2][0]==dis1[2][1]==dis1[2][2] or dis1[0][0]==dis1[1][0]==dis1[2][0] or dis1[0][1]==dis1[1][1]==dis1[2][1] or dis1[0][2]==dis1[1][2]==dis1[2][2] or dis1[0][0]==dis1[1][1]==dis1[2][2] or dis1[0][2]==dis1[1][1]==dis1[2][0] or s==9:
                    break
     else:
         print("                                 ",n1,"IS PLAYING!!!!.....                                                                  ")
         print("avialiable moves are :",av)
         y1=int(input("WHERE YOU WANT TO MARK???"))
         o1=illegal_moves(y1,rmove)
         g1=legal_moves(o1)
         rmove.append(g1)
         av.remove(g1)
         m=0
         mark(g1,dis1,m)
         print(dis1)
         s=len(rmove)
         print("............................................................................................................................")

     if dis1[0][0]==dis1[0][1]==dis1[0][2] or dis1[1][0]==dis1[1][1]==dis1[1][2] or dis1[2][0]==dis1[2][1]==dis1[2][2] or dis1[0][0]==dis1[1][0]==dis1[2][0] or dis1[0][1]==dis1[1][1]==dis1[2][1] or dis1[0][2]==dis1[1][2]==dis1[2][2] or dis1[0][0]==dis1[1][1]==dis1[2][2] or dis1[0][2]==dis1[1][1]==dis1[2][0] or s==9:
                    break
     else:
          print("________________________________________________ MY TURN_____________________________________________________________________________")
          q=hc(dis1,av)
          
          print(q)
          rmove.append(q)
          av.remove(q)
          m=1
          mark(q,dis1,m)
          print(dis1)
          s=len(rmove)
          print("...............................................................................................................................")
          
if dis1[0][0]==dis1[0][1]==dis1[0][2]==0 or dis1[1][0]==dis1[1][1]==dis1[1][2]==0 or dis1[2][0]==dis1[2][1]==dis1[2][2]==0 or dis1[0][0]==dis1[1][0]==dis1[2][0]==0 or dis1[0][1]==dis1[1][1]==dis1[2][1]==0 or dis1[0][2]==dis1[1][2]==dis1[2][2]==0 or dis1[0][0]==dis1[1][1]==dis1[2][2]==0 or dis1[0][2]==dis1[1][1]==dis1[2][0]==0:
       print(n1, "CONGRATULATIONS YOU WIN")
       print("computer","BETTER LUCK NEXT TIME")
elif dis1[0][0]==dis1[0][1]==dis1[0][2]==1 or dis1[1][0]==dis1[1][1]==dis1[1][2]==1 or dis1[2][0]==dis1[2][1]==dis1[2][2]==1 or dis1[0][0]==dis1[1][0]==dis1[2][0]==1 or dis1[0][1]==dis1[1][1]==dis1[2][1]==1 or dis1[0][2]==dis1[1][2]==dis1[2][2]==1 or dis1[0][0]==dis1[1][1]==dis1[2][2]==1 or dis1[0][2]==dis1[1][1]==dis1[2][0]==1:
    print("computer","CONGRATULATION YOU WIN")
    print(n1,"BETTER LUCK NEXT TIME")
elif s==9:
    print("Match Draw")
    print("IT WAS A NICE MATCH!!!!",n1,"and BETTER LUCK NEXT TIME")
print("IT IS A COMBINE EFFORT OF:-\n ABDUL HASEEB \n ZAKIR ULLAH YOUSAFZAI")

          
          


    
