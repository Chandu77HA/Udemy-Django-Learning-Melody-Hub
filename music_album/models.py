from django.db import models

# Create your models here.


class Musician(models.Model):
    # id = models.AutoField(primary_key=True)
    # The above line is auto generated by django when we migrate
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Album(models.Model):
    # id = models.AutoField(primary_key=True)
    # The above line is auto generated by django when we migrate
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    rating = (

        (1, "Worst"),
        (2, "Bad"),
        (3, "Not Bad"),
        (4, "Good"),
        (5, "Excellent"),

    )
    num_stars = models.IntegerField(choices=rating)

    # When we use one class inside the another class we use Meta Keyword

    def __str__(self):
        return self.name + ", Rating - " + str(self.num_stars)


class UploadSamplFile(models.Model):
    file_name = models.CharField(max_length=1000)
    sample_file = models.FileField(
        upload_to='sample_files/')

    def __str__(self):
        file_name = self.sample_file.name.split("/")[-1]
        return file_name
