T = int(input())
for tset_case in range(1,T+1):
    tc, strlen = map(str,input().split())
    str_list = list(map(str,input().split()))
    
    num_list = []
    for i in str_list:
        if i == "ZRO":
            num_list.append(0)
        elif i == "ONE":
            num_list.append(1)
        elif i == "TWO":
            num_list.append(2)
        elif i == "THR":
            num_list.append(3)
        elif i == "FOR":
            num_list.append(4)
        elif i == "FIV":
            num_list.append(5)
        elif i == "SIX":
            num_list.append(6)
        elif i == "SVN":
            num_list.append(7)
        elif i == "EGT":
            num_list.append(8)
        elif i == "NIN":
            num_list.append(9)
     
    numnum_list = sorted(num_list)
     
    result = []
    for i in numnum_list:
        if i == 0:
            result.append("ZRO")
        elif i == 1:
            result.append("ONE")
        elif i == 2:
            result.append("TWO")
        elif i == 3:
            result.append("THR")
        elif i == 4:
            result.append("FOR")
        elif i == 5:
            result.append("FIV")
        elif i == 6:
            result.append("SIX")
        elif i == 7:
            result.append("SVN")
        elif i == 8:
            result.append("EGT")
        elif i == 9:
            result.append("NIN")


    
    print(tc)
    print(" ".join(result))