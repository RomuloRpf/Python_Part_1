n=input("Digite um número inteiro: ")

t=0
igual=False
while t<(len(n)-1):
    i=n[t]
    j=n[t+1]
    if i==j:
        print("sim")
        igual=True
        break
    t+=1
if igual==False:
    print("não")
