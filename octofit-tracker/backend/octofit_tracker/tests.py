from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelSmokeTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create(name='Test', email='test@example.com', team='Marvel')
        self.assertEqual(user.name, 'Test')
    def test_team_creation(self):
        team = Team.objects.create(name='TestTeam')
        self.assertEqual(team.name, 'TestTeam')
    def test_activity_creation(self):
        activity = Activity.objects.create(user_email='test@example.com', activity='Running', duration=30)
        self.assertEqual(activity.activity, 'Running')
    def test_leaderboard_creation(self):
        lb = Leaderboard.objects.create(user_email='test@example.com', points=100)
        self.assertEqual(lb.points, 100)
    def test_workout_creation(self):
        workout = Workout.objects.create(name='Yoga', suggested_for='Marvel')
        self.assertEqual(workout.name, 'Yoga')
