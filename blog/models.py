from django.db import models
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.
#cause we want to use this class in post we must declare this before class post
class Category(models.Model) :
    name = models.CharField(max_length=255)  

    def __str__(self):
        return self.name
    
class post(models.Model):
    image = models.ImageField(upload_to='blog',default='blog/default.jpg')
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length = 255)
    content = models.TextField()
    #tag
    category = models.ManyToManyField(Category)
    conted_vies = models.IntegerField(default = 0)
    status = models.BooleanField(default = False)
    published_date = models.DateTimeField(auto_now = True)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)
    #slug = models.SlugField(default='', editable=False,  max_length=160)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
    related_query_name='hit_count_generic_relation')

    def save(self, *args, **kwargs):
        super(post, self).save(*args, **kwargs)
 
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


    def __str__(self):
        return "{}-{}".format(self.title,self.id)


class Meta:
    ordering = ['created_date']
    #verbose_name = ['Post']# change name in show