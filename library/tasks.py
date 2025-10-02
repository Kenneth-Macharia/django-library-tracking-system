from celery import shared_task
from .models import Loan, Member
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_loan_notification(loan_id):
    try:
        loan = Loan.objects.get(id=loan_id)
        member_email = loan.member.user.email
        book_title = loan.book.title
        send_mail(
            subject='Book Loaned Successfully',
            message=f'Hello {loan.member.user.username},\n\nYou have successfully loaned "{book_title}".\nPlease return it by the due date.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[member_email],
            fail_silently=False,
        )
    except Loan.DoesNotExist:
        pass

@shared_task
def check_overdue_loans():
    loan_obj = Loan()
    loan_date = loan_obj.loan_date
    loan_date = loan_obj.due_date
    overedue_loans = Loan.objects.filter(
        is_returned=False,
        due_date__gt=loan_date
    )

    overedue_members = Member.objects.filter(
        id__in=[id for id in overedue_loans.member.id]
    )

    for member in overedue_members:
        book_title = member.loan.book.title
        member_email = member.user.email
        send_mail(
            subject='Loaned Book Return Overdue',
            message=f'Hello {member.user.username},\n\nThe loaned book"{book_title} is past its due date".\nPlease return it immediately.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[member_email],
            fail_silently=False,
        )
