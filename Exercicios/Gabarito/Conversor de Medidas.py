#Programa que lê um valor em metros e o exibe convertido em centimetros e milimetros.

medida=float(input("uma distância em metros: "))

cm= medida*100
mm= medida*1000

print(f'A medida de {medida}m corresponde a {cm:.0f}cm e {mm:.0f}mm.')