def dash_Nombre_Comercial_func():
    return """select distinct nombre_comercial_imagen_comercial, count(ium_medicamento) as cantidad_solicitudes from medicamento inner join solicitud on solicitud.ium_medicamento = medicamento.ium group by(ium_medicamento,nombre_comercial_imagen_comercial ) having  count(ium_medicamento)>50"""