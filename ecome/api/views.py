from django.http import JsonResponse

# Create your views here.

def home(request):
    return JsonResponse({'info':'khaledjamal','phone':'23456784434'})