from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponse
from application.models import AnswerManager, QuestionManager, Like, Question, Answer, Tag, Profile

def paginate(object_list, objects_count, page_num):

    paginator = Paginator(object_list, objects_count)
    try:
        objects_page = paginator.page(page_num)
    except EmptyPage:
            objects_page = paginator.page(paginator.num_pages)
    return objects_page

def index(request, page = 1):
    questions = Question.objects.new()
    questions = paginate(questions, 5, page)
    return render(request, 'index.html', {
        'objects': questions,
        'view_name': 'index',
        'url_prefix': '',
    })

def hot_index(request, page = 1):
    questions = Question.objects.hot()
    questions = paginate(questions, 5, page)
    return render(request, 'hot.html', {
        'objects': questions,
        'view_name': 'hot_index',
        'url_prefix': '/hot'
    })

def tag_index(request, tag, page = 1):
    questions = Question.objects.by_tags(tag)
    questions = paginate(questions, 5, page)
    return render(request, 'tag.html', {
        'objects': questions,
        'view_name': 'tag_index',
        'url_prefix': '/tag'
    })

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def ask(request):
    return render(request, 'ask.html')

def question(request, q_id,  page = 1):
    print "!!!!!!!!!!!!!!!!!!!!",q_id
    question = Question.objects.by_id(q_id) 
    answers = Answer.objects.by_id(q_id)
    answers = paginate(answers, 3, page)
    return render(request, 'question.html', {
        'objects': answers,
        'view_name': 'question',
        'url_prefix': '/question'
    })
   
    


