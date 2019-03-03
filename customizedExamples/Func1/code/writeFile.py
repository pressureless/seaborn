import scipy.io as scio
dataFile = "/Users/liyong16/Downloads/pvn_ly.mat"
data = scio.loadmat(dataFile)


f = open("/Users/liyong16/Downloads/data_gE.txt", 'a+')
f.write("Value;Type;Height\n")
gE= data['gE']
for i in range(len(gE)):
    f.write(str(gE[i][0]) + ";gE;High\n")
    f.write(str(gE[i][1]) + ";gE;Low\n")

f.close()

f = open("/Users/liyong16/Downloads/data_Cp.txt", 'a+')
f.write("Value;Type;Height\n")
Cp= data['Cp']
for i in range(len(Cp)):
    f.write(str(Cp[i][0]) + ";Cp;High\n")
    f.write(str(Cp[i][1]) + ";Cp;Low\n")
f.close()

f = open("/Users/liyong16/Downloads/data_locE.txt", 'a+')
f.write("Value;Type;Height\n")
locE= data['locE']
for i in range(len(locE)):
    f.write(str(locE[i][0]) + ";locE;High\n")
    f.write(str(locE[i][1]) + ";locE;Low\n")
f.close()

f = open("/Users/liyong16/Downloads/data_Lp.txt", 'a+')
f.write("Value;Type;Height\n")
Lp= data['Lp']
for i in range(len(Lp)):
    f.write(str(Lp[i][0]) + ";Lp;High\n")
    f.write(str(Lp[i][1]) + ";Lp;Low\n")
f.close()

