rango_compras = '51-56'
rango_compras= rango_compras.split('-')
if len(rango_compras)==2:   
    compra_inferior = rango_compras[0]
    compra_superior = rango_compras[1]
elif len(rango_compras)==1:
    compra_inferior = '0'
    compra_superior = rango_compras[0]




print(compra_superior)