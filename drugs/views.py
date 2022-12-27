import os
import shutil
from pyke import knowledge_engine
from pyke import krb_traceback

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseServerError,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

file =  os.path.join( os.path.abspath('') , 'drugs','facts.kfb')
delDir =  os.path.join( os.path.abspath('') , 'drugs','compiled_krb')

print(file)
@csrf_exempt 
def getDrug(request):
  print(request.body)
  json_data = json.loads(request.body)
  
  try:
    drug = None
    cold = json_data['cold']
    headache = json_data['headache']
    highTemperature = json_data['highTemperature']
    sneezing = json_data['sneezing']
    musclePain = json_data['musclePain']
    soreThroat = json_data['soreThroat']
    dizziness = json_data['dizziness']
    sinuses = json_data['sinuses']
    sideEffects = json_data['sideEffects']
    age = json_data['age']
    print(1)
    with open(file, 'w') as f:
    # Write multiple lines of text to the file
      # f.write('diagnose(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)\n' %cold %headache %highTemperature %sneezing %musclePain %soreThroat %dizziness %sinuses %sideEffects %age )
      f.write('diagnose(%s' %cold)
      f.write(', %s' %headache)
      f.write(', %s' %highTemperature)
      f.write(', %s' %sneezing)
      f.write(', %s' %musclePain)
      f.write(', %s' %soreThroat)
      f.write(', %s' %dizziness)
      f.write(', %s' %sinuses)
      f.write(', %s' %sideEffects)
      f.write(', %s)\n' %age)
    engine = knowledge_engine.engine(__file__)
    engine.reset()      # Allows us to run tests multiple times.
    engine.activate('bc_simple_rules')
    with engine.prove_goal('bc_simple_rules.get_drug($drug)') as gen: #STUDENTS: you will need to edit this line
      # print(gen)
      for vars, plan in gen:
        print("You should take: %s" % (vars['drug']))
        drug = vars['drug']
    # shutil.rmtree(delDir)

  except Exception as e:
    print(e)
    res =  JsonResponse({
    'ok' : False,
    'status' : '400',
    'message' : 'failed'
    })
    res.status_code = 400
    return res
  res =  JsonResponse({
    'ok' : True,
    'status' : '200',
    'message' : 'success',
    'data' : drug
  })
  res.status_code = 200
  return res
