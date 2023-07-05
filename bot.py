from src.exercise_1     import GeoAPI
from src.exercise_2_2   import *
from src.exercise_3     import *


class ChatBot:
    
    @classmethod
    def build(cls):
        temperature_above_28 = GeoAPI.is_hot_in_pehuajo()
        if temperature_above_28: 
                print("Bienvenida 1")
        else:   print("Bienvenida 2")
        
      
        in_stock = False      
        while in_stock == False:
            validation_stock = is_product_available()
            print(validation_stock.get("message"))
            in_stock = validation_stock.get("in_stock")
        
        
        valid_code = False      
        while valid_code == False:
            validation_code = validate_discount_code()
            print(validation_code.get("message"))
            valid_code = validation_code.get("valid_code")
        
        print("Pedido confirmado con exito.")
    
        
        
if __name__ == '__main__':
    ChatBot.build()