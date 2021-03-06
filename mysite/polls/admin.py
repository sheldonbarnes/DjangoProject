from django.contrib import admin

from .models import Choice, Question, Contact, UserProfile

class ContactAdmin(admin.ModelAdmin):
    list_display = ('FirstName', 'LastName','PhoneNumber','EmailAddress','Address')
    search_fields = ['FirstName', 'LastName','PhoneNumber','EmailAddress','Address']
    list_filter = ['LastName','FirstName']
    
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):


    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date','was_published_recently')
    list_filter = ['pub_date']
    list_per_page = 100
    search_fields = ['question_text']

admin.site.register(Contact,ContactAdmin)
admin.site.register(UserProfile)
#admin.site.register(Question, QuestionAdmin)
