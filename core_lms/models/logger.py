from django.db import models


class Logger(models.Model):
    user = models.ForeignKey(to='auth.User', null=True,
                             on_delete=models.SET_NULL, related_name='+')
    path = models.CharField(max_length=128)
    create_date = models.DateTimeField(auto_now_add=True)
    execution_time = models.FloatField()
    query_params = models.CharField(max_length=64, null=True)
