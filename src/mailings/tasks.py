import datetime
import logging

from celery import shared_task
from mailings.models import Mailing


@shared_task
def send_message():
    try:
        mailings = Mailing.objects.all()
        count_process_mailings = 0
        for mailing in mailings:
            phones = [client.phone for client in mailing.clients.all()]
            logging.info(f"send_sms_viber - {phones}, {mailing.mailing_text.text}")
            logging.debug("Send SMS/Viber. Success!")
            count_process_mailings += 1
            mailing.status = "SENT"
            mailing.send_date = datetime.datetime.now()
            mailing.save(update_fields=["status", "send_date"])
        return f"Finish. Count mailings for clients = {count_process_mailings}"
    except Exception as ex:
        logging.info(f"Error! {ex}")
