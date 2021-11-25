from django.http.response import HttpResponse
from django.shortcuts import render
import pickle
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from os import listdir
from os.path import isfile, join
from playsound import playsound

# Create your views here.
@csrf_exempt
def index(request):
    if request.method == "POST":
        mypath = "/home/ahmadreza/uploaded/"
        # data = json.loads(request.body)
        data = request.body
        
        # print(data.decode('utf8')[0:4])
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        # print(data.decode('utf8')[0:12])
        if "fnfniihhname".encode() in data:
            # print(data.decode('utf8')[24:])
            print("yes")
            import os
            os.system("mv {} {}".format(mypath+onlyfiles[len(onlyfiles)-1],mypath+data.decode('utf8')[24:]))
            return JsonResponse({"true":"true"})
        else:
            t = 0 
            for i in onlyfiles:
                f = open(mypath+i, "rb")
                da = f.read()
                f.close()
                
                if data == da:
                    t+=1    
            if t == 0:
                f = open("/home/ahmadreza/dat.dat","rb")
                integer = pickle.load(f)
                f.close()
                
                f = open("/home/ahmadreza/uploaded/" + str(integer), "wb")
                
                f.write(data)
                f.close()
                
                integer = integer+1
                f = open("/home/ahmadreza/dat.dat","wb")
                pickle.dump((integer),f)
                f.close()
    
    # for playing note.wav file
                playsound('/home/ahmadreza/Downloads/notification.mp3')
                
                return JsonResponse({"true":"true"})
            else:
                return JsonResponse({"true":"false"})
    else:
        return render(request, "./index.html",{})
    
    


def view(request):
    mypath = "/home/ahmadreza/uploaded/"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    # print(onlyfiles)
    # ret = {"zea":{}}
    # z = 0
    # for i in onlyfiles:
    #     print(i)
    #     ret["zea"]["yek"] = str(i)
    #     # ret["hey"] = i
    #     z+= 1
    ret = {"zea":onlyfiles}    
    print(ret)   
    return render(request, "./download.html", ret)

def download(request):
    q = request.GET["q"]
    mypath = "/home/ahmadreza/uploaded/" + q
    response = HttpResponse(content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(q)
    # generate dynamic file content using object pk
    f = open(mypath,"rb")
    dat = f.read()
    response.write(dat)
    return response
    
