import csv


def quitar(archivo):
    with open(archivo) as i, open("final.csv", 'w') as s:
        entrada = csv.reader(i)
        salida = csv.writer(s)

        next(entrada)
        k = 0
        for linea in entrada:
            if k % 2 == 0:
                salida.writerow([linea[0][:-3]])
            k += 1


quitar("target_competencia_ids.csv")
