from django.db import models

class Contact(models.Model):
    description_text = models.CharField(max_length=200,blank=True, default='')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=20,blank=True, default='')
    state_of_domicile = models.CharField(max_length=2)
    group_code_id = models.CharField(max_length=20,blank=True, default='')
    group_name = models.CharField(max_length=100,blank=True, default='')
    co_code = models.CharField(max_length=20,blank=True, default='')
    short_company_name = models.CharField(max_length=200,blank=True, default='')
    email = models.EmailField(blank=True, default='')
    fein = models.CharField(max_length=20,blank=True, default='')
    request_filing = models.BooleanField()
    class Meta:
        verbose_name_plural = 'contacts'
    @property
    def full_name(self):
        return u'%s %s' % (self.first_name, self.last_name)

    def __unicode__(self):
        return u'%s' % self.full_name
