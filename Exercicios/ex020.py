# if Ellse e operadores logicos
tenho_sede= False
tenho_fome= True

estou_em_dieta=True

if tenho_sede and tenho_fome:
    print("Fazer um sanduiche e uma Coquinha")
elif tenho_sede and not(tenho_fome):
    if estou_em_dieta:
        print("Tomar agua")
    else:
        print("Tomar uma coquinha")
elif not(tenho_sede) and tenho_fome:
    print("Fazer um sanduiche")
else:
    print("Ficar vendo Netflix")
