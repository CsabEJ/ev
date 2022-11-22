wr=open('H:\\ev.txt''a')
ev= [2984,2348,2069,2204,2418,2037,2092,2495,2487,2827,2305,2650]

#ev = False
#if len(ev) == 12:
    #ev = True
    #print(f'ez egy év adatsora')
#else:
    #print(f'ez nem egy év adatsora')
    
legnagyobb = ev[0]
legkisebb = ev[0]
for elem in ev:
    if elem > legnagyobb:
        legnagyobb = elem
print(f'{legnagyobb}')

for elem in ev:
    if elem < legkisebb:
        legkisebb = elem
print(f'{legkisebb}')
    
print(sum(ev))


h = 0

for x in ev:
    if x < 2400:
        h += 1
print(h)

hossz = len(ev)
ker = legnagyobb
y = 0
while ev[y] != ker:
    y += 1
print(f'legnagyobb helye: {y+1}')
    
hossz = len(ev)
ker = legkisebb
i = 0
while ev[i] != ker:
    i += 1
print(f'legkisebb helye: {i+1}')


wr.write(f'{legnagyobb}','\n')
wr.write(f'{legkisebb}','\n')
wr.write(f'{h}','\n')
wr.write(f'{y+1}','\n')
wr.write(print(sum(ev),'\n'))

wr.close

