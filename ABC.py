A = int(input('Digite o primeiro número: '))
B = int(input('Digite o segundo número: '))
C = int(input('Digite o terceiro número: '))

print('EXIBINDO EM ORDEM CRESCENTE')
if A < B < C:
    print(A, ' - ', B, ' - ', C)
elif A < C < B:
    print(A, ' - ', C, ' - ', B)
elif B < A < C:
    print(B, ' - ', A, ' - ', C)
elif B < C < A:
    print(B, ' - ', C, ' - ', A)
elif C < B < A:
    print (C, ' - ', B, ' - ', A)
