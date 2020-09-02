#PROGRAMA: IMPOSTO

#Entrada de dados
#variáveis de entrada: m,e,f
m=float(input("municipal:\n"))
e=float(input("estadual: \n"))
f=float(input("federal: \n"))

#Desenvolvimento
#variável auxiliar: t
t=m+e+f
pm=m/t*100
pe=e/t*100
pf=f/t*100

#Saída de dados
#variáveis de saída:pm,pe,pf
#f"pm={pm:.2f}"
#f -> método f-format de formatação.
# "pm="-> texto pm=
#{pm:.2f-> exibir o conteúdo da variável pm com duas casas decimais
#.2-> 2 casas decimais
#o segundo f-> indica que estamos com um número decimal
#"%"-> como % está dentro das aspas duplas ela aprece como caracter no texto
print(f"pm={pm:.2f}%")
print(f"pe={pe:.2f}%")
print(f"pf={pf:.2f}%")









