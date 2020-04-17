from django.db import models
from django.contrib.auth.models import User
# Tables in the database

# A table that holds all Servers with auto primary key, display name and foreign owner id
class Server(models.Model):
    server_id = models.AutoField(primary_key=True)
    display_name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name="server")
    def __str__(self):
        return self.display_name

# A table that holds all Channels with auto pk, display name, type and fk Server id
class Channel(models.Model):
    channel_id = models.AutoField(primary_key=True)
    display_name = models.CharField(max_length=100)
    TEXT = 'text'
    VOICE = 'voice'
    type_choices = [
        (TEXT, 'Text'),
        (VOICE, 'Voice'),
    ]
    type = models.CharField(
        max_length=5,
        choices=type_choices,
        default='text',
        blank=False,
    )
    server = models.ForeignKey(Server, on_delete=models.CASCADE,)
    def __str__(self):
        return self.display_name+" "+self.type
