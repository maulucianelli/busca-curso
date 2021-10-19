from emec.emec import Institution
import csv
import json

# instancia com o codigo da ies no mec
ies = Institution(72)

# faz o parse de todos os dados da instituicao
ies.parse()

# escreve um arquivo json com os dados coletados
ies.write_json('emec.json')

# instancia com o codigo da ies no mec
#filename = 'codigos_ies.CSV'#
#
#with open (filename, 'r') as csvfile:
#    datareader =csv.reader(csvfile)
#    for row in datareader:
#        print(csvfile.readlines())
