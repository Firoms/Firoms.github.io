# 자료형이란?

자료형은 쉽게 말해서 자료의 형태이다.   
다양한 자료들이 각각의 자료형으로 분류되면서 자료들을 보다 쉽게 파악하고 다룰 수 있다.   
파이썬은 다양한 자료형의 자료들로만 이루어졌다고 봐도 될 정도로 자료형은 중요하다.   
대표적인 파이썬의 자료형으로는 [int](#1-int-정수형), [float](<#2_float_실수형>), [str], [bool], [list], [tuple], [set], [dictionary], [function], [class](<##9. type>) 등이 있다.   
자료의 자료형은 파이썬 내장 함수인  type을 이용하여  확인해 볼 수 있다.   

---
## 1. int 정수형
int는 integer의 줄임말로 integer는 정수를 뜻하는 단어이다.   
따라서 정수들은 모두 int 자료형에 속한다.      
파이썬 내장 함수인 [type]을 이용하면 int 자료형인지 확인할 수 있다.   
보통 다양한 [연산]을 하는데 사용된다.   

---

## 2. float 실수형
float은 실수를 뜻하는 단어로 모든 실수형은 float 자료형에 속한다.   
정수도 실수에 포함되지만, 소수점이 붙은 경우에만 float 자료형이라고 생각해도 된다.   
예를 들어, 3은 int 자료형이지만 3.0은 float 자료형인 것이다.   
마찬가지로 파이썬 내장 함수인 [type]을 이용하면 float 자료형인지 확인 할 수 있다.   
int 자료형과 함께 다양한 [연산]을 하는데 사용된다.   

---


int는 integer의 줄임말로 integer는 정수를 뜻하는 단어이다.   
따라서 정수들을 모두 int형 또는 integer형이라 부른다.   

    >>> print(type(123))
    <class 'int'>

    >>> print(type(0))
    <class 'int'>

    >>> print(type(-321))
    <class 'int'>

---

## 2. float
int형의 정수들을 제외한 실수들은 모두 float형이라 부른다.   
쉽게 말해서 뒤에 소수점이 붙은 숫자들은 모두 float형이다.   
0.0, 1.0과 같이 정수에 소수점이 붙은 것 역시 float형으로 분류한다.

    >>> print(type(3.14))
    <class 'float'>

    >>> print(type(-1.23))
    <class 'float'>

    >>> print(type(0.0))
    <class 'float'>

---

## 3. str (string)
str은 string의 줄임말로 string은 문자열을 뜻하는 단어이다.    
영어, 한국어 모두 str형 또는 string형으로 부른다.   
단, 문자 그대로 써주는 것이 아니라 따옴표로 감싸주어야 한다.   
따옴표가 붙지 않은 문자들은 프로그램에서 변수로 인식하기 때문이다.   
    
    >>> print(type('Hi'))
    <class 'str'>

    >>> print(type("안녕하세요"))
    <class 'str'>

    >>> print(type(""))
    <class 'str'>

공백 역시 str형에 포함한다는 것을 확인할 수 있다.   
다만, 다음과 같은 오류상황은 조심하여야 한다.   

    # 오류 상황

    >>> print(type(Hi)) # 변수로 인식하여 오류가 나거나 다른 자료형으로 인식할 수 있다.   
    NameError: name 'Hi' is not defined

    >>> print(type('안녕하세요")) # 따옴표의 종류를 통일해야 한다.
    SyntaxError: EOL while scanning string literal

---

## 4. bool
bool형에는 True와 False 두가지만 존재한다.   
참과 거짓을 나타내는 것이 bool형이다.

    >>> print(type(True))
    <class 'bool'>

    >>> print(type(False))
    <class 'bool'>

---

## 5. list
list형은 여러 자료형을 묶어놓은 듯한 형태의 자료형이다.   
[] 안에 , 를 간격으로 다양한 자료들을 넣어줄 수 있다.   
list 안에 list 역시 넣어줄 수 있다는 점이 특징이다.   

    >>> print(type([1, 2, 3]))
    <class 'list'>

    >>> print(type(['a','b', ['c', 'd', 'e']]))
    <class 'list'>

---

## 6.tuple
tuple형은 list형처럼 여러 자료형을 묶어놓은 듯한 형태의 자료형이다.   
() 안에 , 를 간격으로 다양한 자료들을 넣어줄 수 있다.   
tuple 안에 tuple 역시 넣어줄 수 있다.  
그러나 list형과는 달리, tuple형의 값을 바꿀 수 없다.   
언뜻 보기에는 값이 바뀔때도 있는 것 같아 혼동된다.   
하지만 tuple이 변하면, tuple의 id 값이 함께 변한다.
즉, tuple의 값이 변한 것이 아니라 새로운 tuple 자료가 생성된 것이다.

    >>> print(type((1, 2, 3)))
    <class 'tuple'>

    >>> print(type(('a', 'b', ('c', 'd', 'e'))))
    <class 'tuple'>


---

## 7. dict (dictionary)
dictionary형은 key에 따른 value 값을 가지는 형태의 자료형이다.   
쉽게 말해서 두 값을 쌍으로 저장하는 리스트이다.   
{} 안에 , 를 간격으로 key:value 형태로 다양한 자료들을 넣어줄 수 있다.   
다만 key 값은 중복될 수 없고 value 값만 중복될 수 있다.   
따라서 key 값만 있으면 value 값을 가져올 수 있는 것이 장점이다.   
처음에는 필요성을 못 느낄 수도 있지만, 나중에 정말 유용한 자료형이다.     

    >>> print(type({1:'A', 2:'B', 3:'C'}))
    <class 'dict'>

    >>> print(type({1:1, 2:1, 3:1}))
    <class 'dict'>


---

## 8. function

---

## 9. type

---

## 10. 그 외(range, set, __main__ 등)

---
data type
