while True:
 Gari_qisam = input("kam gare ba boze (Sada or Fancy):").lower()

 Oraze = int(input("so oraze be chalay "))

 match Gari_qisam:
    case "sada":
        Orazo_hisab =  2000
    case "fancy":
        Orazo_hisab =  5000
    case _:
        print("Invalid car type.")
        exit()

 Orazo_hisab = Orazo_hisab * Oraze

 if Oraze > 7:
    rihayat = Orazo_hisab * 0.10  
 else:
    rihayat = 0
 subtotal = Orazo_hisab
 Orazo_hisab = subtotal - rihayat

 Na_Jeza_Pese = subtotal * 0.015

 Tol_Raqam = subtotal + Na_Jeza_Pese

 print("\n----- da karayae hesab -----")
 print(f"Gari Qisam    : {Gari_qisam}")
 print(f"Orazo Hesab   : {Oraze}")
 print(f"rihayat       : {rihayat}")
 print(f"Na Jeza Pese  : Rs. {Na_Jeza_Pese}")
 print(f"Tol Raqam     : Rs. {Tol_Raqam}")
 print("BAL QAS ROLEGA")