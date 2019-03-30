# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    film = models.ForeignKey('Film', models.DO_NOTHING, blank=True, null=True)
    com_comment = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    content = models.CharField(max_length=256)
    time = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comment'



class Film(models.Model):
    film_id = models.AutoField(primary_key=True)
    c_name = models.CharField(max_length=256, blank=True, null=True)
    e_name = models.CharField(max_length=256, blank=True, null=True)
    country = models.CharField(max_length=128, blank=True, null=True)
    category = models.CharField(max_length=128, blank=True, null=True)
    release_time = models.DateField(blank=True, null=True)
    mark = models.CharField(max_length=32, blank=True, null=True)
    status = models.CharField(max_length=128, blank=True, null=True)
    image = models.CharField(max_length=256, blank=True, null=True)
    des = models.CharField(max_length=256, blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'film'


class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    role = models.CharField(max_length=128, blank=True, null=True)
    films = models.ManyToManyField(Film, through='StaffFilm')

    class Meta:
        managed = False
        db_table = 'staff'


class StaffFilm(models.Model):
    film = models.ForeignKey(Film, models.DO_NOTHING, primary_key=True)
    staff = models.ForeignKey(Staff, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'staff_film'
        unique_together = (('film', 'staff'),)


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, blank=True, null=True)
    password = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
