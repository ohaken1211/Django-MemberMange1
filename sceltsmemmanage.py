import django
import os
import sys

sys.path.append(r'c:\Users\Kentaro\Desktop\Scelts\MemberManage\scelts_manager')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scelts_manager.settings")

#from django.core.management import execute_from_command_line
#execute_from_command_line(sys.argv)

django.setup()
from manager.models import Person
Person.objects.filter(sex = "0").delete()
Person.objects.filter(sex = "9").delete()

import csv
reader = csv.reader(open("member_list.csv", encoding="utf-8"))
 
for r in reader:
    p = Person()
    p.name = r[0]
    p.sex = r[1]
    p.grade = r[2]
    p.instrument = r[3]
    p.save()
