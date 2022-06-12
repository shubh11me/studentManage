from msilib.schema import Class
from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
import datetime
from .models import student
from .serializers import *
from rest_framework.decorators import api_view


def generate_id(last_id,stData,seria,model,key):
    x = datetime.datetime.now()
    gen = x.strftime("%m")+x.strftime("%Y")+x.strftime("%H")+x.strftime("%f")
    new_id = "Cliqstud"+str(last_id)+gen
    Mydata = model.objects.get(id=last_id)
    stData[key]=new_id

    AllDataSeri = seria(Mydata, data=stData)
    if AllDataSeri.is_valid():
        AllDataSeri.save()
        return {"status":True,"new_data":stData}
    else:
        return  {"status":False}
   #  return new_id


@api_view(['GET', 'POST', 'DELETE'])
def students(request, pk=None):
    if request.method == 'POST':
        stData = JSONParser().parse(request)
        stSeri = studSeri(data=stData)
        if stSeri.is_valid():
            stSeri.save()
            
            myLast = (student.objects.last()).id
            new_id = generate_id(myLast,stData,studSeri,student,'student_id')
            return JsonResponse({"data":new_id['new_data']}, status=status.HTTP_201_CREATED)

    elif request.method == 'GET':
        if pk is not None:
            try:
                AllData = student.objects.get(pk=pk)
                AllDataSeri = studSeri(AllData, many=False)
                return JsonResponse(AllDataSeri.data, status=status.HTTP_200_OK, safe=False)
            except:
                return JsonResponse({"s": "Nodata found", "cs": pk, }, safe=False)

        else:
            AllData = student.objects.all()
            AllDataSeri = studSeri(AllData, many=True)
            return JsonResponse(AllDataSeri.data, status=status.HTTP_200_OK, safe=False)


def get_students(id):
    try:
        AllData = student.objects.get(pk=id)
        AllDataSeri = studSeri(AllData, many=False)
        return AllDataSeri.data
    except:
        return {"s": "Nodata found", "cs": id, }


def studentName(request, name=None):
    if request.method == 'GET':
        Mydata = student.objects.get(name=name)
        AllDataSeri = studSeri(Mydata, many=False)
        serData = AllDataSeri.data
        gotData = get_students(AllDataSeri.data['id'])
        serData['new'] = gotData
        return JsonResponse(serData, status=status.HTTP_200_OK, safe=False)


@api_view(['PUT'])
def updateStudent(request, pk):
    if request.method == 'PUT':
        Mydata = student.objects.get(student_id=pk)
        stData = JSONParser().parse(request)
        AllDataSeri = studSeri(Mydata, data=stData)
        if AllDataSeri.is_valid():
            AllDataSeri.save()
            return JsonResponse(stData, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({'stData': stData})


# api for teacher with functions

# @api_view(['GET', 'POST','PUT'])
# def teachBanv(request, pk=None):
#     if request.method == 'POST':
#         cdata=JSONParser().parse(request)
        
#         sdata=teachSeri(data=cdata)
#         if sdata.is_valid():
#             sdata.save()
#             return JsonResponse(cdata,status=status.HTTP_201_CREATED, safe=False)
#     elif request.method == 'GET':
#         if pk is not None:
#             data=teacher.objects.get(id=pk)
#             sdata=teachSeri(data,many=False)
#             return JsonResponse(sdata.data,status=status.HTTP_200_OK, safe=False)
#         else:
#             data=teacher.objects.all()
#             sdata=teachSeri(data,many=True)
#             return JsonResponse(sdata.data,status=status.HTTP_200_OK, safe=False)
#     elif request.method == 'PUT':
#         if pk is not None:
#             reqData=JSONParser().parse(request)
#             data=teacher.objects.get(id=pk)
#             sdata=teachSeri(data,data=reqData)
#             if sdata.is_valid():
#                 sdata.save()
#                 return JsonResponse(sdata.data,status=status.HTTP_201_CREATED, safe=False)       



# api for teacher with class and APIVIew
from rest_framework.views import APIView

# class Student(APIView):
#     def post(self, request):
