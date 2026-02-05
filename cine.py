# compra: No pueden comprar mas de 7 boletos por persona

# precio boleto: 12$

# descuentos: => 6  --> 15% sobre el total

#             = 3, 4, 5  --> 10% sobre el total 

#             = 1, 2 --> no descuento

# pago con cineco - 10% sobre el total
#

def procesar(formPago, cantB, cantP ):

    max_boletos = int(cantP) * 7
    

    if cantB > max_boletos:
        return f"No se pueden vender más de {max_boletos} boletos para {cantP} personas"
    if cantB <= 0:
        return f"No se pueden menos de 0 boletos"

    # precio base
    totPago = cantB * 12
    
    if cantB >= 6:
        totPago = totPago - (totPago * .15)

    if  3 <= cantB <= 5:
        totPago = totPago - (totPago * .10)

    # descuento por tarjeta cineco
    if formPago == "si":
        totPago -= totPago * 0.10

    return  totPago
    