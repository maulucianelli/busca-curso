import csv
import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
from django.core.management.base import BaseCommand, CommandError

csvfile = os.path.join(BASE_DIR,'commands\dbtcc.csv')
#ajustar modelo
from buscacurso.models import Curso_teste

with open(csvfile, encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        _, created = Curso_teste.objects.get_or_create(
            codigo_curso=row[0],
            codigo_ies=row[1],
            sigla_ies=row[2],
            nome_ies=row[3],
            )
            # creates a Tuple of the new object or
            # current object and a boolean of if it was created