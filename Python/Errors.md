# NameError
1) NameError: name '<>' is not defined   

선언되지 않은 변수 명을 이용하려 할 때 발생하는 오류이다.   
때론, 따옴표를 빼먹어서 문자열을 변수로 인식하여 발생하기도 한다.   


# SyntaxError
1) SyntaxError: EOL while scanning string literal
        EOL은 End Of Life를 줄인 표현이라고 한다.   
        따라서, 문자열을 읽어들이는데 문법적 오류가 있어 발생한다.   
        보통 따옴표가 잘못 쓰였을 때 발생하곤 한다.   

2) SyntaxError: multiple statements found while compiling a single statement
        이 오류는 파이썬 쉘에서 한 번에 여러 문장을 실행했을 때 발생하는 오류이다.   
        프롬프트당 한 줄만 입력해야 한다.


# RecursionError
1) RecursionError: maximum recursion depth exceeded in comparison
        일정 횟수 이상의 재귀가 반복되면 일어나는 에러이다.   
        재귀 횟수를 조정하는 방법도 있다.   

# IndentationError
1) IndentationError: expected an indented block
        들여쓰기를 잘못했을 때 일어나는 에러이다.

# TypeError
1) TypeError : int() argument must be a string, a bytes-like object or a number, not <>
        자료를 int 자료형으로 바꾸려할 때 발생하는 오류로 int 자료형으로 변경 불가할 때 발생하는 에러이다.

2) TypeError: 'tuple' object does not support item <>
        튜플 값을 변경하려고 할 때 발생하는 오류로 일어나는 오류로 tuple은 immutable 한 자료형이다.
# ValueError
1) ValueError: invalid literal for int() with base 10: <>
        str 자료형 값을 int 자료형으로 변경하려고 할 때 주로 일어나는 오류이다.