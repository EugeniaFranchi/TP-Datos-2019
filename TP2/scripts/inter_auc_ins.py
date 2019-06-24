import csv
import sys



def intercalar(entrada_1, entrada_2, salida):
    """
    entrada1 es el archivo que contiene las predicciones de installs
    entrada2 es el arch que tiene las preds de auctions
    salida es el nombre del archivo de salida
    """
    with open(entrada_1) as f, open(entrada_2) as f2, open(salida,"w") as s:
        lector1 = csv.reader(f)
        lector2 = csv.reader(f2)
        escritor = csv.writer(s)

        escritor.writerow(next(lector1))
        next(lector2)

        for linea in lector1:
            usuario1 = linea[0]
            valor1 = linea[1]

            linea2 = next(lector2)
            usuario2 = linea2[0]
            valor2 = linea2[1]

            escritor.writerow([usuario + "_sc", valor1])
            escritor.writerow([usuario2 + "_st", valor2])


intercalar(sys.argv[1], sys.argv[2], sys.argv[3])

# Ejemplo de uso desde la terminal:
#    python3 inter_auc_ins.py preds_installs.csv preds_auctions.csv submit_kaggle.csv
