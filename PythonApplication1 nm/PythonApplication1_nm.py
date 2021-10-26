from random import*
inimesed=["Anna","Tomm","Anna","Max"]
palgad=[1200,2000,1560,1200]

def sisesta_andmed(i,p):
    global N
    N=4
    for n in range(N):
        inimene=input("Nimi: ")
        i.append(inimene)
        palk=randint(100,10000)
        p.append(palk)
    return i,p

def andmed_ekranile(i,p):
    N=len(i)
    for n in range(N):
        print(i[n],"-",p[n])

def kustutamine(i,p): #удалить человека и его зарплату (вводим имя)
    nimi=input("Sisesta nimi, keda vaja kustutada:")
    n=i.count(nimi) #кол-во
    abi_list=[]
    if n>0:
        t=0
        for e in range(len(i)):
            if i[e]==nimi:
                t+=1
                abi_list.append(int(e)) #список индексов
                print(t, ". ", i[e],"-",p[e])
        j=int(input("Järjekordne number:"))
        i.pop(abi_list[j-1])
        p.pop(abi_list[j-1])
        andmed_ekranile(i,p)
    return i,p


def suurim_palk(i,p):
    suurim=max(p)
    #count() for abi_list p.index()->i.index() andmed_ekranile (abi_list)


def sorteerimine(i,p,v):
    N=len(p)
    if v==1:
        for n in range (0,N):
            for m in range (n,N):
                if p[n]<p[m]:
                    abi=p[n]
                    p[n]=p[m]
                    p[m]=abi
                    abi=i[n]
                    i[n]=i[m]
                    i[m]=abi
    else:
        for n in range (0,N):
            for m in range (n,N):
                if p[n]>p[m]:
                    abi=p[n]
                    p[n]=p[m]
                    p[m]=abi
                    abi=i[n]
                    i[n]=i[m]
                    i[m]=abi

    andmed_ekranile(i,p)

def vordsed_palgad(i,p):
    N=len(p)
    dublikatid=[x for x in palgad if palgad.count(x)>1 ]
    print(list(set(dublikatid)))
vordsed_palgad(inimesed,palgad)

    #abi_list=[]
    #for n in range (0,N):
    #    for m in range (n,N):
    #        if p[n]==p[m]:
    #            n=p.count(p[n])

   ???  elif valik=="nimi":
        ots_nimi,ots_palk=nimi(palk,inimesed)
        for i in range(len(ots_nimi)):
            print(ots_nimi[i]," saab kätte   ", ots_palk[i])

while 1:
    print("a-andmete sisestamine\ne-andmed ekranile\nk-kustutamine\nmax-kellel on suurim palk\ns-sort\nv-vordsed")
    valik=input()
    if valik.lower()=="a":
        inimesed,palgad=sisesta_andmed(inimesed,palgad)
    elif valik.lower()=="e":
        andmed_ekranile(inimesed,palgad)
    elif valik.lower()=="k":
        inimesed,palgad=kustutamine(inimesed,palgad)
    elif valik.lower()=="max":
        suurim_palk(inimesed,palgad)
    elif valik.lower()=="s":
        sorteerimine(inimesed,palgad,int(input("1-kahaneb, 2-kasvab")))
    elif valik.lower()=="v":
        vordsed_palgad(inimesed,palgad)
    elif valik.lower()=="v":

    else:
        break




inimesed,palgad=sisesta_andmed(inimesed,palgad)
andmed_ekranile(inimesed,palgad)



print(inimesed)
print(palgad)

