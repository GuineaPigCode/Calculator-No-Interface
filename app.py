start = ('Calculator No Interface')

print('{:=^30}'.format(start))

text1s = ('Sum')
text2m = ('Multiplication')
text3d = ('Division')

text4di = ('Integer Division')
text5e = ('Power')


n1 = int(input('Add with what number\n > '))
n2 = int(input('Add with the main number\n > '))

s = n1 + n2
m = n1 * n2
d = n1 / n2

di = n1 // n2
e = n1 ** n2

print('\n{:=^20}'.format(text1s))
print('Sum To The Total Of {}\n'.format(s))

print('{:=^20}'.format(text2m))
print('Multiplication To Total Of {}\n'.format(m))

print('{:=^20}'.format(text3d))
print('Division To Total Of {}\n'.format(d))

print('{:=^20}'.format(text4di))
print('Integer Division To Total Of {}\n'.format(di))

print('{:=^20}'.format(text5e))
print('Total Power Of {}\n'.format(e))
