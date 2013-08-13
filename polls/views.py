from django.http import HttpResponse

def index(request):
    return HttpResponse('hello world')

def detail(request, poll_id):
    return HttpResponse('Looking at poll %s' % poll_id)

def results(request, poll_id):
    return HttpResponse('Looking at results of poll %s' % poll_id)

def vote(request, poll_id):
    return HttpResponse('Voting on poll %s' % poll_id)
