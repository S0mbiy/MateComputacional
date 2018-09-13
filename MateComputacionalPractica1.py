
# coding: utf-8

# In[37]:


def automataIdentificador(entrada):
    lamda="acdfghjklmnoqrsuwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    abc="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sigma="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
    num="0123456789"
    
    estado=0
    limite=len(entrada)
    for i in range(limite):
        letra=entrada[i]
        if(estado==0):
            if(letra in lamda):
                estado=1
            elif(letra == "v"):
                estado=2
            elif(letra == "p"):
                estado=3
            elif(letra == "b"):
                estado=4
            elif(letra == "e"):
                estado=5
            elif(letra == "t"):
                estado=6
            elif(letra == "i"):
                estado=7
            elif(letra == "_"):
                estado=8
            else:
                estado=9
        elif (estado==1):
            if(letra not in sigma):
                estado=9
        elif (estado==2):
            if(letra=="a"):
                estado=10
            elif(letra not in sigma):
                estado=9
            else:
                estado=1
        elif (estado==3):
            if(letra=="r"):
                estado=11
            elif(letra not in sigma):
                estado=9
            else:
                estado=1
        elif (estado==4):
            if(letra=="e"):
                estado=12
            elif(letra not in sigma):
                estado=9
            else:
                estado=1
        elif (estado==5):
            if(letra=="n"):
                estado=13
            elif(letra=="l"):
                estado=14
            elif(letra not in sigma):
                estado=9
            else:
                estado=1
        elif (estado==6):
            if(letra=="h"):
                estado=15
            elif(letra not in sigma):
                estado=9
            else:
                estado=1
        elif (estado==7):
            if(letra=="f"):
                estado=16
            elif(letra not in sigma):
                estado=9
            else:
                estado=1
        elif (estado==8):
            if(letra in abc):
                estado=1
            elif(letra not in sigma):
                estado=9
        elif (estado==9):
            estado=9
        elif (estado==10):
            if(letra=="r"):
                estado=16
            elif(letra not in sigma):
                estado=9
            else:
                estado=1
        elif (estado==11):
            if(letra =="o"):
                estado=17
            elif(letra not in sigma):
                estado=9
            else:
                estado=1
        elif (estado==12):
            if(letra =="g"):
                estado=18
            elif(letra not in sigma):
                estado=9
            else:
                estado=1
        elif (estado==13):
            if(letra =="d"):
                estado=16
            elif(letra not in sigma):
                estado=9
            else:
                estado=1
        elif (estado==14):
            if(letra =="s"):
                estado=19
            elif(letra not in sigma):
                estado=9
            else:
                estado=1
        elif (estado==15):
            if(letra =="e"):
                estado=20
            elif(letra not in sigma):
                estado=9
            else:
                estado=1
        elif (estado==16):
            if(letra in sigma):
                estado=1
            else:
                estado=9
        elif (estado==17):
            if(letra =="g"):
                estado=21
            elif(letra not in sigma):
                estado=9
            else:
                estado=1
        elif (estado==18):
            if(letra =="i"):
                estado=22
            elif(letra not in sigma):
                estado=9
            else:
                estado=1
        elif (estado==19):
            if(letra =="e"):
                estado=16
            elif(letra not in sigma):
                estado=9
            else:
                estado=1
        elif (estado==20):
            if(letra =="n"):
                estado=16
            elif(letra not in sigma):
                estado=9
            else:
                estado=1
        elif (estado==21):
            if(letra =="r"):
                estado=23
            elif(letra not in sigma):
                estado=9
            else:
                estado=1
        elif (estado==22):
            if(letra =="n"):
                estado=16
            elif(letra not in sigma):
                estado=9
            else:
                estado=1
        elif (estado==23):
            if(letra =="a"):
                estado=24
            elif(letra not in sigma):
                estado=9
            else:
                estado=1
        elif (estado==24):
            if(letra =="m"):
                estado=16
            elif(letra not in sigma):
                estado=9
            else:
                estado=1
    return estado in [1,2,3,4,5,6,7,10,11,12,13,14,15,17,18,19,20,21,22,23,24]
    
print(automataIdentificador("_A"))      


# In[111]:


def automataNum(entrada):
    num="0123456789"
    
    estado=0
    limite=len(entrada)
    for i in range(limite):
        letra=entrada[i]
        if(estado==0):
            if(letra in "123456789"):
                estado=1
            elif(letra=="0"):
                estado=2
            else:
                estado=3
        elif(estado==1):
            if(letra=="."):
                estado=6
            elif(letra not in num):
                estado=3
        elif(estado==2):
            if(letra in "01234567"):#probar con 0
                estado=5
            elif(letra=="."):
                estado=6
            elif(letra=="x"or letra=="X"):
                estado=4
            else:
                estado=3
        elif(estado==3):
            estado=3
        elif(estado==4):
            if(letra not in "0123456789abcdefABCDEF"):
                estado=3
        elif(estado==5):
            if(letra=="."):
                estado=6
            elif(letra not in "01234567"):
                estado=3
        elif(estado==6):
            if(letra in num):
                estado=10
            elif(letra not in num):
                estado=3
        elif(estado==7):
            if(letra in num):
                estado=9
            elif(letra=="+"or letra=="-"):
                estado=8
            else:
                estado=3
        elif(estado==8):
            if(letra in num):
                estado=9
            else:
                estado=3
        elif(estado==9):
            if(letra not in num):
                estado =3
        elif(estado==10):
            if(letra=="e"or letra=="E"):
                estado=7
            elif(letra not in num):
                estado=3
    if(estado in [1]):
        return ["Natural",True]
    elif(estado in [2,5]):
        return ["Octal",True]
    elif(estado in [4]):
        return ["Hexadecimal",True]
    elif(estado in [9,10]):
        return ["Punto flotante",True]
    else:
        return ["Error",False]
print(automataNum("1E"))
        
            


# In[107]:


def prueba(entrada):
    ans=automataIdentificador(entrada)
    if(ans):
        return ["Identificador",True]
    ans=automataNum(entrada)
    if(ans[1]):
        return ans
    else:
        return ["Error",False]
print(prueba("01234.1"))        

