
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone
from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Drop collections directly using PyMongo for clean slate
        db = connection.cursor().db_conn
        for collection in ['leaderboard', 'activities', 'workouts', 'users', 'teams']:
            if collection in db.list_collection_names():
                db[collection].drop()

        # Now repopulate using Django ORM

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create Users
        tony = User.objects.create(name='Tony Stark', email='tony@stark.com', team=marvel)
        steve = User.objects.create(name='Steve Rogers', email='steve@rogers.com', team=marvel)
        bruce = User.objects.create(name='Bruce Banner', email='bruce@banner.com', team=marvel)
        clark = User.objects.create(name='Clark Kent', email='clark@kent.com', team=dc)
        diana = User.objects.create(name='Diana Prince', email='diana@prince.com', team=dc)

        # Create Workouts
        pushups = Workout.objects.create(name='Pushups', description='Upper body', difficulty='Easy')
        running = Workout.objects.create(name='Running', description='Cardio', difficulty='Medium')
        squats = Workout.objects.create(name='Squats', description='Lower body', difficulty='Easy')

        # Create Activities
        Activity.objects.create(user=tony, type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user=steve, type='Pushups', duration=20, date=timezone.now().date())
        Activity.objects.create(user=bruce, type='Squats', duration=25, date=timezone.now().date())
        Activity.objects.create(user=clark, type='Running', duration=40, date=timezone.now().date())
        Activity.objects.create(user=diana, type='Pushups', duration=15, date=timezone.now().date())

        # Create Leaderboard
        Leaderboard.objects.create(user=tony, score=120, rank=1)
        Leaderboard.objects.create(user=steve, score=110, rank=2)
        Leaderboard.objects.create(user=clark, score=100, rank=3)
        Leaderboard.objects.create(user=bruce, score=90, rank=4)
        Leaderboard.objects.create(user=diana, score=80, rank=5)

        self.stdout.write(self.style.SUCCESS('Successfully populated octofit_db with test data'))
