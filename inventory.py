L=[]
D=[30, 15, 25, 15, 45, 30, 25, 15, 20, 35, 20, 30]
O=[]
d=0
i=0
s=20
S=60

L.append(S)




while i<len(D):
  i+=1
  if L[i-1]<s:
    O.append(S-L[i-1])
  else :
    O.append(0)
  d=D[i-1]
  L.append(L[i-1] + O[i-1] - d)
  
  


n=i
O.append(S-L[n])
L.append(S)


print(len(O))
print("O",O)
print("L",L)
print("D",D)

print(n)
#Average demand

demand=0
for x in range(0,len(D)):
  demand+=D[x]

print(demand)

#average order
demand2=0
for y in range(0,len(O)):
  demand2+=O[y]
print(demand2)
  
Demand_Average=demand/n
order_Average=demand2/n

print(Demand_Average,order_Average)
