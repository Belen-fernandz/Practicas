print("Bienvenido al programa..")

persona={"Nombre":"","Apellido":"","Edad":0,"Peso":0,"Altura":0,"Direccion":"","Telefono":""}

def cat_imc(imc):
    if imc < 18.5:
        print ("Está en un Bajo Peso")
    elif imc < 24.9:
        print ("Está en un Peso Normal")
    elif imc < 29.9:
        print ("Está en Sobre Peso")
    elif imc < 34.9:
        print ("Tiene Obesidad tipo I")
    elif imc < 39.9:
        print ("Tiene Obesidad tipo II")
    elif imc > 40:
        print ("Tiene Obesidad tipo III")

def imprimir(persona):
    for item in persona:
        value = persona[item].upper() if type(persona[item]) == str else persona[item]
        print(item, ":", value)

for item in persona:
	persona[item] = input(f"Ingrese su {item} :" )

imc=round(float(persona["Peso"])/(float(persona["Altura"])**2),2)
persona["IMC"]=imc

imprimir (persona)
cat_imc (imc)

   
   
   
   



