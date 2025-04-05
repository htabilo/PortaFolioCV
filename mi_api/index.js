     // Lista de productos
     const productos = [
        { nombre: "PC Gamer Ryzen", precio: 1200, imagen: "pc1.jpg" },
        { nombre: "Laptop Intel i7", precio: 900, imagen: "pc2.jpg" },
        { nombre: "MacBook Pro M2", precio: 1500, imagen: "pc3.jpg" }
    ];

    // Contenedor de productos
    const contenedor = document.getElementById("productos");

    // Generar tarjetas de productos
    productos.forEach(producto => {
        const card = document.createElement("div");
        card.className = "col-md-4";
        card.innerHTML = `
            <div class="card">
                <img src="${producto.imagen}" class="card-img-top" alt="${producto.nombre}">
                <div class="card-body">
                    <h5 class="card-title">${producto.nombre}</h5>
                    <p class="fw-bold">$${producto.precio}</p>
                    <button class="btn btn-primary" onclick="agregarAlCarrito('${producto.nombre}')">Agregar al carrito</button>
                </div>
            </div>
        `;
        contenedor.appendChild(card);
    });

    // Función para agregar al carrito
    function agregarAlCarrito(nombre) {
        alert(`✅ ${nombre} ha sido agregado al carrito.`);
    }
