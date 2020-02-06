from django.shortcuts import render
from ..exception_catcher import catch
from django.http import HttpResponse, JsonResponse
from .forms import SubscriberForm
import json
from ..validators import validate_variables, email_validate
from .models import Subscriber

exception = catch(default_value=(
    HttpResponse(json.dumps({"message": "Error"}, ensure_ascii=False), content_type="application/json; encoding=utf-8",
                 status=200)))


@catch(default_value=False)
def save_on_queue(form_data: dict) -> bool:
    import pika
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', socket_timeout=5, retry_delay=5))
    channel = connection.channel()
    channel.queue_declare(queue='form_save_queue')
    channel.basic_publish(exchange='',
                          routing_key='form_save_queue',
                          body=json.dumps(form_data))
    connection.close()
    return True


class SubscriberViews:
    @staticmethod
    @exception
    def form_view(request):
        return render(request, "form.html", {"form": SubscriberForm()})

    @staticmethod
    @exception
    def save_subscriber(request):
        if request.method == "POST":
            form = SubscriberForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data.get("name")
                surname = form.cleaned_data.get("surname")
                email = form.cleaned_data.get("email")
                phone = form.cleaned_data.get("phone")
                if validate_variables(name, surname, email, phone) and email_validate(email):
                    form_data = {
                        "name": name,
                        "surname": surname,
                        "email": email,
                        "phone": phone
                    }
                    result = save_on_queue(form_data)
                    if result:
                        return render(request, "form.html", {"form": SubscriberForm()})
        return JsonResponse({"message": "Invalid Form Data"}, status=403)

    @staticmethod
    @exception
    def list_subscriber(request):
        result = []
        for record in Subscriber.select():
            result.append({
                "name": record.name,
                "surname": record.surname,
                "email": record.email,
                "phone": record.phone,
                "created_date":str(record.created_date)
            })
        return HttpResponse(json.dumps(result, ensure_ascii=False),
                            content_type="application/json; encoding=utf-8",
                            status=200)
