import csv


def intercalar(entrada):

    with open(entrada) as f, open("mi_target_2.csv","w") as s:
        lector = csv.reader(f)
        escritor = csv.writer(s)

        escritor.writerow(next(lector))

        for linea in lector:
            usuario = linea[0]
            valor = linea[1]

            escritor.writerow([usuario + "_sc", valor])
            escritor.writerow([usuario + "_st", valor])


intercalar("resultados_2.csv")
