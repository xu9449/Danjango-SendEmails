from django.http import HttpResponse
from . import sendInternalEmail

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def handle_click(request):
    # add your data manipulate here

    user_email = 'xu9449@gmail.com'
    form_url = "Bob is a BangBiao!!!!!"
    sendInternalEmail.sendData(user_email, form_url)

def baobo(request):
    return HttpResponse("Hi Bo, this is how to use url (Views)")





    # if request.method == "POST":
    #     data = json.loads(request.body)
    #     html_table = data['html_table']
    #     df = pd.read_html(html_table)[0]  # Convert HTML table back to DataFrame

    #     # Perform your DataFrame manipulations here
    #     df['new_column'] = df['existing_column'] * 2

    #     # Simulate sending an email
    #     send_email(df.to_html())  # Function to send an email

    #     return JsonResponse({'status': 'success'}, status=200)
    # return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

