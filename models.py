from django.db import models
from dateutil.relativedelta import *
import calendar

TODAY = datetime.date.today()
MONTH = TODAY.month
YEAR = TODAY.year

class Job(models.Model):

	STATUS_CHOICES = (('D','Draft'),('P','Published'))
	LOCATION_CHOICES = (('ALL','All'), ('ATI','Atikokan'), ('DRY','Dryden'),('FFR','Fort Frances'),('KEN','Kenora'),('RLK','Red Lake'),('SLK','Sioux Lookout'))
	TERM_CHOICES = (('PT','Part-Time'),('FT','Full-Time'),('CF','Contact Full-Time'),('CP','Contract Part-Time'))

	status = models.CharField(max_length='1',choices=STATUS_CHOICES)
	publish_date = models.DateField()
	closing_date = models.DateField()
	title = models.CharField(max_length=64, blank=False)
	location = models.CharField(max_length=3,choices=LOCATION_CHOICES)
	term = models.CharField(max_length=2,choices=TERM_CHOICES)
	contract_length = models.IntegerField(max_length=2, help_text='Length specified in months')
	extension_possible = models.BooleanField()
	union = models.BooleanField()
	positions_available = models.IntegerField()
	qualifications = models.TextField()
	service = models.CharField(max_length=64)

	def clean(self):
		if self.term == 'CF' or self.term == 'CP' and self.contract_length is None:
			raise ValidationError('Contact positions need a contract length specified in number of months.')
		if self.status == 'P' and self.publish_date is None:
			self.publish_date = TODAY
		if self.closing_date is None:
			pass

	class Meta:
		abstract = True

class SalariedJob(Job):
	scale_start = models.DecimalField(max_length=8)
	scale_end = models.DecimalField(max_length=8)
	hours = models.DecimalField(max_length=4)

class NonSalariedJob(Job):
	wage = models.DecimalField(max_length=4)