def calculadora(operacao):
    def soma(a,b):
        return a + b

    def sub(a,b):
        return a - b
    
    def multi(a,b):
        return a * b
    
    def div(a,b):
        return a / b
    
    match operacao :
        case"+":
            return soma
        case"-":
            return sub
        case"*":
            return multi
        case"/":
            return div
        

calculadora("+")(2,2)
calculadora("-")(7,2)
calculadora("*")(2,2)
calculadora("/")(2,2)

