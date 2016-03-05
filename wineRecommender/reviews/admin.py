from django.contrib import admin

# Register your models here.
from .models import Wine, Review

class ReviewAdmin(admin.ModelAdmin):
	model = Review
	list_display = ('wine', 'rating', 'user_name', 'comment', 'pub_date')
	list_filter = ['pub_date', 'user_name']
	search_fields = ['comment']

class WineAdmin(admin.ModelAdmin):
	model = Wine
	list_display = ('name', 'year')
	# list_filter = ['year']
	# search_fields = ['comment']
# This will allow us to see our Review app model entities
# in the admin now. So youll see a section for Wines and Reviews
admin.site.register(Wine, WineAdmin)
# Reviews guts will be different because we've created a
#  custom class ReviewAdmin that dictates what we see
admin.site.register(Review, ReviewAdmin)