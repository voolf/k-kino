# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Jenre'
        db.create_table('film_jenre', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('jenre_name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('jenre_title', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('film', ['Jenre'])

        # Adding model 'Status'
        db.create_table('film_status', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status_film_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('film', ['Status'])

        # Deleting field 'Film.film_jenre'
        db.delete_column('film', 'film_jenre')

        # Adding field 'Film.film_status'
        db.add_column('film', 'film_status',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['film.Status']),
                      keep_default=False)

        # Adding field 'Film.film_is_moderator'
        db.add_column('film', 'film_is_moderator',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Film.film_image'
        db.add_column('film', 'film_image',
                      self.gf('django.db.models.fields.files.ImageField')(default='/media/filmImg/default.jpg', blank=True, max_length=100),
                      keep_default=False)

        # Adding M2M table for field film_jenres on 'Film'
        m2m_table_name = db.shorten_name('film_film_jenres')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('film', models.ForeignKey(orm['film.film'], null=False)),
            ('jenre', models.ForeignKey(orm['film.jenre'], null=False))
        ))
        db.create_unique(m2m_table_name, ['film_id', 'jenre_id'])


    def backwards(self, orm):
        # Deleting model 'Jenre'
        db.delete_table('film_jenre')

        # Deleting model 'Status'
        db.delete_table('film_status')

        # Adding field 'Film.film_jenre'
        db.add_column('film', 'film_jenre',
                      self.gf('django.db.models.fields.CharField')(max_length=40, default='other'),
                      keep_default=False)

        # Deleting field 'Film.film_status'
        db.delete_column('film', 'film_status_id')

        # Deleting field 'Film.film_is_moderator'
        db.delete_column('film', 'film_is_moderator')

        # Deleting field 'Film.film_image'
        db.delete_column('film', 'film_image')

        # Removing M2M table for field film_jenres on 'Film'
        db.delete_table(db.shorten_name('film_film_jenres'))


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False'})
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
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'related_name': "'user_set'", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'related_name': "'user_set'", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'object_name': 'ContentType', 'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'film.film': {
            'Meta': {'object_name': 'Film', 'db_table': "'film'"},
            'film_award': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'film_country': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'film_created_users': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'film_date_public': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 8, 28, 0, 0)'}),
            'film_image': ('django.db.models.fields.files.ImageField', [], {'default': "'/media/filmImg/default.jpg'", 'blank': 'True', 'max_length': '100'}),
            'film_is_moderator': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'film_jenres': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['film.Jenre']", 'related_name': "'films'", 'symmetrical': 'False'}),
            'film_like': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True', 'null': 'True'}),
            'film_money_create': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True', 'null': 'True'}),
            'film_name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'film_sided_id': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'film_sided_site': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'film_status': ('django.db.models.fields.related.ForeignKey', [], {'default': '2', 'to': "orm['film.Status']"}),
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