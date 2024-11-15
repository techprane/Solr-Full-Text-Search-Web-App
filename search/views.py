import pysolr
from django.shortcuts import render
from django.conf import settings

# Create your views here.
def search(request):
    # query = request.GET.get('q', '')
    query = "msg:Hello"
    print(f"Erroorrrr! {query}")
    results = []
    if query:
        solr = pysolr.Solr(settings.SOLR_URL, always_commit=True)
        print(f"Shout if error occur like Joe do say: {query}")
        # results = solr.search(query)
    return render(request, 'search/search.html', {'results': results, 'query': query})
