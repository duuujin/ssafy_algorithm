# 괄호가 제대로 짝이 맞는 지 확인하는 함수
def check_match(expression):
    # stack -> 후입선출
    stack = [] # 빈 리스트로 초기화
    matching_dict = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }


    # 주어진 expression을 순회하면서, 괄호의 종류에 따라 push, pop를 진행하면서 비교
    for char in expression:
        # 여는 괄호가 나오면 바로 스택에 넣는다.
        if char in matching_dict.values():
            stack.append(char)
        # 닫힌 괄호가 나오면 스택에 pop 하고 같은 괄호인지 비교한다.
        elif char in matching_dict.keys():
            #스택에서 꺼낸다. 그리고 비교한다.
            if not stack :
                return False
            
            #비어있지 않으니까 꺼냄
            # 짝이 맞는지 확인
            # 현재 여기서 char는 닫힌 괄호 -> key값으로 넣으며ㅑㄴ 닫힌 괄호에 매칭되어야 하는 여는 괄호 나옴
            if stack[-1] != matching_dict[char]:
                return False
            
            # 스택이 비어있지도 않고 , 짝도 맞는 경우
            stack.pop()

    if stack: # 스택이 안 비었다? 그러면 열린 괄호가 짝이 없다는 소리.
        return False

    return True 




examples = ["(a(b)","a(b)c","a{b(c[d]e}f)"]
for ex in examples:
    if check_match(ex):
        print(f'{ex}는 올바른 괄호')
    else:
        print(f'{ex}는 올바르지 않은 괄호')