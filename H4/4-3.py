bedrag=867
print('bedrag =',bedrag/100)
dollars=bedrag//100
print('dollars =',dollars)
bedrag=bedrag-dollars*100
kwartjes=bedrag//25
print('kwartjes =',kwartjes)
bedrag=bedrag-kwartjes*25
dubbeltjes=bedrag//10
print('dubbeltjes =',dubbeltjes)
bedrag=bedrag-dubbeltjes*10
stuivers=bedrag//5
print('stuivers =',stuivers)
bedrag=bedrag-stuivers*5
centen=bedrag
print('centen =',centen)