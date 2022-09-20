from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponse ,JsonResponse
from .serializers import PageSerializer
from .models import Page
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
# def get_pages(request):
#     pages=[
#         {"name": "Nike" , "website": "Nike.com
# " , "stars": "5"},
#         {"name": "Adidas" , "website": "Adidas.com" , "stars": "5"}
#     ]
#     return render(request,'pages/pages.html',{'pages':pages})


def get_pages(request):
    # query set
    pages=Page.objects.all()
    return HttpResponse(pages)
    return render(request,'pages/pages.html',{'pages':pages})


########################### old School  ##########################################
def get_all_pages(request):
    # query set to return all data
    pages=Page.objects.all()
    data={"data":list(pages.values('id','name','website','stars'))}
    return JsonResponse(data)
    return render(request,'pages/pages.html',{'pages':pages})



def get_page(request,page_id):
    # query set to return one data using id
    page=Page.objects.get(pk=page_id)
    # to return a json file
    data={
        'name':page.name,
        'website':page.website,
        'stars':page.stars
    }
    return JsonResponse(data)
    # return HttpResponse(page)
    
##############################################################################################
################################## new school  ###############################################

# show the all of data
class PageView(APIView):
    def get_pages(self,request):
        pages=Page.objects.all()
        data=PageSerializer(pages,many=True).data
        return Response(data)
    
   
    
# show the one of data
# class PageView(APIView):
    # def get(self,request,page_id):
    #     page=Page.objects.get(pk=page_id)
    #     # page=get_object_or_404(Page,pk=page_id)
    #     data=PageSerializer(page).data
    #     return Response(data)
    
    def post(self,request):
        serializer=PageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    
    
    