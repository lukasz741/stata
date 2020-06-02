import csv
import statistics

with open("spx_d (2).csv", 'r') as csv_file:
    csv_reader = csv.reader(csv_file , delimiter=',')
    csv_file.readline()

    i=0
    lista_Stopa_zwrotu_dzienna_K3 = []
    lista_Stopa_zwrotu_dzienna_K4 = []
    lista_Stopa_zwrotu_dzienna_K1 = []

    lista_wolumen_K3 = []
    lista_wolumen_K4 = []
    lista_wolumen_K1 = []
    for line in csv_reader:
        if i in range(0,64):
            Stopa_zwrotu_dzienna_K3 = ((float(line[4]) - float(line[1])) / float(line[1])*100)
            lista_Stopa_zwrotu_dzienna_K3.append(Stopa_zwrotu_dzienna_K3)
            wolumen_K3 = int(line[5])
            lista_wolumen_K3.append(wolumen_K3)
            i += 1
        elif i in range(64,128):
            Stopa_zwrotu_dzienna_K4 = ((float(line[4]) - float(line[1])) / float(line[1])*100)
            lista_Stopa_zwrotu_dzienna_K4.append(Stopa_zwrotu_dzienna_K4)
            wolumen_K4 = int(line[5])
            lista_wolumen_K4.append(wolumen_K4)
            i += 1
        else:
            Stopa_zwrotu_dzienna_K1 = ((float(line[4]) - float(line[1])) / float(line[1])* 100)
            lista_Stopa_zwrotu_dzienna_K1.append(Stopa_zwrotu_dzienna_K1)
            wolumen_K1 = int(line[5])
            lista_wolumen_K1.append(wolumen_K1)
            i += 1


with open("wartosci_dla_analizy_1_SP500.txt", 'w') as f:
    #K3
    f.write("stopy zwrotu w K3:\nmin: ")
    f.write(str((min(lista_Stopa_zwrotu_dzienna_K3))))
    f.write("\nmax: ")
    f.write(str((max(lista_Stopa_zwrotu_dzienna_K3))))
    f.write("\nsrednia: ")
    f.write(str((sum(lista_Stopa_zwrotu_dzienna_K3)/64)))
    f.write("\nodchylenie standardowe: ")
    f.write(str((statistics.stdev(lista_Stopa_zwrotu_dzienna_K3))))
    f.write("\n\n")

    #K4
    f.write("stopy zwrotu w K4:\nmin: ")
    f.write(str(min(lista_Stopa_zwrotu_dzienna_K4)))
    f.write("\nmax: ")
    f.write(str(max(lista_Stopa_zwrotu_dzienna_K4)))
    f.write("\nsrednia: ")
    f.write(str(sum(lista_Stopa_zwrotu_dzienna_K4)/64))
    f.write("\nodchylenie standardowe: ")
    f.write(str(statistics.stdev(lista_Stopa_zwrotu_dzienna_K4)))
    f.write("\n\n")

    #K1
    f.write("stopy zwrotu w K1:\n")
    f.write("min: ")
    f.write(str(min(lista_Stopa_zwrotu_dzienna_K1)))
    f.write("\nmax: ")
    f.write(str(max(lista_Stopa_zwrotu_dzienna_K1)))
    f.write("\nsrednia: ")
    f.write(str(sum(lista_Stopa_zwrotu_dzienna_K1)/62))
    f.write("\nodchylenie standardowe: ")
    f.write(str(statistics.stdev(lista_Stopa_zwrotu_dzienna_K1)))









