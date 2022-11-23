import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import psycopg2
import dash_Importador_func

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
    row=cursor.fetchone()
    print(row)
    dfCases=cursor.execute(dash_Importador_func())
    
    rows=cursor.fetchall()
   


    external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]

    app=dash.Dash(__name__,external_stylesheets=external_stylesheets)
    fig = px.bar(rows,x=0,y=1,color_discrete_sequence=["#b52a64"],height=500,width=900,
                      title='Grafico_barras(cantidad vs nombre_importador)')
    fig1= px.pie(rows,values=1,names=0,color_discrete_sequence=["#b52a64"],height=500,width=900,
                      title='Pie Graph(cantidad vs nombre_importador)')
    
    
    app.layout = html.Div([
        
        html.Div([
        html.H2('Importadores que mas solicitan'),
        html.Img(src="/assets/grafico.png")
        ],className='banner'),
        
        html.Div([
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
        
    ],className='container')
    
    ])
    if __name__ == ('__main__'):
        app.run_server(debug=True)  
    

except Exception as ex:
    print(ex)

finally:
   
    
    connection.close()
    print("Conexion finalizada.")