def Rcalc():
    A_string=raw_input("Please enter the area of the wall (in m2): ")
    A=float(A_string)
    NumberOfLayers_string=raw_input("Please enterNumber of layers: ")
    NumberOfLayers=float(NumberOfLayers_string)
    layerNumber=1
    R_tot=0
    while layerNumber<=NumberOfLayers:
        print("\n \n \n Layer Number "+ str(layerNumber)+ "\n")
        L=raw_input("Please Enter the length of the layer (in m): ")
        k=raw_input("Please Enter the condictivty of the layer (in W/(m*K)): ")
        print("\n you just said that in this layer"+ "L= " + L+ " m  "+ "k= "+ k +" W/(m*K) \n")
        R_layer=float(L)/(float(k)*A)
        R_tot=R_tot+R_layer
        print("\n The layer's Resistance is"+ str(R_layer)+ " degC/W \n")
        layerNumber=layerNumber+1
    print("\n We have calculated the resistance of all of the layers \n")
    print("\n The Overall Resistance is "+ str(R_tot)+ " degC/W \n")

Rcalc()