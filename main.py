from flask import Flask, redirect,render_template,request
app= Flask(__name__)

#datos
usuarios=['admin@gmail.com','juan@gmail.com','pedro@gmai.com']
contrasenas=['123','456','789']
prods=['teclado','raton']

#vistas
@app.route('/', methods=['post','get'])
def login():
    if request.method=='POST':
        nombre=request.form['nombre']
        contrasena=request.form['contra']
        cont=0
        for u in usuarios :
            if nombre==u and contrasena==contrasenas[cont]:
                return render_template('principal.html',nombre=nombre)
            cont=cont+1
    return render_template('login.html')

@app.route('/productos', methods=['post','get'])
def productos():
    return render_template('productos.html',productos=prods)

@app.route('/registrarProd',methods=['post','get'])
def registrarProd():
    if request.method=='POST':
        nuevo=request.form['nombreProd']
        prods.append(nuevo)
        return render_template('productos.html',productos=prods)
    return render_template('registrarProducto.html')


@app.route('/editarProd/<int:idProd>',methods=['post','get'])
def editarProd(idProd):
    if request.method=='POST':
        nuevo=request.form['nombreProd']
        prods[idProd-1]=nuevo
        return render_template('productos.html',productos=prods)
    prod=prods[idProd-1]
    return render_template('editarProducto.html',producto=prod,idProd=idProd)


@app.route('/eliminarProd/<int:idProd>',methods=['post','get'])
def eliminarProd(idProd):
    if request.method=='POST':
        prod=request.form['nombreProd']
        prods.remove(prod)
        return render_template('productos.html',productos=prods)
    prod=prods[idProd-1]
    return render_template('eliminarProducto.html',producto=prod,idProd=idProd)

#main
if __name__=='__main__':
    app.run(debug=True)
    #app.run(debug=True,host = '127.0.0.1', port = '5001')
    #app.run(debug=True,host = '0.0.0.0', port = '80')

# habilitar el entorno virtual
#en windows venv\scripts\activate
#en mac source venv/bin/activate

#levantar el servidor
#python .m main
