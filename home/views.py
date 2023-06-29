from multiprocessing import context
from django.http import QueryDict
from django.shortcuts import render, HttpResponse
from django.core.files.storage import FileSystemStorage
import pickle
import tensorflow as tf
from tensorflow import keras 
import joblib
import numpy as np
from keras.preprocessing import image
'''tf.saved_model.LoadOptions(
    allow_partial_checkpoint=False,
    experimental_io_device=None,
    experimental_skip_checkpoint=False
)
lr=joblib.load('./models/model.pkl')
'''

#importing libraries
# Create your views here.
def index(request):
    context= {
        "variable1":"this is sent",
        "variable2":"this is unsent"
    }
    return render(request,'index.html',context)
    # return HttpResponse("index")
'''
def SigntoText(request):
    return render(request,'signupload.html')
'''

def TexttoSign(request):
    a=request.GET
    print(a)
    context={
        "var": a
    }
    return render(request,'textupload.html',context)


def AboutUs(request):
    return render(request,'about.html')

def details(request):
    return render(request,'details.html')

def Contact(request):
    return render(request,'contact.html')



def SigntoText(request):
    
    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)     
        # load saved model
        #with open('model_pkl' , 'rb') as f:
         #   lr = pickle.load(f)
        return render(request, 'signupload.html', {'file_url': file_url})
    return render(request, 'signupload.html')


