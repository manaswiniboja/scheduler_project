from django.db import models


class Scheduler(models.Model):

    # ---------- CHOICES ----------
    PROCESS_CHOICES = [
        ('Application Data Backup', 'Application Data Backup'),
        ('DB Sync', 'DB Sync'),
        ('Files Sync', 'Files Sync'),
        ('Empower Settings', 'Empower Settings'),
        ('Chromeleon Settings', 'Chromeleon Settings'),
    ]

    BUSINESS_UNIT_CHOICES = [
        ('QA', 'QA'),
        ('QC', 'QC'),
        ('R&D', 'R&D'),
    ]

    PLANT_CHOICES = [
        ('Plant-1', 'Plant-1'),
        ('Plant-2', 'Plant-2'),
    ]

    LOCATION_CHOICES = [
        ('India', 'India'),
        ('USA', 'USA'),
    ]

    MODULE_CHOICES = [
        ('Scheduler', 'Scheduler'),
        ('Backup', 'Backup'),
        ('Sync', 'Sync'),
    ]

    INSTRUMENT_CHOICES = [
        ('HPLC', 'HPLC'),
        ('GC', 'GC'),
        ('LCMS', 'LCMS'),
    ]

    FREQUENCY_CHOICES = [
        ('Daily', 'Daily'),
        ('Weekly', 'Weekly'),
        ('Monthly', 'Monthly'),
    ]

    UOM_CHOICES = [
        ('Minutes', 'Minutes'),
        ('Hours', 'Hours'),
        ('Days', 'Days'),
    ]

    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]

    # ---------- COMMON FIELDS ----------
    process = models.CharField(max_length=50, choices=PROCESS_CHOICES)

    business_unit = models.CharField(
        max_length=50, choices=BUSINESS_UNIT_CHOICES, blank=True, null=True
    )

    plant = models.CharField(max_length=50, choices=PLANT_CHOICES)
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES)
    module = models.CharField(max_length=50, choices=MODULE_CHOICES)

    instrument = models.CharField(
        max_length=50, choices=INSTRUMENT_CHOICES, blank=True, null=True
    )

    execution_frequency = models.CharField(
        max_length=20, choices=FREQUENCY_CHOICES, blank=True, null=True
    )

    interval = models.IntegerField(blank=True, null=True)

    uom = models.CharField(
        max_length=20, choices=UOM_CHOICES, blank=True, null=True
    )

    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='Active'
    )

    effected_from = models.DateField(blank=True, null=True)

    # ---------- DB / FILE / APP CONFIG ----------
    host_ip = models.CharField(max_length=50, blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)

    username = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)

    database = models.CharField(max_length=100, blank=True, null=True)
    table_name = models.CharField(max_length=100, blank=True, null=True)

    source_dir = models.CharField(max_length=255, blank=True, null=True)
    target_dir = models.CharField(max_length=255, blank=True, null=True)

    # ---------- EMPOWER FIELDS ----------
    empower_module = models.CharField(max_length=50, blank=True, null=True)
    empower_plant = models.CharField(max_length=50, blank=True, null=True)
    empower_location = models.CharField(max_length=50, blank=True, null=True)
    empower_host = models.CharField(max_length=255, blank=True, null=True)
    empower_data_source = models.CharField(max_length=255, blank=True, null=True)
    empower_username = models.CharField(max_length=50, blank=True, null=True)
    empower_password = models.CharField(max_length=255, blank=True, null=True)
    empower_default_project = models.CharField(max_length=255, blank=True, null=True)
    empower_project_contains = models.CharField(max_length=255, blank=True, null=True)
    empower_client = models.CharField(max_length=50, blank=True, null=True)
    empower_status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="Active"
    )

    # ---------- CHROMELEON FIELDS ----------
    chromeleon_module = models.CharField(max_length=50, blank=True, null=True)
    chromeleon_process = models.CharField(max_length=100, blank=True, null=True)
    chromeleon_location = models.CharField(max_length=50, blank=True, null=True)
    chromeleon_host = models.CharField(max_length=255, blank=True, null=True)

    chromeleon_username = models.CharField(max_length=50, blank=True, null=True)
    chromeleon_password = models.CharField(max_length=255, blank=True, null=True)

    chromeleon_service = models.CharField(max_length=20, blank=True, null=True)
    chromeleon_plant = models.CharField(max_length=50, blank=True, null=True)
    chromeleon_group = models.CharField(max_length=50, blank=True, null=True)

    chromeleon_project_contains = models.CharField(max_length=255, blank=True, null=True)

    chromeleon_pwd_days = models.IntegerField(blank=True, null=True)
    chromeleon_alert_days = models.IntegerField(blank=True, null=True)

    chromeleon_resume_date = models.DateField(blank=True, null=True)
    chromeleon_status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="Active"
    )

    # ---------- FLAGS ----------
    chromeleon_skip_project = models.BooleanField(default=False)
    chromeleon_data_vault = models.BooleanField(default=False)

    # ---------- AUDIT ----------
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.plant} | {self.process}"
