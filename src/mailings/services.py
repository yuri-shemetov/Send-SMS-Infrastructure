import datetime

from django.db.models import QuerySet

from letters.models import Letter
from mailings.models import Mailing


def sending_router(mailing_text: Letter, clients: QuerySet, send_date=None):
    # for client in clients:
    #     recipient_list = [client.email]
    #     send_message(
    #         title=mailing_text.title,
    #         recipient_list=recipient_list,
    #         text=mailing_text.text,
    #     )
    # Mailing.active.create(
    #     mailing_text=mailing_text,
    #     clients=clients,
    #     send_date=datetime.datetime.now(),
    #     status="SENT",
    # )
    pass
