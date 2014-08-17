# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Film.film_country'
        db.add_column('film', 'film_country',
                      self.gf('django.db.models.fields.CharField')(null=True, max_length=200),
                      keep_default=False)

        # Adding field 'Film.film_money_create'
        db.add_column('film', 'film_money_create',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Film.film_country'
        db.delete_column('film', 'film_country')

        # Deleting field 'Film.film_money_create'
        db.delete_column('film', 'film_money_create')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'object_name': 'Permission', 'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Group']", 'symmetrical': 'False', 'related_name': "'user_set'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Permission']", 'symmetrical': 'False', 'related_name': "'user_set'"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'object_name': 'ContentType', 'db_table': "'django_content_type'", 'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'film.film': {
            'Meta': {'object_name': 'Film', 'db_table': "'film'"},
            'film_award': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'film_country': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '200'}),
            'film_created_users': ('django.db.models.fields.TextField', [], {'default': "'-'"}),
            'film_date_public': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 8, 17, 0, 0)'}),
            'film_genre': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'film_like': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'film_money_create': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'film_name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'film_sided_id': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '200'}),
            'film_sided_site': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'film_text': ('django.db.models.fields.TextField', [], {}),
            'film_user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'film_year': ('django.db.models.fields.IntegerField', [], {'default': '2014'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'film.film_comment': {
            'Meta': {'object_name': 'Film_comment', 'db_table': "'film_comment'"},
            'film_comment_date': ('django.db.models.fields.DateTimeField', [], {}),
            'film_comment_link': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['film.Film']"}),
            'film_comment_text': ('django.db.models.fields.TextField', [], {}),
            'film_comment_user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['film']