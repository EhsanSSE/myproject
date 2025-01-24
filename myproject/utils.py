from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.conf import settings

@csrf_exempt
def tinymce_upload(request):
    if request.method == 'POST' and request.FILES.get('file'):
        # Gereftan file az request
        uploaded_file = request.FILES['file']
        # Zakhire file dar media/uploads/
        file_path = default_storage.save(f'uploads/{uploaded_file.name}', uploaded_file)
        # Sakht URL baraye aks
        file_url = f'{settings.MEDIA_URL}{file_path}'
        # Pas dade shodan URL be TinyMCE
        return JsonResponse({'location': file_url})
    return JsonResponse({'error': 'Invalid request'}, status=400)
