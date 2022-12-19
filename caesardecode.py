str = 'afZ_r9VYfScOeO_UL^RWUc';

def acsiiAdd(ch, i):
    return chr(ord(ch)+i)


bias=5
for ch in str:
    print(acsiiAdd(ch, bias), end='')
    bias+=1
print()