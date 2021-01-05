from django.db import models

# Create your models here.
class category(models.Model):
    id = models.BigAutoField(primary_key=True)
    categories = models.TextField(blank=True, null=True)
    isactive = models.IntegerField(blank=True, null=True)
    #created = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    #modified = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    def get_name(self):
        return u'{0}'.format(self.categories)

    def __str__(self):
        return self.categories

    class Meta:
        db_table = 'table_category'

class subcategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    categories = models.ForeignKey(category, blank=True, null=True, on_delete=models.CASCADE, related_name='category_id')
    subcategory = models.TextField(blank=True, null=True)
    isactive = models.IntegerField(blank=True, null=True)
    #created = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    #modified = models.DateTimeField(auto_now_add=True,blank=True, null=True)



    class Meta:
        db_table = 'table_subcategory'



class savecategorys(models.Model):
    id = models.BigAutoField(primary_key=True)
    categories_id = models.IntegerField(blank=True, null=True)
    subcategory_id = models.IntegerField(blank=True, null=True)
    isactive = models.IntegerField(blank=True, null=True)
    #created = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    #modified = models.DateTimeField(auto_now_add=True,blank=True, null=True)



    class Meta:
        db_table = 'table_savecategorys'


class users(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    isactive = models.SmallIntegerField(default=1)
    create_date = models.DateTimeField(auto_now_add=True,null=True)
    modified = models.DateTimeField(auto_now=True,null=True)



    class Meta:
        db_table = 'table_user'