from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.conf import settings
from django.core.mail  import send_mail

def contact(request):
    if request.method == 'POST':
        task_id = request.POST['task_id']
        task = request.POST['task']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        nurse_email = request.POST['nurse_email']

        # check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.filter(task_id=task_id, user_id=user_id).exists()
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this task')
                return redirect('/tasks/'+task_id)

        # Utilisez un nom de variable différent pour éviter le conflit
        new_contact = Contact(task=task, task_id=task_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
        new_contact.save()

        # send email
        send_mail(
            'Property task Inquiry',
            'There has been an inquiry for ' + task + '. Sign into the admin panel for more info',
            settings.EMAIL_HOST_USER,  
            [nurse_email, settings.EMAIL_HOST_USER],

            fail_silently=False
        )

        messages.success(request,'Your request has been submitted, a nurse will get back to you soon')
        return redirect('/tasks/'+task_id)

