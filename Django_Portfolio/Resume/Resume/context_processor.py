from django.contrib.auth.models import User

def project_context(request):
    context = {
        'jealous': User.objects.first(),
        
    }
    
    return context