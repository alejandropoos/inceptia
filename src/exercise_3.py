_AVAILABLE_DISCOUNT_CODES = ["Primavera2021", "Verano2021", "Navidad2x1", "heladoFrozen"]


def validate_discount_code() -> dict:
    """
    Response:
        {
            "valid_code": bool,\n
            "message": str
        }
        
    valid_code possible cases:
        True: 
            ->Voucher Accepted
            
        False:
            ->Voucher Rejected
    """
    
    pairwise_differences    = []
    discount_code_character = []
    len_codes               = []
    
    discount_code   = input("Ingrese un codigo de descuento: ")
    
    if discount_code == "":
        return {
            "valid_code":   False,
            "message":      "No ha introducido un codigo, por favor intentelo de nuevo."}
    
    for character in discount_code: discount_code_character.append(character)
    
    try:
        for code in _AVAILABLE_DISCOUNT_CODES:
           len_codes.append(len(code))
        
        if len(discount_code) not in len_codes:
            return {
                "valid_code":   False,
                "message":      "Codigo invalido."}
                    
        for code in _AVAILABLE_DISCOUNT_CODES:
            if len(discount_code) != len(code):
                continue
            
            for i in range(len(code)):
                if discount_code_character[i] != code[i]:
                    pairwise_differences.append(2)
        
        if len(pairwise_differences) > 1:
            return {
                "valid_code":   False,
                "message":      "Codigo invalido."}
        else:
            return {
                "valid_code":   True,
                "message":      "Codigo aceptado."}
    except IndexError:
        return {
            "valid_code":   False,
            "message":      "Codigo invalido."}