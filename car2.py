while True:
    Gari_qisam = input("Kam gari ba wakhli (Sada ya Fancy): ").lower()
    Oraze = int(input("So oraze ba chalay: "))

    match Gari_qisam:
        case "sada":
            Daily_rate = 2000
        case "fancy":
            Daily_rate = 5000
        case _:
            print("Invalid gari qisam. Faqat 'Sada' ya 'Fancy' likha.")
            continue  

    subtotal = Daily_rate * Oraze

    if Oraze > 7:
        rihayat = subtotal * 0.10  
        rihayat = 0

    discounted_total = subtotal - rihayat

    Na_Jeza_Pese = discounted_total * 0.15

    Tol_Raqam = discounted_total + Na_Jeza_Pese

    print("\n----- Da Karayae Hisab -----")
    print(f"Gari Qisam     : {Gari_qisam.capitalize()}")
    print(f"Oraze          : {Oraze}")
    print(f"Daily Rate     : Rs. {Daily_rate}")
    print(f"Subtotal       : Rs. {subtotal}")
    print(f"Rihayat (Discount) : Rs. {rihayat}")
    print(f"Na Jeza Pese (Tax) : Rs. {Na_Jeza_Pese}")
    print(f"Tol Raqam      : Rs. {Tol_Raqam}")
    print("------ Bal Qas ------")
    
    break