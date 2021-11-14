from src.model.Usuario import Usuario
from src.model.Compra import Compra

def filtro_solo_rangoCompras(rango_inf, rango_sup):
    usuarios= Usuario.select().where(Usuario.acum_compras >= rango_inf, Usuario.acum_compras <= rango_sup)