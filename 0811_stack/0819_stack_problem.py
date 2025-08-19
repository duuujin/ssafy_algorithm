T = int(input())
for test_case in range(1,T+1):
    moon = input()

    def check_match(moon):
        stack = []
        matching_dict = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        for char in moon:
            if char in matching_dict.values():
                stack.append(char)
            elif char in matching_dict.keys():
                if not stack:
                    return False
                if stack[-1] != matching_dict[char]:
                    return False
                stack.pop()
        if stack:
            return False
        return True


    if check_match(moon):
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')


