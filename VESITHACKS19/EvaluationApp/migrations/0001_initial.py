# Generated by Django 2.2.5 on 2019-09-22 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dname', models.CharField(max_length=20)),
                ('c1', models.SmallIntegerField()),
                ('c2', models.SmallIntegerField()),
                ('c3', models.SmallIntegerField()),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=20)),
                ('d_no', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_requests_created', to='EvaluationApp.Dept')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=20)),
                ('dno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_requests_created', to='EvaluationApp.Dept')),
            ],
        ),
        migrations.CreateModel(
            name='ManagementFB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mf1', models.SmallIntegerField()),
                ('mf2', models.SmallIntegerField()),
                ('mf3', models.SmallIntegerField()),
                ('mf4', models.SmallIntegerField()),
                ('mf5', models.SmallIntegerField()),
                ('mfcomment', models.TextField()),
                ('feedbackby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='managementfb_requests_created1', to='EvaluationApp.User')),
                ('feedbackof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='managementfb_requests_created2', to='EvaluationApp.User')),
                ('feedbackto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='managementfb_requests_created', to='EvaluationApp.User')),
            ],
        ),
        migrations.CreateModel(
            name='HRassessment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hra1', models.SmallIntegerField()),
                ('hra2', models.SmallIntegerField()),
                ('hra3', models.SmallIntegerField()),
                ('hra4', models.SmallIntegerField()),
                ('hra5', models.SmallIntegerField()),
                ('hra_assessment_report', models.TextField()),
                ('assessedby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hrassessment_requests_created1', to='EvaluationApp.User')),
                ('assessedof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hrassessment_requests_created', to='EvaluationApp.User')),
            ],
        ),
        migrations.CreateModel(
            name='Evaluates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e1', models.SmallIntegerField()),
                ('e2', models.SmallIntegerField()),
                ('e3', models.SmallIntegerField()),
                ('e4', models.SmallIntegerField()),
                ('e5', models.SmallIntegerField()),
                ('e6', models.SmallIntegerField()),
                ('e7', models.SmallIntegerField()),
                ('e8', models.SmallIntegerField()),
                ('e9', models.SmallIntegerField()),
                ('e10', models.SmallIntegerField()),
                ('suggestion', models.TextField()),
                ('evaluated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evaluates_requests_created1', to='EvaluationApp.User')),
                ('evaluation_of', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evaluates_requests_created', to='EvaluationApp.User')),
            ],
        ),
        migrations.CreateModel(
            name='DTassessment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dta1', models.SmallIntegerField()),
                ('dta2', models.SmallIntegerField()),
                ('dta3', models.SmallIntegerField()),
                ('dta4', models.SmallIntegerField()),
                ('dta5', models.SmallIntegerField()),
                ('dta_assessment_report', models.TextField()),
                ('assessedby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dtassessment_requests_created1', to='EvaluationApp.User')),
                ('assessedof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dtassessment_requests_created', to='EvaluationApp.User')),
            ],
        ),
        migrations.CreateModel(
            name='DHassessment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dha1', models.SmallIntegerField()),
                ('dha2', models.SmallIntegerField()),
                ('dha3', models.SmallIntegerField()),
                ('dha4', models.SmallIntegerField()),
                ('dha5', models.SmallIntegerField()),
                ('dha_assessment_report', models.TextField()),
                ('assessedby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dhassessment_requests_created1', to='EvaluationApp.User')),
                ('assessedof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dhassessment_requests_created', to='EvaluationApp.User')),
            ],
        ),
        migrations.AddField(
            model_name='dept',
            name='dHeadId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dept_requests_created', to='EvaluationApp.User'),
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.TextField(max_length=50)),
                ('c1', models.SmallIntegerField()),
                ('c2', models.SmallIntegerField()),
                ('c3', models.SmallIntegerField()),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_requests_created', to='EvaluationApp.Project')),
            ],
        ),
    ]
