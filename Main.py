print("Suma de dos Numeros")
x=0
while x<1000:
    n1=int(raw_input("Intoduzca el valor del Primer sumero a sumar: "))
    n2=int(raw_input("Intoduzca el valor del Primer segundo a sumar: "))
    print("El Resultado es: "+str(n1+n2))
    rsp=raw_input("Quiere sumar de nuevo?  S/N :")
    if rsp=="n" or rsp=="N":
       break
