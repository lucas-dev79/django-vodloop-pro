from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views import View
from django.contrib.auth.forms import UserCreationForm


class PodcastLoginView(LoginView):
    template_name = "accounts/login.html"

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            login(request, form.get_user())
            return JsonResponse({'success': True, 'redirect_url': '/'})  # Replace '/' with your home page URL
        else:
            errors = {field: error.get_json_data() for field, error in form.errors.items()}
            return JsonResponse({'success': False, 'errors': errors}, status=400)

def logout_view(request):
    logout(request)
    return redirect('login')

class RegistrationView(View):
    template_name = "accounts/register.html"

    def get(self, request):
        form = UserCreationForm()
        return render(request, self.template_name, context={'form': form})
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return JsonResponse({
                'success': True,
                'title': "Registration Successful!",
                'success_message': "Your account has been created successfully. Please login.",
                'redirect_url': '/auth/login/'  # Replace with your desired URL
            })
        else:
            # Return validation errors as JSON
            errors = {field: error.get_json_data() for field, error in form.errors.items()}
            return JsonResponse({'success': False, 'errors': errors}, status=400)



