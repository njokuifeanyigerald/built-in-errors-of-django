from django.shortcuts import render


def home(request):
    context = {

    }
    return render(request, 'app/home.html', context)


def error_404(request, exception):
    return render(request, 'app/404.html')



def error_500(request, *args, **argv):
    return render(request, 'app/500.html', status=500)

        
def error_403(request, exception):

        return render(request,'app/403.html')

def error_400(request,  exception):
        return render(request,'app/400.html')  