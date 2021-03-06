from django.db import models

# Create your models here.

class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    # For Python 3.x
    def __str__(self):
        return self.text

    # For Python 2.x
    def __unicode__(self):
        return self.text

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.get_display_text()

    def __unicode__(self):
        return self.get_display_text()

    def get_display_text(self):
        if len(self.text) > 50:
            return self.text[:50] + '...'
        else:
            return self.text