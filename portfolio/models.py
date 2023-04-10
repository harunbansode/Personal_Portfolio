from django.db import models

class Project_details(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    year = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Project_details_table'
        managed = True
        verbose_name = 'Project_details'
        verbose_name_plural = 'Project_details'