from django.core.mail import send_mail
from django.core.management.base import BaseCommand
from django.db.models import Sum

from log.models import current_month, MyUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        reports = MyUser.objects.filter(steps__insertion_date__month=current_month).annotate(Sum('steps')) \
            .order_by('-steps__sum')
        mail_contents_1 = '<table>%s</table>'
        table_rows = []
        user_mail_list = []
        for user in reports:
            table_rows.append('<tr><td>%s</td><td>%s</td></tr>' % (user.username, str(user.steps__sum)))
        mail_contents_1 = mail_contents_1 % '\n'.join(table_rows)

        send_mail(
            'Edetabel',
            '',
            'sammudsamm@gmail.com',
            # settings.EMAIL_HOST_USER,  # List of email addresses also accepted,
            user_mail_list,
            fail_silently=False,
            html_message=mail_contents_1
        )


