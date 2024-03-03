from django.shortcuts import render

# Create your views here.
def homepage_view(request):
    return render(request, 'home.html')

def search_view(request):
    location = request.GET.get('location')
    # Perform search logic using the 'location' value
    # For example, you could query a database for towns around Kiambu
    results = ['Town1', 'Town2', 'Town3']  # Dummy results
    return render(request, 'search_results.html', {'results': results})