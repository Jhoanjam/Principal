x=0
resul=0
while x<1000:
    n1=int(raw_input("Intoduzca el Primer valor : "))
    n2=int(raw_input("Intoduzca el segundo valor : "))
    tipo=raw_input("Que desea Hacer (+)(-)(*)(/) ")
    if tipo=="+":
       resul=n1+n2
    elif tipo=="-":
       resul=n1-n2   
    elif tipo=="*":
       resul=n1*n2
    elif tipo=="/":
       resul=n1/n2


    print("El Resultado es: "+str(resul))
    rsp=raw_input("Quieres Realizar Otra Operacion?  S/N :")
    
    if rsp=="n" or rsp=="N":
       break
