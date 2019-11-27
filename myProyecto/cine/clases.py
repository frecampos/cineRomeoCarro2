class elemento:
    cod=0
    nombre=""
    precio=0
    cantidad=0

    def __init__(self,codigo,nombre,precio,cantidad):
        self.cod=codigo
        self.nombre=nombre
        self.precio=precio
        self.cantidad=cantidad
    
    def toString(self):
        return {
            'codigo': str(self.cod),
            'nombre': self.nombre,
            'precio': str(self.precio),
            'cantidad': str(self.cantidad),
            'total':str(self.total())
        }
    def total(self):
        return str(int(self.precio)*int(self.cantidad))
        
class CartItem(object):

    def __init__(self, pelicula, cantidad, precio):
        self.pelicula = pelicula
        self.cantidad = int(cantidad)
        self.precio = int(precio)

    def __repr__(self):
        return u'CartItem Object (%s)' % self.pelicula

    def to_dict(self):
        return {
            'pelicula_name': self.pelicula.name,
            'cantidad': self.cantidad,
            'precio': str(self.precio),
        }

    @property
    def subtotal(self):        
        return self.precio * self.cantidad


class carrito(object):

    def __init__(self,session,session_key=None):        
        self.arreglo= {} 
        self.session = session  
        self.session_key = session_key         

    def agregar(self, pelicula, precio=None, cantidad=1):
        self.arreglo[pelicula.name]=CartItem(pelicula, cantidad, precio)
        self.update_session()

    def update_session(self):
        """
        Serializes the cart data, saves it to session and marks session as modified.
        """
        self.session[self.session_key] = self.cart_serializable
        self.session.modified = True

    @property
    def cart_serializable(self):
        """
        The serializable representation of the cart.
        For instance:
        {
            '1': {'product_pk': 1, 'quantity': 2, price: '9.99'},
            '2': {'product_pk': 2, 'quantity': 3, price: '29.99'},
        }
        Note how the product pk servers as the dictionary key.
        """
        cart_representation = {}
        for item in self.items:
            # JSON serialization: object attribute should be a string
            product_id = str(item.pelicula.name)
            cart_representation[product_id] = item.to_dict()
        return cart_representation

    @property
    def items(self):
        return self.arreglo.values()

    @property
    def items(self):
        """
        The list of cart items.
        """
        return self.arreglo.values()

class Compras(object):

    def __init__(self,session):        
        self.arreglo={}
        self.session = session  
        self.session_key = "compras"         

    def agregar(self, pelicula, precio=None, cantidad=1):
        self.arreglo[pelicula.name]=CartItem(pelicula, cantidad, precio)
        self.update_session()

    def update_session(self):
        """
        Serializes the cart data, saves it to session and marks session as modified.
        """
        self.session[self.session_key] = self.cart_serializable
        self.session.modified = True

    @property
    def cart_serializable(self):
        """
        The serializable representation of the cart.
        For instance:
        {
            '1': {'product_pk': 1, 'quantity': 2, price: '9.99'},
            '2': {'product_pk': 2, 'quantity': 3, price: '29.99'},
        }
        Note how the product pk servers as the dictionary key.
        """
        cart_representation = {}
        for item in self.items:
            # JSON serialization: object attribute should be a string
            product_id = str(item.pelicula.name)
            cart_representation[product_id] = item.to_dict()
        return cart_representation

    @property
    def items(self):
        return self.arreglo.values()

    @property
    def items(self):
        """
        The list of cart items.
        """
        return self.arreglo.values()
