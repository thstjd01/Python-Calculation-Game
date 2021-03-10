import turtle as t
import time
import random as rd

def lineimg():
    t.penup() #오른쪽 모래
    t.color('#FFE08C')
    t.goto(55,220)
    t.begin_fill()
    t.goto(350,220)
    t.goto(350,-350)
    t.goto(55,220)
    t.end_fill()
    
    t.color('black') #오른쪽 2번째 줄
    t.pendown()
    t.begin_fill()
    t.goto(60,220)
    t.goto(350,-350)
    t.goto(345,-350)
    t.goto(55,220)
    t.end_fill()

    t.penup()#왼쪽 모래
    t.goto(-350,220)
    t.color('#FFE08C')
    t.pendown()
    t.begin_fill()
    t.goto(-350,-350)
    t.goto(-55,220)
    t.goto(-350,220)
    t.end_fill()
    
    t.color('black') #왼쪽 2번째 줄
    t.penup()
    t.goto(-55,220)
    t.pendown()
    t.begin_fill()
    t.goto(-60,220)
    t.goto(-350,-350)
    t.goto(-345,-350)
    t.goto(-55,220)
    t.end_fill()

    t.penup() #오른쪽 1번째 줄
    t.goto(25,220)
    t.pendown()
    t.begin_fill()
    t.goto(130,-350)
    t.goto(125,-350)
    t.goto(20,220)
    t.goto(25,220)
    t.end_fill()

    t.penup() #왼쪽 1번째 줄
    t.goto(-25,220)
    t.pendown()
    t.begin_fill()
    t.goto(-130,-350)
    t.goto(-125,-350)
    t.goto(-20,220)
    t.goto(-25,220)
    t.end_fill()

    t.penup() #끝 선
    t.goto(55,220)
    t.pendown()
    t.goto(-55,220)

    t.penup()

def endlineimg():
    t.penup() #오른쪽 막대
    t.goto(80,220)
    t.begin_fill()
    t.goto(80,250)
    t.goto(75,250)
    t.goto(75,220)
    t.goto(80,220)
    t.end_fill()

    t.goto(-80,220) #왼쪽 막대
    t.begin_fill()
    t.goto(-80,250)
    t.goto(-75,250)
    t.goto(-75,220)
    t.goto(-80,220)
    t.end_fill()

    t.color('red') #빨강 깃발
    t.penup()
    t.goto(-80,250)
    t.pendown()
    t.begin_fill()
    t.goto(-80,280)
    t.goto(80,280)
    t.goto(80,250)
    t.goto(-80,250)
    t.end_fill()

def treeimg():
    t.penup() #아래 오른쪽 나무
    t.color('brown')
    t.goto(270,-200)
    t.pendown()
    t.begin_fill()
    t.goto(270,-30)
    t.goto(230,50)
    t.goto(230,-120)
    t.goto(270,-200)
    t.end_fill()

    t.penup()
    t.color('#86E57F')
    t.goto(220,150)
    t.pendown()
    t.begin_fill()
    t.goto(285,40)
    t.goto(285,-80)
    t.goto(220,60)
    t.goto(220,150)
    t.end_fill()

    t.penup() #아래 왼쪽 나무
    t.color('brown')
    t.goto(-270,-200)
    t.pendown()
    t.begin_fill()
    t.goto(-270,-30)
    t.goto(-230,50)
    t.goto(-230,-120)
    t.goto(-270,-200)
    t.end_fill()

    t.penup()
    t.color('#86E57F')
    t.goto(-220,150)
    t.pendown()
    t.begin_fill()
    t.goto(-285,40)
    t.goto(-285,-80)
    t.goto(-220,60)
    t.goto(-220,150)
    t.end_fill()

    t.penup() #위 오른쪽 나무
    t.color('brown')
    t.goto(145,170)
    t.pendown()
    t.begin_fill()
    t.goto(145,45)
    t.goto(110,115)
    t.goto(110,230)
    t.goto(145,170)
    t.end_fill()

    t.penup()
    t.color('#86E57F')
    t.goto(110,230)
    t.pendown()
    t.begin_fill()
    t.goto(110,310)
    t.goto(145,265)
    t.goto(145,170)
    t.goto(110,230)
    t.end_fill()
    
    t.penup() #위 왼쪽 나무
    t.color('brown')
    t.goto(-145,170)
    t.pendown()
    t.begin_fill()
    t.goto(-145,45)
    t.goto(-110,115)
    t.goto(-110,230)
    t.goto(-145,170)
    t.end_fill()

    t.penup()
    t.color('#86E57F')
    t.goto(-110,230)
    t.pendown()
    t.begin_fill()
    t.goto(-110,310)
    t.goto(-145,265)
    t.goto(-145,170)
    t.goto(-110,230)
    t.end_fill()

def bgimg():
    t.penup() #산
    t.goto(-350,220)
    t.pendown()
    t.color('#009300')
    t.begin_fill()
    t.goto(0,330)
    t.goto(350,220)
    t.goto(-350,220)
    t.end_fill()

    t.penup() #하늘
    t.goto(-350,350)
    t.pendown()
    t.color('#7ED2FF')
    t.begin_fill()
    t.goto(350,350)
    t.goto(350,220)
    t.goto(0,330)
    t.goto(-350,220)
    t.goto(-350,350)
    t.end_fill()

def mine():
    t.penup() #1번째 줄 
    t.goto(105,-225)
    t.pendown()
    t.color('#6B66FF')
    t.begin_fill()
    t.goto(-105,-225)
    t.goto(-100,-195)
    t.goto(100,-195)
    t.goto(105,-225)
    t.end_fill()

    t.penup() #3번째 줄
    t.goto(75,-55)
    t.pendown()
    t.color('#6B66FF')
    t.begin_fill()
    t.goto(-75,-55)
    t.goto(-70,-25)
    t.goto(70,-25)
    t.goto(75,-55)
    t.end_fill()

    t.penup() #5번째 줄
    t.goto(45,125)
    t.pendown()
    t.color('#6B66FF')
    t.begin_fill()
    t.goto(-45,125)
    t.goto(-38,155)
    t.goto(38,155)
    t.goto(45,125)
    t.end_fill()

    t.penup() #2번째 줄 왼쪽
    t.goto(-230,-120)
    t.pendown()
    t.color('#6B66FF')
    t.begin_fill()
    t.goto(-85,-120)
    t.goto(-80,-90)
    t.goto(-215,-90)
    t.goto(-230,-120)
    t.end_fill()

    t.penup() #2번째 줄 오른쪽
    t.goto(230,-120)
    t.pendown()
    t.color('#6B66FF')
    t.begin_fill()
    t.goto(85,-120)
    t.goto(80,-90)
    t.goto(215,-90)
    t.goto(230,-120)
    t.end_fill()

    t.penup() #4번째 줄 오른쪽
    t.goto(145,45)
    t.pendown()
    t.color('#6B66FF')
    t.begin_fill()
    t.goto(55,45)
    t.goto(50,75)
    t.goto(130,75)
    t.goto(145,45)
    t.end_fill()

    t.penup() #4번째 줄 왼쪽
    t.goto(-145,45)
    t.pendown()
    t.color('#6B66FF')
    t.begin_fill()
    t.goto(-55,45)
    t.goto(-50,75)
    t.goto(-130,75)
    t.goto(-145,45)
    t.end_fill()
    

t.setup(width=700,height=700) #창 크기

t.speed(0) #이미지 표시
bgimg()
lineimg()
endlineimg()
treeimg()
mine()
t.bgcolor('#F6F6F6')

t.shape("turtle") #플레이어 설정
t.setheading(90)
t.color('#D1B2FF')
t.speed(5)

t.penup()
t.goto(0,-320) #처음 거북이 위치
t.pendown()

while (True): #초기 단계
    u=input('거북이 계산 게임을 시작 하시겠습니까?(yes or no):')
    if u=='yes' or u=='no':
        break
    
if u=='yes': #준비 단계
    print()
    print('★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★')
    print('설명:1.파이썬 쉘에 W(앞) S(뒤) A(왼쪽) D(오른쪽) 입력')
    print('     2.플레이어는 보라색 거북이 입니다.')
    print('     3.타일에 닿으면 문제가 나옵니다.')
    print('     4.문제를 맞추거나 빨리 완주 할수록 점수가 오릅니다.')
    print('<TIP> 중간에 있는 타일은 20점, 양쪽에 있는 타일은 50점 입니다.')
    print('     5.빨간색 깃발 까지 완주하면 됩니다.')
    print('     6.게임 중간에 break을 입력하면 종료합니다.')
    print('     7.높은 점수를 받기 위해 노력하세요!')
    print('★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★')
    print()
    while (True):
        ok=input('준비되셨습니까?(yes):')
        if ok=='yes':
            print('5초 뒤에 시작합니다!')
            print()
            break
elif u=='no':
    print()
    print('게임을 종료합니다')

score=0
tlist=[0,0,0,0,0,0,0]
p=0

if u=='yes': #시작 단계
    time.sleep(1)
    print('5!')
    time.sleep(1)
    print('4!')
    time.sleep(1)
    print('3!')
    time.sleep(1)
    print('2!')
    time.sleep(1)
    print('1!')
    time.sleep(1)
    print('출발!')
    print()
    start_time=time.time()
    while (True):
        user=input('') #방향키
        if user=='a':
            t.penup()
            t.setheading(180)
            t.forward(30)
            t.setheading(90)
        if user=='d':
            t.penup()
            t.setheading(0)
            t.forward(30)
            t.setheading(90)          
        if user=='w':
            t.penup()
            t.forward(30)
        if user=='s':
            t.penup()
            t.setheading(270)
            t.forward(30)
            t.setheading(90)
            
        if (240>=t.ycor()>=220)and(-65<=t.xcor()<=65): #빨간 깃발
            end_time=time.time()
            gap=end_time-start_time
            print()
            print('당신은 {0}문제를 맞추었고, {1:6.4f}초에 들어왔습니다!'.format(p,gap))
            gap=int(gap)
            score+=(100-gap)
            print()
            print('완주! 축하합니다. 점수={}'.format(score))
            print()
            time.sleep(1)
            print('게임을 종료합니다.')
            break

        if (tlist[0]==0) and ((-195>=t.ycor()>=-225)and(-105<=t.xcor()<=105)): #1번째 줄
            tlist[0]=1
            a=rd.randint(1,10)
            b=rd.randint(1,10)
            print(a,'x',b,'= ?')
            ans=int(input())
            if a*b==ans:
                print()
                print('정답입니다!')
                print()
                p+=1
                score+=20
            else:
                print()
                print('틀렸습니다ㅠㅠ 정답은:',a*b)
                print()

        if (tlist[1]==0) and ((-25>=t.ycor()>=-55)and(-75<=t.xcor()<=75)): #3번째 줄
            tlist[1]=1
            a=rd.randint(1,100)
            b=rd.randint(1,100)
            print(a,'+',b,'= ?')
            ans=int(input())
            if a+b==ans:
                print()
                print('정답입니다!')
                print()
                p+=1
                score+=20
            else:
                print()
                print('틀렸습니다ㅠㅠ 정답은:',a+b)
                print()

        if (tlist[2]==0) and ((155>=t.ycor()>=125)and(-45<=t.xcor()<=45)): #5번째 줄
            tlist[2]=1
            a=rd.randint(1,10)
            b=rd.randint(1,10)
            print(a,'x',b,'= ?')
            ans=int(input())
            if a*b==ans:
                print()
                print('정답입니다!')
                print()
                p+=1
                score+=20
            else:
                print()
                print('틀렸습니다ㅠㅠ 정답은:',a*b)
                print()

        if (tlist[3]==0) and ((-90>=t.ycor()>=-120)and(-230<=t.xcor()<=-80)): #2번째 왼쪽
            tlist[3]=1
            a=rd.randint(1,100)
            b=rd.randint(1,100)
            print(a,'+',b,'= ?')
            ans=int(input())
            if a+b==ans:
                print()
                print('정답입니다!')
                print()
                p+=1
                score+=50
            else:
                print()
                print('틀렸습니다ㅠㅠ 정답은:',a+b)
                print()

        if (tlist[4]==0) and ((-90>=t.ycor()>=-120)and(80<=t.xcor()<=230)): #2번째 오른쪽
            tlist[4]=1
            a=rd.randint(1,10)
            b=rd.randint(1,10)
            print(a,'x',b,'= ?')
            ans=int(input())
            if a*b==ans:
                print()
                print('정답입니다!')
                print()
                p+=1
                score+=50
            else:
                print()
                print('틀렸습니다ㅠㅠ 정답은:',a*b)
                print()

        if (tlist[5]==0) and ((75>=t.ycor()>=45)and(-145<=t.xcor()<=-50)): #4번째 왼쪽
            tlist[5]=1
            a=rd.randint(1,100)
            b=rd.randint(1,100)
            print(a,'+',b,'= ?')
            ans=int(input())
            if a+b==ans:
                print()
                print('정답입니다!')
                print()
                p+=1
                score+=50
            else:
                print()
                print('틀렸습니다ㅠㅠ 정답은:',a+b)
                print()
                
        if (tlist[6]==0) and ((75>=t.ycor()>=45)and(50<=t.xcor()<=145)): #4번째 오른쪽
            tlist[6]=1
            a=rd.randint(1,10)
            b=rd.randint(1,10)
            print(a,'x',b,'= ?')
            ans=int(input())
            if a*b==ans:
                print()
                print('정답입니다!')
                print()
                p+=1
                score+=50
            else:
                print()
                print('틀렸습니다ㅠㅠ 정답은:',a*b)
                print()

        if user=='break': #종료
            print()
            print('게임을 종료합니다.')
            break

t.done()
