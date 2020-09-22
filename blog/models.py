from django.db import models

# Create your models here.
class Blog(models.Model):

    post_id = models.AutoField(primary_key=True)
    tittle = models.CharField(max_length = 500)
    head0 = models.CharField(max_length = 500)
    chead0 = models.CharField(max_length = 5000)
    head1 = models.CharField(max_length = 500)
    chead1 = models.CharField(max_length = 5000)
    head2 = models.CharField(max_length=500)
    chead2 = models.CharField(max_length = 5000)
    pub_date = models.DateField()
    thumnail = models.ImageField(upload_to="blog/imag")
    #objects = models.Manager()
    def __str__(self):
        return self.tittle