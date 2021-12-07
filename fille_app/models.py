from django.db import models

class File(models.Model):
  file = models.FileField(blank=False, null=False, upload_to='images/')
  remark = models.CharField(max_length=20)
  timestamp = models.DateTimeField(auto_now_add=True)