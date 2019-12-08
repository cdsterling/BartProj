# Generated by Django 3.0 on 2019-12-08 05:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_auto_20191207_2031'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteStation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station', models.CharField(blank=True, choices=[('LAKE', 'Lake Merritt'), ('FTVL', 'Fruitvale'), ('COLS', 'Coliseum'), ('SANL', 'San Leandro'), ('BAYF', 'Bay Fair'), ('HAYW', 'Hayward'), ('SHAY', 'South Hayward'), ('UCTY', 'Union City'), ('FRMT', 'Fremont'), ('ROCK', 'Rockridge'), ('ORIN', 'Orinda'), ('LAFY', 'Lafayette'), ('WCRK', 'Walnut Creek'), ('PHIL', 'Pleasant Hill/Contra Costa Centre'), ('CONC', 'Concord'), ('NCON', 'North Concord/Martinez'), ('PITT', 'Pittsburg/Bay Point'), ('PCTR', 'Pittsburg Center'), ('ANTC', 'Antioch'), ('12TH', '12th St. Oakland City Center'), ('19TH', '19th St. Oakland'), ('MCAR', 'MacArthur'), ('CAST', 'Castro Valley'), ('WDUB', 'West Dublin/Pleasanton'), ('DUBL', 'Dublin/Pleasanton'), ('WOAK', 'West Oakland'), ('EMBR', 'Embarcadero'), ('MONT', 'Montgomery St.'), ('POWL', 'Powell St.'), ('CIVC', 'Civic Center/UN Plaza'), ('16TH', '16th St. Mission'), ('24TH', '24th St. Mission'), ('GLEN', 'Glen Park'), ('BALB', 'Balboa Park'), ('DALY', 'Daly City'), ('ASHB', 'Ashby'), ('DBRK', 'Downtown Berkeley'), ('NBRK', 'North Berkeley'), ('PLZA', 'El Cerrito Plaza'), ('DELN', 'El Cerrito del Norte'), ('RICH', 'Richmond'), ('WARM', 'Warm Springs/South Fremont'), ('COLM', 'Colma'), ('SSAN', 'South San Francisco'), ('SBRN', 'San Bruno'), ('MLBR', 'Millbrae'), ('SFIA', "San Francisco Int'l Airport")], max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
