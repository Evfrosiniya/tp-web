from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class AnswerManager(models.Manager):
    def by_id(id):
        return Answer.objects.filter(question=id)


class QuestionManager(models.Manager):
    def new():
        return Question.objects.order_by('-pub_date')

    def hot():
        return Question.objects.order_by('-rating')

    def by_tags(tag):
        return Question.objects.filter(tags__title=tag)

    def by_id(q_id):
        return Question.objects.get(id=q_id)


class Like(models.Model):
  likes = models.IntegerField(default=0)
  
class Question(models.Model):
  theme_text = models.CharField(max_length=200)
  question_text = models.TextField()
  tags_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField(default=timezone.now)
  author = models.ForeignKey(User)
  likes = models.ManyToManyField(Like)


class Answer(models.Model):
  answer_text = models.TextField()
  pub_date = models.DateTimeField(default=timezone.now)
  author = models.ForeignKey(User)
  correct = models.BooleanField(default=False)
  likes = models.ManyToManyField(Like)

class Tag(models.Model):
  tags_text = models.CharField(max_length=200)

class Profile(models.Model):
  user = models.OneToOneField(User)
  avatar_name = models.CharField(max_length=250)




