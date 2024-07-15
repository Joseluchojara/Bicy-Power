
// Función para mostrar u ocultar el detalle del carrito
function toggleCarrito() {
    const carritoDetalle = document.getElementById('carrito-detalle');
    
    if (carritoDetalle.style.display === 'none' || carritoDetalle.style.display === '') {
        carritoDetalle.style.display = 'block';
    } else {
        carritoDetalle.style.display = 'none';
    }
}

// Función para agregar un producto al carrito
function agregarAlCarrito(producto) {
    // Crear elemento de lista para el producto
    const listaProductos = document.getElementById('lista-productos');
    const nuevoProducto = document.createElement('li');
    nuevoProducto.innerHTML = `${producto.nombre} - $${producto.precio.toFixed(2)} <button class="eliminar" onclick="eliminarProducto(this, ${producto.precio})">Eliminar</button>`;
    
    // Agregar el producto a la lista del carrito
    listaProductos.appendChild(nuevoProducto);

    // Sumar el precio del producto al total
    sumarTotal(producto.precio);

    // Actualizar la cantidad de productos en el carrito
    actualizarCantidadCarrito();
}

// Función para eliminar un producto del carrito
function eliminarProducto(elemento, precioProducto) {
    // Eliminar el elemento de la lista
    elemento.parentNode.remove();
    
    // Restar el precio del producto eliminado al total
    restarTotal(precioProducto);

    // Actualizar la cantidad de productos en el carrito
    actualizarCantidadCarrito();
}

// Función para sumar el precio al total del carrito
function sumarTotal(precio) {
    const totalElemento = document.getElementById('total');
    let total = parseFloat(totalElemento.textContent);
    total += precio;
    totalElemento.textContent = total.toFixed(2);
}

// Función para restar el precio al total del carrito
function restarTotal(precio) {
    const totalElemento = document.getElementById('total');
    let total = parseFloat(totalElemento.textContent);
    total -= precio;
    totalElemento.textContent = total.toFixed(2);
}

// Función para actualizar la cantidad de productos en el carrito
function actualizarCantidadCarrito() {
    const cantidadProductos = document.getElementById('lista-productos').childElementCount;
    const carritoCantidad = document.getElementById('carrito-cantidad');
    carritoCantidad.textContent = cantidadProductos;
}

