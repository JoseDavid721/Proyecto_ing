def dash_Tipo_Solicitud():
    return """select distinct tipo_solicitud, count(tipo_solicitud) as cantidad from solicitud group by(tipo_solicitud)"""