# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Film.film_money_create'
        db.delete_column('film', 'film_money_create')


    def backwards(self, orm):
        # Adding field 'Film.film_money_create'
        db.add_column('film', 'film_money_create',
                      self.gf('django.db.models.fields.IntegerField')(blank=True, default=0),
                      keep_default=False)


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'related_name': "'user_set'", 'blank': 'True', 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'related_name': "'user_set'", 'blank': 'True', 'symmetrical': 'False'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'", 'object_name': 'ContentType'},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'film.film': {
            'Meta': {'object_name': 'Film', 'db_table': "'film'"},
            'film_award': ('django.db.models.fields.TextField', [], {'blank': 'True', 'default': "''"}),
            'film_country': ('django.db.models.fields.CharField', [], {'max_length': '200', 'default': "''"}),
            'film_created_users': ('django.db.models.fields.TextField', [], {'blank': 'True', 'default': "''"}),
            'film_date_public': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 8, 28, 0, 0)'}),
            'film_image': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100', 'default': "'/media/filmImg/default.jpg'"}),
            'film_is_moderator': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'film_like': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True', 'default': '0'}),
            'film_name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'film_sided_id': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'film_sided_site': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'film_status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['film.Status']", 'default': '2'}),
            'film_text': ('django.db.models.fields.TextField', [], {}),
            'film_user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'films'"}),
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
        },
        'film.jenre': {
            'Meta': {'object_name': 'Jenre'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jenre_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'jenre_title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'film.status': {
            'Meta': {'object_name': 'Status'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status_film_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['film']