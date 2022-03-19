from django.db import models


class Url(models.Model):

    url = models.URLField(max_length=2038)
    url_hash = models.PositiveIntegerField(db_index=True)
    code = models.CharField(max_length=9)
    code_hash = models.PositiveIntegerField(db_index=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __format__(self, format_spec):
        return '{} - {}'.format(self.url, self.code)
