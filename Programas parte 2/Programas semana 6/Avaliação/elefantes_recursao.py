def incomodam(numero_incomodam):
    

    if numero_incomodam <= 0:  # Base da recursao 
       return ""  
    
    if numero_incomodam > 0:
        
        return "incomodam " + incomodam(numero_incomodam - 1) # Recursao
        
def elefantes(numero_cancao):

    if numero_cancao < 1: # Base da recursao
        return ""
    
    if numero_cancao >= 1:
        print("Um elefante incomoda muita gente")
        return str(elefantes(numero_cancao - 1)) + str(numero_cancao - 1) + " elefantes incomodam muita gente\n" + str(numero_cancao) + " elefantes " + str(incomodam(numero_cancao)) + "muito mais\n"
