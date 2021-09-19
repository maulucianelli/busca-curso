import csv
import os

from django.core.management.base import BaseCommand, CommandError


#ajustar modelo
from buscacurso.models import Curso, Curso_teste

class Command(BaseCommand):
    """
    """ 

    def __init__(self, *args, **kwargs):
        self.log=""
        self.file_csv = None
        self.file_erros_output_csv = None
        self.headers_required = {
            #inserir nome dos headers agui
            "codigo_curso",
            "codigo_ies",
            "sigla_ies",
            "nome_ies"
        }
        super().__init__(*args, **kwargs)

    def add_arguments(self, parser):
        # Required Argumnet
        parser.add_argument(
            "-f", "--file", type = str, help="Define a file to read."
        )
        # Optional Argument
        parser.add_argument(
            "-o",
            "--csv_err_output",
            type=str,
            default = "error.csv",
            help = "file to save errors",
        )
        
    def handle(self, *args, **kwargs):
        self.file_csv = kwargs["file"]
        self.file_error_output_csv = kwargs["csv_err_output"]
        #custom array
        courses_list = []

        try: 
            with open(self.file_csv) as file:
                csv_reader = csv.reader(
                    file, delimiter= ",", quotechar='"'
                )
                csv_headers = next(csv_reader)

                headers = {i: csv_headers.index(i) for i in csv_headers}


                if not self.validate_required_headers(headers):
                    return
                
                for row in csv_reader:
                    row[0]
                    data = {
                        #colunas
                        #codigo_curso;codigo_ies;sigla_ies;nome_ies
                        "codigo_curso": row[headers["codigo_curso"]],
                        "codigo_ies": row[headers["codigo_ies"]],
                        "sigla_ies": row[headers["sigla_ies"]],
                        "nome_ies": row[headers["nome_ies"]],
                    }





                    #ALTERAR
                    curso = Curso_teste(codigo_curso=codigo_curso,codigo_ies=codigo_ies,sigla_ies=sigla_ies,nome_ies=nome_ies)
                    curso.save()

                    curso = Curso_teste(**data)
                    
                    courses_list.append(curso)
                
                Curso_teste.objects.bulk_create(courses_list)

            self.save_errors_into_csv()
            
        except FileNotFoundError:
            self.stdout.write(
                self.style.ERROR(f"File not Found: {self.file_csv}")
            )







    def validate_required_headers(self, headers):
        """






        """
        if all(column in headers for column in self.headers_required):
            return True

        self.stdout.write(
            self.style.ERROR(
                "The CSV required the columns: {}".format(
                    self.headers_required
                )
            )
        )
        return False

    def save_errors_into_csv(self):
        with open(self.file_error_output_csv, "w+") as file:
            file.write(self.log)





