from django.db import models
from django.utils import text
import datetime
import calendar

TODAY = datetime.date.today()
MONTH = TODAY.month
YEAR = TODAY.year
OPEN = datetime.date((YEAR+5),12,31)

class Location(models.Model):
	name = models.CharField(max_length=64)
	
	def __unicode__(self):
		return self.name

class Job(models.Model):

	STATUS_CHOICES = (('D','Draft'),('P','Published'))
	LOCATION_CHOICES = (('ALL','All'), ('ATI','Atikokan'), ('DRY','Dryden'),('FFR','Fort Frances'),('KEN','Kenora'),('RLK','Red Lake'),('SLK','Sioux Lookout'))
	TERM_CHOICES = (('PT','Part-Time'),('FT','Full-Time'),('CF','Contact Full-Time'),('CP','Contract Part-Time'))
	WAGE_CHOICES = (('A','Per Annum'),('H','Per Hour'),('W','Per Week'))

	status = models.CharField(max_length='1',choices=STATUS_CHOICES)
	publish_date = models.DateField()
	closing_date = models.DateField()
	title = models.CharField(max_length=64, blank=False)
	location = models.ManyToManyField(Location)
	term = models.CharField(max_length=2,choices=TERM_CHOICES)
	contract_length = models.IntegerField(max_length=2, help_text='Length specified in months')
	extension_possible = models.BooleanField()
	union = models.BooleanField()
	positions_available = models.IntegerField()
	qualifications = models.TextField()
	requirements = models.TextField()
	service = models.CharField(max_length=64)
	payscale_start = models.DecimalField(max_digits=8, decimal_places=2)
	payscale_end = models.DecimalField(max_digits=8, decimal_places=2)
	payscale_period = models.CharField(max_length=1,choices=WAGE_CHOICES)
	hours_per_week = models.DecimalField(max_digits=4,decimal_places=2)

	def clean(self):
		if self.term == 'CF' or self.term == 'CP':
			if self.contract_length is None:
				raise ValidationError('Contact positions need a contract length specified in number of months.')
		if self.status == 'P' and self.publish_date is None:
			self.publish_date = TODAY
		if self.closing_date is None:
			self.closing_date = OPEN

	def get_absolute_url(self):
		return '/corporate-services/careers/' + text.slugify(self.title)

	def __unicode__(self):
		return self.title