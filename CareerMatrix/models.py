from django.db import models

class Role(models.Model):
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.role

class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

class Year(models.Model):
    year = models.CharField(max_length=30)

    def __str__(self):
        return self.year

class Detail(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)

    billable_hours = models.CharField(max_length=20, blank=True, default='')

    general_content = models.TextField(blank=True, default='')

    sub_header_first_section =  models.CharField(max_length=200, blank=True, default='')
    sub_content_first_section = models.TextField(blank=True, default='')

    sub_header_second_section =  models.CharField(max_length=200, blank=True, default='')
    sub_content_second_section = models.TextField(blank=True, default='')

    sub_header_third_section =  models.CharField(max_length=200, blank=True, default='')
    sub_content_third_section = models.TextField(blank=True, default='')

    def __str__(self):
        return self.role.role + ' - ' + self.category.category
