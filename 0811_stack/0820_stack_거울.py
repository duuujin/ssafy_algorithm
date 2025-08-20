T = int(input())
for test_case in range(1,T+1):
    s = input()
    
    def mirror_str(s):
        mirror_dict = {
        'b' : 'd',
        'd' : 'b',
        'p' : 'q',
        'q' : 'p'
        }
        mirrored = ""
        for ch in s:
            mirrored += mirror_dict[ch]
        return mirrored[::-1]
    
    result = mirror_str(s)
    print(f'#{test_case} {result}')