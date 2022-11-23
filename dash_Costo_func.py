def dash_Costo():
    return """select distinct Rango_de_costo_unitario, count(ium) as cantidad from medicamento group by(Rango_de_costo_unitario)"""