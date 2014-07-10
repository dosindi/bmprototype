from django.shortcuts import render_to_response  
from django.core.context_processors import csrf  
from django.views.decorators.csrf import csrf_exempt  
from django.http import HttpResponse  
from django import forms  
import os  
import sqlite3  
import json  
BASE_DIR = os.path.dirname(os.path.realpath(__file__))  
MEDIA_ROOT = os.path.join(os.environ['OPENSHIFT_DATA_DIR'], 'media')  
STATIC_ROOT = os.path.join(BASE_DIR, '..', 'static')  
class UploadFileForm(forms.Form):  
    title = forms.CharField(max_length=50)  
    file  = forms.FileField()  
def home(request):  
    return render_to_response('home/home.html')  
@csrf_exempt  
def upload_file(request):  
    cont = ""  
    conn = sqlite3.connect(os.path.join(os.environ['OPENSHIFT_DATA_DIR'], 'sqlite3.db'))  
    cursor = conn.cursor()  
    count = 0  
    for upfile in request.FILES.getlist('upload'):  
        for chunk in upfile.chunks():  
            cont = str(chunk)[2:][:-1]  
    val = []  
    val = str(cont).split("n")  
    conn = sqlite3.connect(os.path.join(os.environ['OPENSHIFT_DATA_DIR'], 'sqlite3.db'))  
    cursor = conn.cursor()  
    for el in val:  
        if el.find('r') > -1 :  
            cmd = "INSERT INTO transactiontb VALUES ('" + str(el)[:-3] + "')"  
        else:  
            cmd = "INSERT INTO transactiontb VALUES ('" + str(el) + "')"  
        cursor.execute(cmd)  
    conn.commit()  
    cmd = "SELECT * FROM transactiontb"  
    cursor = conn.cursor()  
    count = 0  
    lines = []  
    for res in cursor.execute(cmd):  
        lines.insert(count,str(res)[2:][:-3])  
        count = count + 1  
    conn.close()  
    return HttpResponse(json.dumps(lines))  
def create_table(request):  
    conn = sqlite3.connect(os.path.join(os.environ['OPENSHIFT_DATA_DIR'], 'sqlite3.db'))  
    cursor = conn.cursor()  
    cmd = "CREATE TABLE transactiontb(amt text)"  
    cursor.execute(cmd)  
    conn.commit()  
    conn.close()  
    return HttpResponse("success") 