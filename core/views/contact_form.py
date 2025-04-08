from django.http import JsonResponse
from django.shortcuts import render
from core.forms import ContactForm
from django.contrib.auth.decorators import login_required

@login_required
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Return a JSON response for successful submission
            return JsonResponse({
                'success': True,
                'title': "Fantastico!",
                'success_message': "Abbiamo ricevuto il tuo messaggio.<br>Ti risponderemo appena torniamo dalle Maldive,<br>nel mentre fai qualcosa di divertente.",
                'redirect_url': '/'  # Replace with your desired URL
            })
        else:
             # Return validation errors as JSON
            errors = {field: error.get_json_data() for field, error in form.errors.items()}
            return JsonResponse({'success': False, 'errors': errors}, status=400)
            
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})