from django.db import models

class Question(models.Model):
    # Field for the question text
    question_text = models.CharField(max_length=200)
    # Field for the publication date
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    # A foreign key to associate a choice with a question
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # Field for the choice text
    choice_text = models.CharField(max_length=200)
    # Field to store the number of votes
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
