import csv


def mezclar(archivo, archivo2):
    with open(archivo) as f, open(archivo2) as f2, open("merge.csv","w") as s:
                lector1 = csv.reader(f)
                lector2 = csv.reader(f2)
                escritor = csv.writer(s)

                escritor.writerow(next(lector1))
                next(lector2)

                for linea in lector1:
                    linea2 = next(lector2)

                    escritor.writerow([linea[0], min(linea[1], linea2[1])])



mezclar("mi_target.csv", "mi_target_2.csv")
