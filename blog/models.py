from django.db import models
from datetime import datetime
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    time = models.DateTimeField(default = datetime.now, blank = True)
    body = models.TextField()
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])

    class Meta:
        ordering = ["-time"]

class Comment(models.Model):
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    time = models.DateTimeField(default = datetime.now, blank = True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.name

class Members(models.Model):
    Mr = 'Mr'
    Mrs = 'Mrs'
    Miss = 'Miss'
    Title = (
        (Mr, 'Mr'),
        (Mrs, 'Mrs'),
        (Miss, 'Miss'),
    )

    Male = 'M'
    Female = 'F'
    Gender = (
        (Male, 'Male'),
        (Female, 'Female'),
    )
   
    Intercession = 'I'
    Trade_and_Investment = 'T'
    Economy = 'E'
    Sounds_and_Worship = 'S'
    Dances_Poems_and_Arts = 'D'
    Intercity_and_International_Affairs = 'II'
    IT_and_Communications ='IT'
    Leadership_and_Government = 'L'
    SMEs_Development_and_Priesthood = 'SME'
    PBC_Finances_Council24 = 'PF'

    Faculty = (
        
        (Intercession, 'Intercession'),
        (Trade_and_Investment, 'Trade and Investment'),
        (Economy, 'Economy'),
        (Sounds_and_Worship, 'Sounds and Worship'),
        (Dances_Poems_and_Arts, 'Dances Poems and Arts'),
        (Intercity_and_International_Affairs, 'Intercity and International Affairs'),
        (IT_and_Communications, 'IT and Communications'),
        (Leadership_and_Government, 'Leadership and Government'),
        (SMEs_Development_and_Priesthood, 'SMEs Development and Priesthood'),
        (PBC_Finances_Council24, 'PBC Finances Council 24'),
        

    )


    Title = models.CharField(max_length=40, choices=Title)
    Gender = models.CharField(max_length=10, choices=Gender, default=Male,)
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    Mobile_Number = models.IntegerField()
    Email = models.EmailField()
    Nationality = models.CharField(max_length=30)
    Occupation = models.CharField(max_length=30)
    Interested_PBC_Faculty = models.CharField(max_length=40, choices=Faculty, default=Intercession,)
    Agree_to_Terms_and_Conditions = models.BooleanField()
    pbc_number = models.CharField(max_length=30, null=True, blank=True,)

    def __str__(self):
        return self.Title