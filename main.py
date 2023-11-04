import pandas as pd
# Conexión a la base de datos
URI_CNX = "mysql+pymysql://mysql:mysql@127.0.0.1:3306/neptuno"
# Generando las consultas SQL
Q_PRODUCTOS = "SELECT * FROM productos;"
Q_PROVEEDORES = "SELECT * FROM proveedores;"
Q_CLIENTES = "SELECT * FROM clientes;"
Q_PEDIDOS = "SELECT * FROM pedidos;"
Q_DETALLES = "SELECT * FROM detalles;"

# Obteniendo el resultado de las consultas en un dataframe
df_productos = pd.read_sql(Q_PRODUCTOS, URI_CNX)
df_proveedores = pd.read_sql(Q_PROVEEDORES, URI_CNX)
df_clientes = pd.read_sql(Q_CLIENTES, URI_CNX)
df_pedidos = pd.read_sql(Q_PEDIDOS, URI_CNX)
df_detalles = pd.read_sql(Q_DETALLES, URI_CNX)

# Mostrando la cantidad de id_proveedores en la tabla producto y verificando que ninguno sea nulo
print(df_productos['proveedor_id'].info())

# Uniendo el df producto y proveedor
df_prod_prov = pd.merge(df_productos, df_proveedores,
                        how="inner", left_on="proveedor_id", right_on="id")
# restructurando el df resultante y manteniendo solo el id del producto, producto  y empresa del proveedor
df_prod_prov = df_prod_prov[['id_x', 'producto', 'empresa']]
# cambiando el nombre de las columnas a id_producto, producto y proveedor
df_prod_prov.columns = ['id_producto', 'producto', 'proveedor']
print(df_prod_prov)

# Manteniendo solo la columna id, empresa y pais del df_clientes
df_clientes = df_clientes[['id', 'empresa', 'pais']]
# cambiando el nombre de las columnas a id_cliente, empresacliente, paiscliente
df_clientes.columns = ['id_cliente', 'empresacliente', 'paiscliente']
print(df_clientes)

# generando la columna preciototal en el df_detalles, en base a la siguiente fórmula: (PrecioVenta*CantidadVendida) - (PrecioVenta*CantidadVendida*Descuento)
df_detalles['preciototal'] = (df_detalles['precio_unidad']*df_detalles['cantidad']) - (
    df_detalles['precio_unidad']*df_detalles['cantidad']*df_detalles['descuento'])
print(df_detalles)

# generando la columna precioconimpuesto en el df_detalles, incrementando el 13% al preciototal
df_detalles['precioconimpuesto'] = df_detalles['preciototal'] + \
    (df_detalles['preciototal'] * 0.13)

print(df_detalles)

# creando el df_ventas uniendo el df_pedidos con df_clientes respetando los registros de df_pedidos
df_ventas = pd.merge(df_pedidos, df_clientes, how="left",
                     left_on="cliente_id", right_on="id_cliente")

# restructurando df_ventas para mantener solo las columnas: empresacliente, paiscliente, fecha_pedido, id
df_ventas = df_ventas[['empresacliente',
                       'paiscliente', 'fecha_pedido', 'id']]
# verificando valores nulos en la unión de cliente con pedidos
print(df_ventas.isnull().sum())
# se identifica que no se cuenta con valores nulos

# uniendo a df_ped_prod los df df_detalles y df_prod_prov

df_ped_prod = pd.merge(df_detalles, df_prod_prov, how="left",
                       left_on="producto_id", right_on="id_producto")
# restructurando df_ped_prod para mantener solo las columnas producto, proveedor, precio_unidad, cantidad, descuento, preciototal, precioconimpuesto,id
df_ped_prod = df_ped_prod[['producto', 'proveedor', 'precio_unidad',
                           'cantidad', 'descuento', 'preciototal', 'precioconimpuesto', 'id']]
# verificando valores nulos en la unión de detalle y producto
print(df_ped_prod.isnull().sum())
# se identifica que no se cuenta con valores nulos

# uniendo a df_ventas el df_ped_prod manteniendo los registros de ambos df si no hubiera coincidencia
df_ventas = pd.merge(df_ventas, df_ped_prod, how="outer")

# restructurando df_ventas en el orden y campos solicitados
df_ventas = df_ventas[['producto', 'proveedor', 'empresacliente', 'paiscliente',
                       'fecha_pedido', 'precio_unidad', 'cantidad', 'descuento', 'preciototal', 'precioconimpuesto']]
# verificando valores nulos en la unión final de ventas con detalle
print(df_ventas.isnull().sum())
# Se identifica que no se cuenta con valores nulos
# Modificando el nombre de las columnas
df_ventas.columns = ['Producto', 'Proveedor', 'EmpresaCliente', 'PaisCliente', 'FechaPedido',
                     'PrecioVenta', 'CantidadVendida', 'Descuento', 'PrecioTotal', 'PrecioConImpuestos']

# generando el detalle del df_ventas
print(df_ventas.describe())

print("En base al detalle anterior sepuede iddentificar que:")
print(
    f"La venta con precio menor es: {min(df_ventas['PrecioTotal'])}, realizado en fecha(s)")
print(df_ventas[df_ventas['PrecioTotal'] == min(
    df_ventas['PrecioTotal'])]['FechaPedido'])
print(
    f"La venta con precio mayor es: {max(df_ventas['PrecioTotal'])}, realizado en fecha(s)")
print(df_ventas[df_ventas['PrecioTotal'] == max(
    df_ventas['PrecioTotal'])]['FechaPedido'])
print(
    f"Se realizaron {df_ventas[df_ventas['Descuento']>0]['Descuento'].count()} ventas con descuento de un total de {df_ventas['Producto'].count()}")
print(f"Llegando a descontar un total de: $ {df_ventas['Descuento'].sum()}")
print(
    f"Asimismo, se recaudó un total de: $ {df_ventas['PrecioConImpuestos'].sum()-df_ventas['PrecioTotal'].sum()} a favor de impuestos")

print(f"En total se cuentan con:\n {df_ventas['Producto'].value_counts().count()} productos\n {df_ventas['Proveedor'].value_counts().count()} Proveedores\n {df_ventas['EmpresaCliente'].value_counts().count()} Clientes de {df_ventas['PaisCliente'].value_counts().count()} países")
# Operaciones por agrupación
print("A continuación se detalla la cantidad de productos realizados en total demanera descendente:")
print((df_ventas.groupby('Producto')[
      'CantidadVendida'].sum()).sort_values(ascending=False))
print("A continuación se detalla la recaudación sin impuestos, ordenado por gestión de manera descendente")
df_ventas['Gestion'] = df_ventas['FechaPedido'].dt.strftime('%Y')
print((df_ventas.groupby('Gestion')[
      'PrecioTotal'].sum()).sort_index(ascending=False))
