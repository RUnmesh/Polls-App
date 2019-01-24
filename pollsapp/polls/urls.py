from django.conf.urls import url
from . import views

app_name = 'polls'

urlpatterns = [
    url(r'^$' , views.test , name = 'test' ) ,
    url(r'^(?P<ques_id>[0-9]+)/$' , views.details , name = 'details' ) ,
    url(r'^(?P<ques_id>[0-9]+)/results/$' , views.results , name = 'results' ) ,
    url(r'^(?P<ques_id>[0-9]+)/votes/$' , views.votes , name = 'votes' ) ,
    url(r'^add/$' , views.add , name = 'add') ,
    url(r'^(?P<ques_id>[0-9]+)/add_choice/$' , views.choiceadd , name = 'choice_add' ) ,
]