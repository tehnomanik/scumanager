from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Squad(models.Model):
    # PROPERTIES
    squad_name = models.CharField(max_length=200, null = True, blank=True)
    squad_leader = models.CharField(max_length=200, null = True, blank=True)
    #squad_leader = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL, blank=True, related_name="squad_leader")
    note = models.CharField(max_length=1000, null = True, blank=True)

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    modified_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, blank=True)

    # METHODS
    def __str__(self):
        return self.squad_name

    def totalCars(self):
        players = self.player_set.all()
        vehicles = 0
        for p in players:
            vehicles += p.vehicle_set.count()
        return str(vehicles)

    def totalFlags(self):
        players = self.player_set.all()
        flags = 0
        for p in players:
            flags += p.flag_set.count()
        return str(flags)       

class Player(models.Model):
    # RELATION
    squad = models.ForeignKey(Squad, null=True, on_delete=models.SET_NULL, blank=True)

    # PROPERTIES
    discord_name = models.CharField(max_length=200, null = True, blank=True)
    ingame_name = models.CharField(max_length=200, null = True)
    steam_name = models.CharField(max_length=200, null = True, blank=True)
    steam_id = models.CharField(max_length=200, null = True, blank=True)
    email = models.EmailField(max_length=200, null = True, blank=True)
    note = models.CharField(max_length=1000, null = True, blank=True)
    is_admin = models.BooleanField(default=False)
    server_id = models.IntegerField(default=0)

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    modified_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, blank=True)

    # METHODS
    def __str__(self):
        return self.ingame_name

    def totalDonations(self):
        donations = self.donation_set.all()
        amount = 0
        for d in donations:
            amount += d.amount
        return str(amount)

class Donation(models.Model):
    # RELATION
    player = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL, blank=True)
    
    # PROPERTIES
    donation_date = models.DateTimeField(null = True, blank=True, auto_now=False, auto_now_add=False)
    amount = models.FloatField(null=True)
    note = models.CharField(max_length=1000, null = True, blank=True)

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    modified_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, blank=True)
    
    # METHODS
    def __str__(self):
        if self.player is not None:
            return str(self.player.ingame_name) + " # " + str(self.amount)
        else:
            return " # " + str(self.amount)

class Flag(models.Model):
    # RELATION
    player = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL)
    
    # PROPERTIES
    location = models.CharField(max_length=200, null = True)
    has_base = models.BooleanField(default=True)
    note = models.CharField(max_length=1000, null = True, blank=True)

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    modified_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, blank=True)
    
    # METHODS
    def __str__(self):
        return self.location

class Vehicle(models.Model):
    # ENUMERATION FOR VEHICLE TYPE
    VEHICLE_TYPE = (
        ('Tractor', 'Tractor'),
        ('Quad', 'Quad'),
        ('SUV', 'SUV'),
        ('Pickup', 'Pickup'),
    )

    # RELATION  
    player = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL, blank=True)
    
    # PROPERTIES
    vehicle_id = models.CharField(max_length=200, null = True, blank=True)
    vehicle_type = models.CharField(max_length=200, null = True, choices=VEHICLE_TYPE)
    note = models.CharField(max_length=1000, null = True, blank=True)

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    modified_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, blank=True)

    # METHODS
    def __str__(self):
        return self.vehicle_type + " # " + str(self.player)
    
class Case(models.Model):
    # ENUMERATION FOR CASE TYPE
    CASE_TYPE = (
        ('PvP', 'PvP'),
        ('Stealing', 'Stealing'),
        ('Destroying', 'Destroying'),
        ('Chat offence', 'Chat offence'),
        ('Good Stuff', 'Good Stuff'),
        ('Other', 'Other'),
    )

    #admins = 

    # RELATION  
    player = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL)

    # PROPERTIES
    
    case_type = models.CharField(max_length=200, null = True, choices=CASE_TYPE)
    case_date = models.DateTimeField(null = True, blank=True, auto_now=False, auto_now_add=False)
    case_location = models.CharField(max_length=200, null = True, blank=True)    
    note = models.CharField(max_length=1000, null = True, blank=True)
    is_active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    modified_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, blank=True, related_name='modified_by')


    # METHODS
    def __str__(self):
        return self.player.ingame_name + " for " + str(self.case_type)