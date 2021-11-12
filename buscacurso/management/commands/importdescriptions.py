# -*- coding: utf-8 -*-

from glob import glob
import json
import os
import time
import unicodedata
import base64

from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from django.db import transaction

from tcc import settings

from buscacurso.models import Courses
from buscacurso.models import CoursesInstitution
from buscacurso.models import Institution
from buscacurso.models import Maintainer

from buscacurso.utils.functions import Status, clean_duration, cleaning_cnpj, only_numerics, clean_ies_name, find_code 


class Command(BaseCommand):

    verbose = False
    help = 'Import e-MEC data for database Buscacurso.'

    def add_arguments(self, parser):
        
        parser.add_argument(
                '--uf',
                dest='uf',
                type=str,
                help='Import emec data from json file with name of UF'
        )
        
        parser.add_argument(
                '--v',
                '--verbose',
                 action='store_true',
                 dest='verbose',
                 default=False,
                 help='Show more details about imports emec data.'
        )
    
        
    def write(self, msg, force_verbose=False, status=Status.success):
            """
            Show message green color in console.
            
            Args:
                msg (string)             : the message to be shown in console.
                force_verbose (boolean)  : flag that force show message even that `verbose` is False.
            """
    
            if self.verbose or force_verbose:                
                self.stdout.write(msg, style_func=lambda x: str(status + '%s' + Status.none) % str(x) )
                
                
    def import_data_from_path(self):

        filename = os.path.join(settings.BASE_DIR, 'buscacurso/descriptiondata/',  'data.json')
        
        if os.path.exists(filename):
            
            self.write('Starting emec data import from json file', status=Status.info)
        
            # open file and read json                
            with open(filename, encoding='utf-8-sig') as data_file:
                data = json.loads(data_file.read())
                
                print (data)

            # start time            
            start = time.time()
            
            #with transaction.atomic():
            unavailable = "Descrição Indisponivel"
            course_clean = Courses.objects.all()
            for course in course_clean.iterator():
                course.description = unavailable
                course.save()

            
            courses_list = data ["cursosP"]
            coursesnames=[]
            text= "custom description"
            course_set = Courses.objects.all()

            for course in course_set.iterator():
                for curso in courses_list:    
                    cursosD = curso['cursosd'] 
                    descri = curso["descricao"]      
                    if course.name == cursosD:    
                        course.description = descri
                        course.save()
                        break
                            

            '''    for curso in courses_list:

                    cursosD = curso['cursosd'] 
                    descri = curso["descricao"]
                    for course in course_set.iterator():
                        if course.name == cursosD:
                            course.description = descri
                            course.save()
                        

                #for course in course_set.iterator():
                    #coursesnames.append(course.description)
                #print(coursesnames)                  

                ##course_set = Courses.objects.all()
            
                #for course in course_set.iterator():
                #    print(course.name)
                    #if
                #        course.description = text
                 #       course.save()
                    
                #for course in course_set.iterator():
                 #   coursesnames.append(course.description)
                
               # print(coursesnames)
                ''' 
                            
            elapsed = time.time() - start
            
        else:
            self.write('Json file for UF informed not found, please check in the folder', True, status=Status.error)
    
    
    def import_data_from_uf(self):
        """
        Import emec data from all json files in the folder
        """
        
        self.write('Starting emec data import from all json files in the folder\n', status=Status.info)
        
        path = os.path.join(settings.BASE_DIR, 'buscacurso/descriptiondata/')
        #print("path:", path)
        for filename in glob('data.json'):
            uf = filename.replace(path, '').replace('.json', '')
            self.import_data_from_uf(uf)
    
    
    def handle(self, *args, **options):
        self.verbose = options['verbose']
        self.import_data_from_path()
                    
        self.write('Finish run import description data!', force_verbose=True)






        
        
