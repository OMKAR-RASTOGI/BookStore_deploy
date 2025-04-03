from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    user_role = request.user.role  # Get user role from the CustomUser model
    return render(request, 'home.html', {'user_role': user_role})
