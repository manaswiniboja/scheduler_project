from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Scheduler
from datetime import datetime


# -------------------- LIST --------------------
def scheduler_list(request):
    schedulers = Scheduler.objects.all().order_by("-id")
    return render(request, 'scheduler/scheduler_list.html', {
        'schedulers': schedulers,
        'choices': Scheduler
    })


# -------------------- CREATE / UPDATE --------------------
def scheduler_create(request):
    if request.method != "POST":
        return redirect("scheduler_list")

    scheduler_id = request.POST.get("scheduler_id")

    process = request.POST.get("process")

    # -------------------- BASE DATA --------------------
    data = {
        # Common
        "process": process,
        "business_unit": request.POST.get("business_unit") or request.POST.get("files_business_unit"),
        "plant": request.POST.get("plant") or request.POST.get("files_plant"),
        "location": request.POST.get("location") or request.POST.get("files_location"),
        "module": request.POST.get("module") or request.POST.get("files_module"),
        "instrument": request.POST.get("instrument") or request.POST.get("files_instrument"),

        # Scheduling
        "execution_frequency": request.POST.get("execution_frequency") or request.POST.get("files_execution_frequency"),
        "interval": get_int(
            request.POST.get("interval")
            or request.POST.get("db_interval")
            or request.POST.get("files_interval")
        ),
        "uom": request.POST.get("uom") or request.POST.get("db_uom") or request.POST.get("files_uom"),

        # Connection
        "host_ip": request.POST.get("host_ip") or request.POST.get("files_host_ip"),
        "port": get_int(request.POST.get("port")),

        # DB
        "username": request.POST.get("username") or request.POST.get("db_username"),
        "password": request.POST.get("password") or request.POST.get("db_password"),
        "table_name": request.POST.get("table_name") or request.POST.get("db_table_name"),

        # Files / App
        "target_dir": request.POST.get("app_target_dir") or request.POST.get("files_target_dir"),

        # Date / Status
        "effected_from": get_date(
            request.POST.get("effected_from")
            or request.POST.get("files_effected_from")
        ),
        "status": request.POST.get("status")
        or request.POST.get("files_status")
        or request.POST.get("db_status")
        or "Active",
    }

    # -------------------- EMPOWER --------------------
    if process == "Empower Settings":
        data.update({
            "module": request.POST.get("empower_module"),
            "plant": request.POST.get("empower_plant"),
            "location": request.POST.get("empower_location"),

            "empower_module": request.POST.get("empower_module"),
            "empower_plant": request.POST.get("empower_plant"),
            "empower_location": request.POST.get("empower_location"),
            "empower_host": request.POST.get("empower_host"),
            "empower_data_source": request.POST.get("empower_data_source"),
            "empower_username": request.POST.get("empower_username"),
            "empower_password": request.POST.get("empower_password"),
            "empower_default_project": request.POST.get("empower_default_project"),
            "empower_project_contains": request.POST.get("empower_project_contains"),
            "empower_client": request.POST.get("empower_client"),
            "empower_status": request.POST.get("empower_status") or "Active",
            "status": request.POST.get("empower_status") or "Active",
        })

    # -------------------- CHROMELEON --------------------
    if process == "Chromeleon Settings":
        data.update({
            # Map to common
            "module": request.POST.get("chromeleon_module"),
            "plant": request.POST.get("chromeleon_plant"),
            "location": request.POST.get("chromeleon_location"),
            "host_ip": request.POST.get("chromeleon_host"),
            "username": request.POST.get("chromeleon_username"),
            "password": request.POST.get("chromeleon_password"),
            "effected_from": get_date(request.POST.get("chromeleon_resume_date")),
            "status": request.POST.get("chromeleon_status"),

            # Chromeleon-only
            "chromeleon_module": request.POST.get("chromeleon_module"),
            "chromeleon_location": request.POST.get("chromeleon_location"),
            "chromeleon_host": request.POST.get("chromeleon_host"),
            "chromeleon_username": request.POST.get("chromeleon_username"),
            "chromeleon_password": request.POST.get("chromeleon_password"),
            "chromeleon_service": request.POST.get("chromeleon_service"),
            "chromeleon_pwd_days": get_int(request.POST.get("chromeleon_pwd_days")),
            "chromeleon_alert_days": get_int(request.POST.get("chromeleon_alert_days")),
            "chromeleon_group": request.POST.get("chromeleon_group"),
            "chromeleon_project_contains": request.POST.get("chromeleon_project_contains"),
            "chromeleon_plant": request.POST.get("chromeleon_plant"),
            "chromeleon_status": request.POST.get("chromeleon_status"),

            #CHECKBOX 
            "chromeleon_data_vault": "chromeleon_data_vault" in request.POST,
            "chromeleon_skip_project": "chromeleon_skip_project" in request.POST,
        })

    # -------------------- SAVE --------------------
    if scheduler_id:
        Scheduler.objects.filter(id=scheduler_id).update(**data)
        messages.success(request, "Scheduler updated successfully")
    else:
        Scheduler.objects.create(**data)
        messages.success(request, "Scheduler created successfully")

    return redirect("scheduler_list")

# -------------------- EDIT --------------------
def scheduler_edit(request, pk):
    scheduler = get_object_or_404(Scheduler, pk=pk)

    return render(request, "scheduler/scheduler_list.html", {
        "schedulers": Scheduler.objects.all().order_by("-id"),
        "edit_scheduler": scheduler,   
        "choices": Scheduler
    })

# -------------------- DELETE --------------------
def scheduler_delete(request, pk):
    scheduler = get_object_or_404(Scheduler, pk=pk)
    scheduler.delete()
    messages.success(request, "Scheduler deleted successfully 🗑️")
    return redirect("scheduler_list")


# -------------------- HELPERS --------------------
def get_int(value):
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def get_date(value):
    if value:
        try:
            return datetime.strptime(value, "%Y-%m-%d").date()
        except ValueError:
            return None
    return None
