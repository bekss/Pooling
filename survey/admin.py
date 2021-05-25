from django.contrib import admin
from .models import Choices, Answer, Question, Polls

admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(Choices)
admin.site.register(Polls)
