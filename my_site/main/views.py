from django.shortcuts import render

# Create your views here.
def main(request):
   return render(request, 'main/index.html',{'title':'передача данных  как  пропсы  на рекате'})

def about(request):
   data ={
      'title':''
   }
   return render(request, 'main/aboutMe.html',{'title':'передача данных  как  пропсы  на рекате'})