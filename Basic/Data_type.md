# 자료형
자료형은 쉽게 말하자면 자료의 형태 또는 자료의 종류이다.   
다양한 종류의 자료들에 변수 이름을 붙여 사용한다.   

---

## 1. int (integer)
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

---

## 6. tuple

---

## 7. dictionary

---

## 8. set

---

## 9. function

---

## 10. range

---

## 11. type

---

## 12. __main__

---
