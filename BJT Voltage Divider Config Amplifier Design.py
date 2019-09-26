def BJT_Amp_Design():
    print("BJT Voltage Divider Config Amplifier Design with known operating point")
    print("***********************************************************************")
    print()
    print()

    Vcc = eval(input("Enter source voltage (Vcc) in volts: "))
    print()
    print("Enter Operating Point:")
    Ic = eval(input("Collector Current (Ic) in milliamps: "))
    Ib = eval(input("Base Current (Ib) in microamps: "))
    Vce = eval(input("Collector-Emitter voltage (Vce): "))
    print()

    #Saving values for percent difference calculation
    Ic1 = Ic
    Ib1 = Ib
    Vce1 = Vce
    #---------------------------------
    
    beta = Ic/(Ib/1000)
    Ie = (1 + beta)*(Ib/1000)
    Ve = 0.1*Vcc

    Re = Ve/Ie    
    Rc = (Vcc - Vce - Re*Ie)/Ic    
    R2 = 0.1*beta*Re    
    Vb = 0.7 + Ve
    R1 = (R2*Vcc)/Vb - R2

    #print("beta = ",beta)
    #print("Ie = ",Ie,"(mA)")
    #print("Ve =",Ve,"(V)")
    #print("Vb =",Vb, "(V)")

    print()
    print("Necessary Resistors: ")
    print("***************************")
    print("Re =",Re,"(kΩ)")
    print("Rc =",Rc,"(kΩ)")
    print("R1 =",R1,"(kΩ)")
    print("R2 =",R2,"(kΩ)")

    print()
    print("Need Standard Resistors for Real Circuit:")
    Re = eval(input("Standard Re (kΩ): "))
    Rc = eval(input("Standard Rc (kΩ): "))
    R1 = eval(input("Standard R1 (kΩ): "))
    R2 = eval(input("Standard R2 (kΩ): "))
    print()

    print()
    print("New Operating Point:")
    print("********************")
    Vb = R2/(R1+R2)*Vcc
    Vbe = Vb - Ve
    Ie = Ve/Re
    #Assuming beta remains constant
    Ib = 1000*Ie/(beta + 1)
    Ic = beta * Ib/1000
    Vce = Vcc - Ic*Rc - Ie*Re

    print("Ib =",Ib,"μA")
    print("Ic =",Ic,"mA")
    print("Vce =",Vce,"V")
    print()

    #Saving values for percent difference calculation
    Ib2 = Ib
    Ic2 = Ic
    Vce2 = Vce
    #--------------------------------------------
    
    print()
    print("Percent Difference Between Operating Point Values:")
    print("**************************************************")
    PDIb = (abs(Ib2-Ib1)/((Ib1+Ib2)/2))*100
    PDIc = (abs(Ic2-Ic1)/((Ic1+Ic2)/2))*100
    PDVce = (abs(Vce2-Vce1)/((Vce1+Vce2)/2))*100

    print("Ib:",PDIb,"%")
    print("Ic:",PDIc,"%")
    print("Vce:",PDVce,"%")

BJT_Amp_Design()
