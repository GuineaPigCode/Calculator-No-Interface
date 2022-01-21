start = ('Start Shit')

print('{:=^30}'.format(start))

text1s = ('Soma')
text2m = ('Multiplicação')
text3d = ('Divição')

text4di = ('Divição Inteira')
text5e = ('Potência')


n1 = int(input('Add with what number\n > '))
n2 = int(input('Add with the main number\n > '))

s = n1 + n2
m = n1 * n2
d = n1 / n2

di = n1 // n2
e = n1 ** n2

print('\n{:=^20}'.format(text1s))
print('Soma Ao Total De {}\n'.format(s))

print('{:=^20}'.format(text2m))
print('Multiplicação Ao Total De {}\n'.format(m))

print('{:=^20}'.format(text3d))
print('Divição Ao Total De {}\n'.format(d))

print('{:=^20}'.format(text4di))
print('Divição Inteira Ao Total De {}\n'.format(di))

print('{:=^20}'.format(text5e))
print('Potência Ao Total De {}\n'.format(e))
