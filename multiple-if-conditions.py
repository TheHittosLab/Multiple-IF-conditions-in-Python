print("Saludos guerrero, ¿Qué desea comprar?\n\n" + 
      "Items disponibles:\n\n" +
      "Espadas:\n\n" + 
      "1-Espada Nivel 1: 150 Monedas de oro.\n" +
      "2-Espada Nivel 2: 1200 Monedas de oro.\n\n" +
      "Escudos: \n\n" + 
      "3-Escudo Nivel 1: 100 Monedas de oro.\n" +
      "4-Escudo Nivel 2: 750 Monedas de oro.\n")

comprar = []

dinero = 1500

espadaLV1 = 150

espadaLV2 = 1200

escudoLV1 = 100

escudoLV2 = 750

if 0 in comprar or comprar == []:
    print("Especifica un número entre 1 y 4.")

if 1 in comprar:
    dinero = dinero - espadaLV1

if 2 in comprar:
    dinero = dinero - espadaLV2

if 3 in comprar:
    dinero = dinero - escudoLV1

if 4 in comprar:
    dinero = dinero - escudoLV2

else:
    print("Especifica un número entre 1 y 4.")

if dinero < 0:
    print("¡No te llega el dinero para todo eso!")

if comprar == [1] or comprar == [2] or comprar == [3] or comprar == [4]:
    print("Te quedan " + str(dinero) + " Monedas de oro.")
    print("Se añadió el/los objeto/s a tu inventario.")