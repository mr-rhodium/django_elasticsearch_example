from django.shortcuts import render, HttpResponse
from django.views import View
from buildings.documents import HouseDocument

class HouseViews(View):
    def get(self, request, *args, **kwargs):
        out = HouseDocument.search().query("match", roof="BR")
        print(out)
        for hit in out:
            print(
                "Car name : {}, description {}".format(hit.name, hit.roof)
            )
        
        return HttpResponse([hit for hit in out])