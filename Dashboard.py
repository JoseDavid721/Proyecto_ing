import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import psycopg2
try:
    connection=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='123456789',
        database='Proyecto_bd'
    ) 
    print("Conexion exitosa")

    cursor=connection.cursor()
    cursor.execute('SELECT version()')
    rows=cursor.fetchall()
    cursor.execute('select distinct Rango_de_costo_unitario, count(ium) as cantidad from medicamento group by(Rango_de_costo_unitario)')
    rows1=cursor.fetchall()
    cursor.execute('select distinct nombre_importador, count(id) as cantidad_solicitudes from importador inner join solicitud on solicitud.id_importador = importador.id group by(id,nombre_importador) having count(id)>80')
    rows2=cursor.fetchall()
    cursor.execute('select distinct nombre_comercial_imagen_comercial, count(ium_medicamento) as cantidad_solicitudes from medicamento inner join solicitud on solicitud.ium_medicamento = medicamento.ium group by(ium_medicamento,nombre_comercial_imagen_comercial ) having  count(ium_medicamento)>50')
    rows3=cursor.fetchall()
    cursor.execute('select distinct tipo_solicitud, count(tipo_solicitud) as cantidad from solicitud group by(tipo_solicitud)')
    rows4=cursor.fetchall()
   


    external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]

    app=dash.Dash(__name__,external_stylesheets=external_stylesheets)
    fig = px.line(rows,x=0,y=1,color_discrete_sequence=["#e3b218"],height=500,width=900,
                      title='Poligono de Frecuencias(cantidad vs costo)')
    fig1= px.pie(rows,values=1,names=0,color_discrete_sequence=["#e3b218"],height=500,width=900,
                    title='Pie Graph(cantidad vs costo)')
    
    fig2 = px.bar(rows1,x=0,y=1,color_discrete_sequence=["#b52a64"],height=500,width=900,
                      title='Grafico_barras(cantidad vs nombre_importador)')
    fig3= px.pie(rows1,values=1,names=0,color_discrete_sequence=["#b52a64"],height=500,width=900,
                      title='Pie Graph(cantidad vs nombre_importador)')
    
    fig4 = px.bar(rows2,x=0,y=1,color_discrete_sequence=["#1572ab"],height=500,width=900,
                      title='Grafico_barras(cantidad vs nombre_comericial)')
    fig5= px.pie(rows2,values=1,names=0,color_discrete_sequence=["#1572ab"],height=500,width=900,
                      title='Pie Graph (cantidad vs nombre_comericial)')
     
    fig6 = px.bar(rows3,x=0,y=1,color_discrete_sequence=["#1572ab"],height=500,width=900,
                      title='Grafico_barras(cantidad vs nombre_comericial)')
    fig7= px.pie(rows3,values=1,names=0,color_discrete_sequence=["#1572ab"],height=500,width=900,
                      title='Pie Graph (cantidad vs nombre_comericial)')
    
    
    
    app.layout = html.Div([
        
        html.Div([
        html.H2('Dashboards'),
        html.Img(src="/assets/grafico.png")
        ],className='banner'),
        
        html.Div([
            html.H2('Rango de costos en el que se encuentra cada medicamento'),
            html.Div(),
                dcc.Graph(
                id='Grafica',
                figure=fig
                ),
        ],className='container'),

        html.Div([
            html.Div(),
            dcc.Graph(
                id='Grafica',
                figure=fig1
                )
        
    ],className='container'),
    
    html.Div([
            html.H2('Importadores que más solicitudes realizaron'),
            html.Div(),
                dcc.Graph(
                id='Grafica',
                figure=fig2
                ),
        ],className='container'),

        html.Div([
            html.Div(),
            dcc.Graph(
                id='Grafica',
                figure=fig3
                ),
        
        ],className='container'),
        
        
        html.Div([
            html.H2('Medicamentos más demandados'),
            html.Div(),
                dcc.Graph(
                id='Grafica',
                figure=fig4
                ),
        ],className='container'),

        html.Div([
            html.Div(),
            dcc.Graph(
                id='Grafica',
                figure=fig5
                ),
        
        ],className='container'),
         
        html.Div([
            html.H2('Número de solicitudes de cada tipo de solicitud '),
            html.Div(),
            dcc.Graph(
                id='Grafica',
                figure=fig6
                ),
        ],className='row'),
           
           

        html.Div([
            html.Div(),
            dcc.Graph(
                id='Grafica',
                figure=fig1
                   ),
    
    
        ])
    ])    
    if __name__ == '__main__':
         app.run_server(debug = True)

except Exception as ex:
    print(ex)

finally:
   
    
    connection.close()
    print("Conexion finalizada.")