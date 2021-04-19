def ambito_test():
    def hacer_local():
        spam = "spam local"
    def hacer_nolocal():
        nonlocal spam
        spam = "spam no local"
    def hacer_global():
        global spam
        spam = "spam global"
    spam = "test spam"
    hacer_local()
    print("despues de hacisnar la variable local:", spam)
    hacer_nolocal()
    print("despues de asignar la variable no local:",spam)
    hacer_global()
    print("despues de la acignacion de variable global:",spam)

ambito_test()
print("el ambito global:", spam)