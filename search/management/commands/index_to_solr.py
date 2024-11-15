import pysolr
from django.core.management.base import BaseCommand
from search.models import Article
from django.conf import settings

class Command(BaseCommand):
    help = 'Index data to Solr'

    def handle(self, *args, **kwargs):
        solr = pysolr.Solr(settings.SOLR_URL, always_commit=True)
        articles = Article.objects.all()
        
        data = [
            {
                'id': article.id,
                'title': article.title,
                'content': article.content,
                'published_date': article.published_date.isoformat()
            }
            for article in articles
        ]

        solr.add(data)
        self.stdout.write(self.style.SUCCESS('Successfully indexed data to Solr!'))
