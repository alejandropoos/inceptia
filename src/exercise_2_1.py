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

def is_product_available(product_name:str, quantity:int) -> bool:
    """
    Response:
        True: 
            ->Available Product\n
        False:\n 
            ->Product not Avilable\n
    """
    try:
        product_name            = unidecode(product_name).capitalize()
        validate_product        = _PRODUCT_DF.where(_PRODUCT_DF.product_name == product_name).dropna()
        quantity_validate       = int(validate_product.quantity.values[0])
        product_name_validate   = str(validate_product.product_name.values[0])
        
        [product_name_validate.split(i) for i in product_name_validate if i != product_name]
        
        if quantity_validate    >= quantity:    return True
        elif quantity_validate  < quantity:     return False
        
    except Exception:
        return False
    
if __name__ == '__main__':
    product_in_stock = is_product_available("limón", 3)
    print(product_in_stock)