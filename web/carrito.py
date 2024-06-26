class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        
        cart = self.session.get("cart")
        montoTotal = self.session.get("cartMontoTotal")
        if not cart:
            cart = self.session["cart"] = {}
            montoTotal = self.session["cartMontoTotal"] = "0"
            
        self.cart = cart
        self.montoTotal = float(montoTotal)
        
    def add(self, producto, cantidad):
        producto_id = str(producto.id)  # Corregido aquí
        if producto_id not in self.cart.keys():
            self.cart[producto_id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "cantidad": cantidad,
                "precio": str(producto.precio),
                "imagen": producto.imagen.url,
                "categoria": producto.categoria.nombre,
                "subtotal": str(cantidad * producto.precio)
            }
        else:
            # Actualizar el producto en el carrito
            for key, value in self.cart.items():
                if key == producto_id:  # Corregido aquí
                    value["cantidad"] = str(int(value["cantidad"]) + cantidad)
                    value["subtotal"] = str(float(value["cantidad"]) * float(value["precio"]))
                    break
        self.save()
    
    def delete(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.cart:
            del self.cart[producto_id]
            self.save()
    
    def clear(self):
        self.session["cart"] = {}
        self.session["cartMontoTotal"] = "0"
        
    def save(self):
        """Guarda cambios en el carrito de compras"""
        montoTotal = 0
        for key, value in self.cart.items():
            montoTotal += float(value["subtotal"])
            
        self.session["cartMontoTotal"] = montoTotal
        self.session["cart"] = self.cart
        self.session.modified = True
