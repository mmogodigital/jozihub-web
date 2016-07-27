import csv
from django.http import HttpResponse
from app.authentication.models import EndUser


def export_view(request):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    writer = csv.writer(response)
    users = EndUser.objects.all()
    writer.writerow(['First Name', 'Last Name', 'Company', 'Email', 'Date Joined'])
    for user in users:
        writer.writerow([
            user.first_name,
            user.last_name,
            user.company,
            user.email,
            str(user.date_joined)])

    return response
