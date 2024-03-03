from django.shortcuts import render, redirect

# Create your views here.
def addandlook_view(request):
    return render(request, 'addandlook.html')

from .forms import HouseForm

def addhouse_view(request):
    if request.method == 'POST':
        form = HouseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the homepage
    else:
        form = HouseForm()
    return render(request, 'addhouse.html', {'form': form})
