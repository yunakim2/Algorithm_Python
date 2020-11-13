# Algorithm_Python



### 1️⃣ python 문법 정리

> 입력

~~~python
# int형으로 input 받기
a = int(input())

# int형으로 한줄의 두개의 변수 저장하기
a,b = map(int,input().split())

# input() 보다 빠르게 입력받기
a,b = map(int,sys.stdin.readline().split())

# 한줄 변수 list 형으로 받기 
c = list(map(int,input().split())
~~~



> 출력

~~~python
# Hello
#	World 
# 출력하기  
print("Hello\nWorld")
~~~

~~~python
# 변수 a b 출력하기
print(a,b," ")
# 변수 a+b=(a+b) 출력하기
print(a,"+",b,"=",a+b)
print("%s+%s=%s"%(a,b,(a+b)))
# 1 2 3 4 출력하기 (뒤에 한칸 띄어스기 하려면 end = ' ')
for i in range(1,5) :
	print(i,end =' ')
~~~

~~~python
# 가로로 출력
print(~ , end='')
~~~

~~~python
# 여러항목 출력 --> ,로 구분시 문자,숫자 모두 일정 공백을 두고 출력
print('This is string :', var_char, 'This is number :' ,var_num,var_num2)

# 공백없이 이어져서 출력 --> +로 구분
print('This is string :' + var_char, 'This is number :', var_num+var_num2)

# 여러항목 출력2 
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))
 
num1=1;num2=2
print('{0} {1}'.format(num1,num2))

#출력(%s : 문자열, %d : 정수 , %f : 부동소수점)
print('Text %s'%var_char)
print('Number %d'%var_num)
print('This is text %s This is number %d'%(var_char,num1))
~~~



> if 문

~~~python
if a>b : print(">")
elif a==b : print("==")
else : print("<")
~~~



> for 문

~~~python
#1부터 9까지 실행
for b in range(1,10) :
  	실행문
    
#0부터 a-1까지 실행
for b in range(a) :
  실행문
  
# a부터 1까지 실행
for a in range(a,0,-1) :
  실행문
~~~

~~~python
# *
# **
# ***
# ****
# ***** 별찍기

for b in range(1,6) :
  print("*"*b)
  
#    *
#   **
#  ***
# ****
#***** 별찍기
for b in range(1,6) :
  print(" "*(5-b)+"*"*b)
~~~



> && ➡️ and , ||➡️ or



> while 문

~~~python
while 조건문 : 
  실행문 
  실행문
  
~~~



> try catch 문 

~~~python
try :
  실행문
except 발생오류 :
  ...
~~~



> 연산

~~~python
* 곱하기
/ 나누기 
// int 형 변환 나누기
% 나머지
+ 더하기
- 빼기
~~~



> list



> 문자열 메소드

[문자열 메소드 정리](https://github.com/yunakim2/Algorithm_Python/blob/master/%EB%AC%B8%EC%9E%90%EC%97%B4%20%EB%A9%94%EC%86%8C%EB%93%9C.md)



---

> 파이썬 스터디 정리

1️⃣ [1.코딩테스트 출제 경향 분석 및 파이썬 문법 부수기](https://github.com/yunakim2/Algorithm_Python/blob/master/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%8A%A4%ED%84%B0%EB%94%94/%EB%8F%99%EB%B9%88%EB%82%98_%EC%9D%B4%EC%BD%94%ED%85%8C_1%EA%B0%95.md)

2️⃣ [2. 그리디 & 구현 ](https://github.com/yunakim2/Algorithm_Python/blob/master/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%8A%A4%ED%84%B0%EB%94%94/%EB%8F%99%EB%B9%88%EB%82%98_%EC%9D%B4%EC%BD%94%ED%85%8C_2%EA%B0%95.md)

