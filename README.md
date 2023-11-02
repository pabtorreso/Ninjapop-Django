# Ninjapop (Proyecto e-commerce con Django)
### INSTRUCCIONES

1. Abrir `entornoVirtual.bat`
2. Instalar dependencias con: `pip install -r requirements.txt`
3. Levantar servidor Django con: `py manage.py runserver`
4. Ingresar a la página desde el navegador con este link: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
5. Para matar el servidor se puede usar `ctrl+c` y para salir del entorno virtual se puede usar: `deactivate`

---

# CREDENCIALES

**user:** admin  
**pass:** 6fR344apq

**user:** maria  
**pass:** 628jKPZrs

---

### CAPACIDADES

- La página puede manejar usuarios desde la pestaña iniciar sesión y registrarse.
- Si se ingresa como admin, se habilitará un acceso al panel de admin CRUD de usuarios y productos.
- Se puede cambiar el estado de administrador de cada usuario desde el panel de administrador.
- La página tiene modo oscuro para los que lo necesitan.
- La página principal muestra un carrusel con publicidad y ofertas. Además, muestra los productos destacados.
- La plantilla catálogo muestra un total de 6 productos por página (tiene sistema de paginación).
- La barra de buscar buscará el producto que coincida con lo que se escriba.
- El carrito de compras funciona por sesiones de usuario, cada usuario tiene su propio carrito.
- El carrito de compras genera un total y suma productos. Los productos se pueden eliminar del carrito.
- Antes de proceder a pagar aparece un modal preguntando si está seguro.
- Cada producto tiene un stock, si el stock es 0 este no se puede agregar al carrito y aparecerá como "No disponible".
- La página consume la API de la CMF y muestra el valor del dólar más reciente en el `navbarText`.
- La página posee una plantilla para contacto, otra para preguntas y respuestas y otra sobre información del cliente.
