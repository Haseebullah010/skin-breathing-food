from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.files.storage import default_storage
from django.http import HttpResponse, JsonResponse
import torch
import json
import os
from django.shortcuts import render

import requests
import json
import io

from django.contrib.staticfiles import finders

def home(request):

    if request.method == "POST":
        print ("post method")
        value3 = request.POST.get("Option3")
        print ("value3",value3)
        if value3=="1":
            return render(request,"home.html")
        if value3=="2":
            return render(request,"home2.html")
        if value3=="3":
            return render(request,"home3.html")        

    return render(request,"index.html")


def index(request):

    return render(request,"index.html")

class Skin_Condition(APIView):
    print ("in class")
    def post(self, request, format=None):
        print ("in function of class")

        # file = request.data.get('fileup')
        # print ("file",file)
        
        file = request.data.get('fileup')
        staticPrefix = "static"
        filename = str(file)
        print ("filename",filename)

        filepath = 'static/' + filename
        with default_storage.open(filepath, 'wb+') as destination:
            for chunk in file.chunks():
                # print ("chunk",chunk)
                destination.write(chunk)
                print ("desdestination",destination )

        api_url = "https://37csi2gzcb.execute-api.ap-southeast-1.amazonaws.com/v1"
        headers =  {"Content-Type":"image/jpg"}
        f = open(filepath , 'rb')
        photo = f.read()
        f.close()
        response = requests.post(api_url, data=photo, headers=headers)
        print(response.json())
        data=response.json()
        data =json.loads(data['body'])
        if len(data['CustomLabels']) > 0:
            name_confidence = []
            for x in data['CustomLabels']:
                name_confidence.append({
                    "name":x['Name'],
                    "confidence": round(x['Confidence'],2)
                })
            return render(request,"home.html",{'context':name_confidence})
        else:
            print("No data found")
            return render(request,"home.html",{'context1':"No Disease Found"})

        return render(request,"home.html")

class Food_Analysis(APIView):
    print ("in class")
    def post(self, request, format=None):
        print ("in function of class")

        # file = request.data.get('fileup')
        # print ("file",file)
        
        file = request.data.get('fileup')
        staticPrefix = "static"
        filename = str(file)
        print ("filename",filename)

        filepath = 'static/' + filename
        with default_storage.open(filepath, 'wb+') as destination:
            for chunk in file.chunks():
                # print ("chunk",chunk)
                destination.write(chunk)
                print ("desdestination",destination )

        api_url = "https://uerehl81gi.execute-api.ap-southeast-1.amazonaws.com/dev"
        headers =  {"Content-Type":"image/jpg"}
        f = open(filepath , 'rb')
        photo = f.read()
        f.close()
        response = requests.post(api_url, data=photo, headers=headers)
        print(response.json())
        data=response.json()
        data =json.loads(data['body'])
        if len(data['CustomLabels']) > 0:
            name_confidence = []
            for x in data['CustomLabels']:
                name_confidence.append({
                    "name":x['Name'],
                    "confidence": round(x['Confidence'],2)
                })
            return render(request,"home2.html",{'context':name_confidence})
        else:
            print("No data found")
            return render(request,"home2.html",{'context1':"No Food Found"})

        return render(request,"home.html")



