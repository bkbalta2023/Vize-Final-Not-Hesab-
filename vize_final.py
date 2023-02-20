print("""
*****************************
Not Ortalaması Hesap Programı
*****************************
""")

v1 = int(input("Vize1 Notu: "))
v2 = int(input("Vize2 Notu: "))
v3 = int(input("Vize2 Notu: "))

hesap = (v1*0.3)+(v2*0.3)+(v3*0.4)

if hesap >= 90:
    print("A1")
elif hesap >= 80:
    print("A2")
elif hesap >= 70:
    print("B1")
elif hesap >= 65:
    print("B2")
elif hesap >= 60:
    print("C")
elif hesap < 60:""
    print("F3")
else:
    print("Geçersiz not girdiniz.")