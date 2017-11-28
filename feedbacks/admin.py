from django.contrib import admin
from feedbacks.models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ["create_date","subject"]
    list_display_links = ["create_date","subject"]
 

admin.site.register(Feedback, FeedbackAdmin)
