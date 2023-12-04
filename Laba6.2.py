def my_split(str):
    a = []
    b = ""
    for x in str:
        if x == " ":
            if b != "":
                a.append(b)
            b = ""
        else:
            b += x
    if b != "":
        a.append(b)
    return a
s= input('Введите строку: ')
s0=input('Введите строку: ')
S=my_split(s)
S_0=my_split(s0)
st = 0

def remove_substring(S, S_0):
    if S_0 in S == -1:
        return S
    result = ""
    index = 0

    while index < len(S):
        if S[index:index + len(S_0)] == S_0:
            index += len(S_0)
        else:
            result += S[index] + ' '
            index += 1
    return result

result = remove_substring(S, S_0)
print(result)






















