from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class AnswerManager(models.Manager):
    def by_id(self, q_id):
        return Answer.objects.filter(question_id = q_id)


class QuestionManager(models.Manager):
    def by_tags(self, tag):
        return Question.objects.filter(tags_text = tag)

    def by_id(self, q_id):
        return Question.objects.get(question_id = q_id)

    def new(self):
        return Question.objects.order_by('-pub_date')

    def hot(self):
        return Question.objects.order_by('-likes')

class Like(models.Model):
  likes = models.IntegerField(default = 0)
  
class Question(models.Model):
  theme_text = models.CharField(max_length = 200)
  question_text = models.TextField()
  question_id = models.CharField(max_length = 200)
  tags_text = models.CharField(max_length = 200)
  pub_date = models.DateTimeField(default = timezone.now)
  author = models.ForeignKey(User)
  likes = models.ManyToManyField(Like)
  objects = QuestionManager()


class Answer(models.Model):
  answer_text = models.TextField()
  pub_date = models.DateTimeField(default = timezone.now)
  author = models.ForeignKey(User)
  correct = models.BooleanField(default = False)
  likes = models.ManyToManyField(Like)
  answer_id = models.CharField(max_length = 200)
  question_id = models.ForeignKey(Question)
  objects = AnswerManager()

class Tag(models.Model):
  tags_text = models.CharField(max_length = 200)

class Profile(models.Model):
  user = models.OneToOneField(User)
  avatar_name = models.CharField(max_length = 250)




