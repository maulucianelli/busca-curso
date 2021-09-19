import csv
from os import EX_SOFTWARE

from django.core.management.base import BaseCommand, CommandError
from django.db import DefaultConnectionProxy
#ajustar modelo
from buscacurso.models import Cursos

class Command(BaseCommand):
    """
    1
    1
    1
    1
    1
    1
    1
    1
    1
    1
    1
    1
    1
    1
    1
    1
    1

    1
    1
    """ 

    def __init__(self, *args, **kwargs):
        self.log=""
        self.file_csv = None
        self.file_erros_output_csv = None
        self.headers_required = {
            #inserir nome dos headers agui
            "first_name",
            "last_name",
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
                        "first_name": row[headers["first_name"]],
                        "last_name": row[headers["last_name"]],




                    }





                    #ALTERAR
                    curso = Cursos(nome = first_name, email=email)
                    curso.save()

                    curso = Cursos(**data)
                    
                    customer_list.append(customer)
                
                Customer.objects.bulk_create(customer_list)

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





