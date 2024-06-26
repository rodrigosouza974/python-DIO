def funcao_principal(func):
    
    def funcao_interna1():
        print("Algo está acontecendo na função 1.")
    
    def funcao_interna2():
        print("Algo está acontecendo na função 2.")    

    funcao_interna1()
    funcao_interna2()

funcao_principal()