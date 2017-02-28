from django.core.mail import send_mail
from django.core.management.base import BaseCommand
from django.db.models import Sum

from log.models import MyUser, current_month


class Command(BaseCommand):
    commands = ['send_reports']
    args = '[command]'
    help = 'Send report'

    def handle(self, *args, **options):
        reports = MyUser.objects.filter(steps__insertion_date__month=current_month).annotate(Sum('steps')) \
            .order_by('-steps__sum')
        mail_contents_1 = '<table>%s</table>'
        table_rows = []
        for user in reports:
            table_rows.append('<tr><td>%s</td><td>%s</td></tr>' % (user.username, str(user.steps__sum)))
        mail_contents_1 = mail_contents_1 % '\n'.join(table_rows)
        print (mail_contents_1)
