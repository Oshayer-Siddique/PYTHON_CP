print("you cant only 2 gates 0 and H(adamard) and N(Not)")

print("You can give upto 4 input")


n = int(input())
gate = list(map(str,input().strip().split()))[:n]

if gate[0] == '0' and gate[1] == 'H':
    a = '50 % '
    b = '50 %'
if gate[0] == '0' and gate[1] == 'H' and gate[2] == 'H':
    a = '100 %'
    b = '0 %'

if gate[0] == '0' and gate[1] == 'H' and gate[2] == 'H '  and gate[3] == 'H':
    a = '50 %'
    b = '50 %'

if gate[0] == '0' and gate[1] == 'N':
    a = '0 %'
    b = '100 %'
if gate[0] == '0' and gate[1] == 'N' and gate[2] == 'H':
    a = '50 %'
    b = '50 %'
if gate[0] == '0' and gate[1] == 'H' and gate[2] == 'N':
    a = '50%'
    b = '50%'

if gate[0] == '0' and gate[1] == 'N'  and gate[2] == 'H' and gate[3] == 'H':
    a = '0 %'
    b = '100 %'
if gate[0] == '0' and gate[1] == 'H'  and gate[2] == 'N' and gate[3] == 'H':
    a = '100 %'
    b = '0 %'
if gate[0] == '0' and gate[1] == 'H'  and gate[2] == 'H' and gate[3] == 'N':
    a = '0 %'
    b = '100 %'





print("0 = ",a)
print("1 = ",b)