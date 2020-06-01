from django.db import models

# Create your models here.





class User(models.Model):
    login = models.CharField(max_length=200, verbose_name='login')
    password = models.CharField(max_length = 50, verbose_name='password')
    isAdmin = models.BooleanField(verbose_name='is admin') # Не нужно, но пусть будет чтобы ошибок не было.
    FIO = models.CharField(max_length = 50, verbose_name='last first middle name', default="")
    Postion = models.CharField(max_length = 50, verbose_name='position', default="")
    Department = models.CharField(max_length = 50, verbose_name='department', default="")

    def __str__(self):
        return self.login


    class Meta():
        verbose_name = 'user'
        verbose_name_plural='users'




class Patient(models.Model):
    number_card = models.IntegerField(verbose_name="card")
    FIO = models.CharField(max_length=100, verbose_name="last first middle name")
    date_birth = models.CharField(max_length=100, verbose_name="birthday")
    sex = models.CharField(max_length=50, verbose_name="sex")
    nationality = models.CharField(max_length=50, verbose_name="nationality")
    education = models.CharField(max_length=100, verbose_name="education")
    address = models.CharField(max_length=100, verbose_name="adress")
    phone = models.CharField(max_length=50, verbose_name="phone")
    job = models.CharField(max_length=100, verbose_name="place work")
    position = models.CharField(max_length=100, verbose_name="position")


    def __str__(self):
        return self.number_card


    class Meta():
        verbose_name = 'patient'
        verbose_name_plural='patients'

# Сущность анкета пациента
class Ancket(models.Model):
    date = models.CharField(max_length=100, verbose_name="date form")
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE, verbose_name="patient")

    def __str__(self):
        return self.date


    class Meta():
        verbose_name = 'form'
        verbose_name_plural='forms'

# Вопросы
class Question(models.Model):
    question = models.CharField(max_length=100, verbose_name="question")

    def __str__(self):
        return self.question


    class Meta():
        verbose_name = 'question'
        verbose_name_plural='qestions'

# ответы
class Answer(models.Model):
    date = models.DateField()
    note = models.TextField()
    conviction = models.IntegerField(default=0)
    ancket = models.ForeignKey(Ancket, on_delete = models.CASCADE)
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    

    def __str__(self):
        return self.note




# Болезни(диагнозы)
class Disease(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    note = models.TextField() #описание

    def __str__(self):
        return self.name



# Эпикризы
class Epicriz(models.Model):
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    invalid = models.BooleanField(default = False)
    lechenie = models.CharField(max_length=500, default="", verbose_name="Лечение", null=True)
    date_gospit = models.DateField(default = "1999-01-01" , null=True)
    date_vipisky = models.DateField(default = "1999-01-01", null=True)

    def __str__(self):
        return self.lechenie




# Диагнозы
class Diagnos(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    epicriz = models.ForeignKey(Epicriz, on_delete = models.CASCADE)
    disease = models.ForeignKey(Disease, on_delete = models.CASCADE)
    note = models.TextField()

    def __str__(self):
        return self.note
