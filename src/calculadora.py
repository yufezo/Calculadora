from dash import Dash, html, dcc, callback, Output, Input

app = Dash()

# Criar botão que aumenta contador

app.layout = [
    html.H1(id='counter'),
    html.Button(children='Clique aqui', id='counterButton')
]

@callback(
    Output('counter', 'children'),
    Input('counterButton', 'n_clicks')
)
def updateCounter(counter):
    if counter is None:
        return '0'
    else:
        return counter

if __name__ == '__main__':
    app.run(debug=True)
