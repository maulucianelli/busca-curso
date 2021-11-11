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

from buscacurso.models import *

from buscacurso.utils.functions import Status, clean_duration, cleaning_cnpj, only_numerics, clean_ies_name, find_code 

class Command(BaseCommand):
    verbose = False
    help = 'Import descriptions.'
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
        """
        Import emec data from json file with name of the UF
        
        Args:
            uf {String}:    uf name for open json file
        """
        
        #filename = os.path.join(settings.BASE_DIR, 'emec/emec_data/output/', uf.upper() + '.json')
        filename = os.path.join(settings.BASE_DIR, 'buscacurso/descriptiondata/',  'data.json')
        #print("filename:", filename)
        # check if file exists
        if os.path.exists(filename):
            
            self.write('Starting description data import from json file', status=Status.info)
        
            # open file and read json                
            with open(filename, encoding='utf-8') as data_file:
                data = json.loads(data_file.read())
                #print (data)

            # start time            
            start = time.time()
            
           # with transaction.atomic():
        coursesnames=[]
        text= "custom description"
        course_set = Courses.objects.all()
        # The `iterator()` method ensures only a few rows are fetched from
        # the database at a time, saving memory.
        for course in course_set.iterator():
            print(course.name)
            course.description = text
            course.save()
            
        for course in course_set.iterator():
            coursesnames.append(course.description)
        print(coursesnames)


        
    def handle(self, *args, **options):
        """
        `importemecdata` command handler.
        Args:
            *args (tuple)     : arguments after `importemecdata` command, ex: `python manage.py importemecdata arg1 arg2 arg3`
            **options (dict)  : dict with options by default option ['verbose'] / (--v) is False
        """

        self.verbose = options['verbose']
        
        if options['uf']:
            self.import_data_from_uf(options['uf'])
        else:
            self.import_data_from_path()
                        
        self.write('Finish run import emec data!', force_verbose=True)
        
        
