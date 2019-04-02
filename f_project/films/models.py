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
    film = models.ForeignKey('FilmBrief', models.DO_NOTHING, blank=True, null=True)
    icon = models.CharField(max_length=256, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    content = models.CharField(max_length=256, blank=True, null=True)
    release_time = models.DateField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comment'



class FilmBrief(models.Model):
    film_id = models.AutoField(primary_key=True)
    c_name = models.CharField(max_length=128, blank=True, null=True)
    e_name = models.CharField(max_length=128, blank=True, null=True)
    category = models.CharField(max_length=128, blank=True, null=True)
    release_time = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=128, blank=True, null=True)
    length = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'film_brief'


class FilmBriefMember(models.Model):
    member = models.ForeignKey('Member', models.DO_NOTHING, primary_key=True)
    film = models.ForeignKey(FilmBrief, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'film_brief_member'
        unique_together = (('member', 'film'),)


class FilmDetail(models.Model):
    detail_id = models.AutoField(primary_key=True)
    film = models.ForeignKey(FilmBrief, models.DO_NOTHING, blank=True, null=True)
    cover_url = models.CharField(max_length=256, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=64, blank=True, null=True)
    score_pe_num = models.IntegerField(blank=True, null=True)
    box_office = models.CharField(max_length=128, blank=True, null=True)
    synopsis = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'film_detail'


class Member(models.Model):
    member_id = models.AutoField(primary_key=True)
    img = models.CharField(max_length=256, blank=True, null=True)
    member_name = models.CharField(max_length=128, blank=True, null=True)
    member_type = models.CharField(max_length=64, blank=True, null=True)
    film_briefs = models.ManyToManyField(FilmBrief, through='FilmBriefMember')
    
    class Meta:
        managed = False
        db_table = 'member'


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    password = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
