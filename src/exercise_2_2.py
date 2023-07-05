import pandas as pd
from unidecode import unidecode

_PRODUCT_DF = pd.DataFrame(
                {
                    "product_name": [
                        "Chocolate", 
                        "Granizado", 
                        "Limon", 
                        "Dulce de leche"], 
                    "quantity": [3, 10, 0, 5]})

def is_product_available() -> dict:
    """
    Response:
        {
            "in_stock": bool,\n
            "message": str
        }
    
    in_stock possible cases:
        True: 
            ->Available Product
            
        False:
            ->Product not Avilable
    """

    
    input_product = input(
        '''
        \033[1mCartilla de sabores y cantidades disponibles en stock\033[0m
        \t\033[1m   Sabores        |   En stock inmediato\033[0m
        \tChocolate         |           3
        \tGranizado         |           10
        \tLimon             |       -Sin stock-
        \tDulce de leche    |           5
        
        Ingrese un producto por favor: 
        '''
        )
    input_quantity = int(input("Por favor, indique la cantidad deseada del gusto {}: ". format(input_product)))
    
    try:
        input_product            = unidecode(input_product).capitalize()
        validate_product        = _PRODUCT_DF.where(_PRODUCT_DF.product_name == input_product).dropna()
        quantity_validate       = int(validate_product.quantity.values[0])
        product_name_validate   = str(validate_product.product_name.values[0])

        [product_name_validate.split(i) for i in product_name_validate if i != input_product]
        
        if quantity_validate    <= 0: 
            return {
                "in_stock": False, 
                "message": "\nOh no! El 1 sabor {} se encuentra sin stock momentaneamente.\n Prueba elegir otro!\n".format(input_product)}
        if quantity_validate    >= input_quantity: 
            return {
                "in_stock": True,
                "message": ""}
        elif quantity_validate  <  input_quantity: 
            return {
                "in_stock": False, 
                "message": "\nOh no! El 2 sabor {} se encuentra sin stock momentaneamente.\n Prueba elegir otro!\n".format(input_product)}
        
    except IndexError:
        return {
            "in_stock": False, 
            "message": "\nOh no! El sabor {} lamentablemente es inexistente en nuestra cartilla.\n Prueba elegir otro!\n".format(input_product)}
    except AttributeError:
        return {
            "in_stock": False, 
            "message": "\nPor favor, ingrese unicamente sabores en formato texto.\n"}
    except TypeError:
        return {
            "in_stock": False, 
            "message": "\nPor favor, para cantidades ingrese valores numéricos unicamente en formato entero. (sin comillas - not string)\n"}
