# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Film'
        db.create_table('film', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('film_name', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('film_created_users', self.gf('django.db.models.fields.TextField')(blank=True, default='')),
            ('film_jenre', self.gf('django.db.models.fields.CharField')(max_length=40, default='other')),
            ('film_text', self.gf('django.db.models.fields.TextField')()),
            ('film_year', self.gf('django.db.models.fields.IntegerField')(default=2014)),
            ('film_date_public', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 8, 28, 0, 0))),
            ('film_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('film_award', self.gf('django.db.models.fields.TextField')(blank=True, default='')),
            ('film_like', self.gf('django.db.models.fields.IntegerField')(blank=True, null=True, default=0)),
            ('film_sided_site', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('film_sided_id', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('film_country', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('film_money_create', self.gf('django.db.models.fields.IntegerField')(blank=True, null=True, default=0)),
        ))
        db.send_create_signal('film', ['Film'])

        # Adding model 'Film_comment'
        db.create_table('film_comment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('film_comment_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('film_comment_text', self.gf('django.db.models.fields.TextField')()),
            ('film_comment_link', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['film.Film'])),
            ('film_comment_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('film', ['Film_comment'])


    def backwards(self, orm):
        # Deleting model 'Film'
        db.delete_table('film')

        # Deleting model 'Film_comment'
        db.delete_table('film_comment')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'blank': 'True', 'symmetrical': 'False', 'related_name': "'user_set'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False', 'related_name': "'user_set'"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'object_name': 'ContentType', 'ordering': "('name',)", 'db_table': "'django_content_type'", 'unique_together': "(('app_label', 'model'),)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'film.film': {
            'Meta': {'db_table': "'film'", 'object_name': 'Film'},
            'film_award': ('django.db.models.fields.TextField', [], {'blank': 'True', 'default': "''"}),
            'film_country': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'film_created_users': ('django.db.models.fields.TextField', [], {'blank': 'True', 'default': "''"}),
            'film_date_public': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 8, 28, 0, 0)'}),
            'film_jenre': ('django.db.models.fields.CharField', [], {'max_length': '40', 'default': "'other'"}),
            'film_like': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True', 'default': '0'}),
            'film_money_create': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True', 'default': '0'}),
            'film_name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'film_sided_id': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'film_sided_site': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'film_text': ('django.db.models.fields.TextField', [], {}),
            'film_user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'film_year': ('django.db.models.fields.IntegerField', [], {'default': '2014'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'film.film_comment': {
            'Meta': {'db_table': "'film_comment'", 'object_name': 'Film_comment'},
            'film_comment_date': ('django.db.models.fields.DateTimeField', [], {}),
            'film_comment_link': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['film.Film']"}),
            'film_comment_text': ('django.db.models.fields.TextField', [], {}),
            'film_comment_user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['film']