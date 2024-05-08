from django.shortcuts import render
from . import sendInternalEmail

def show_form(request):
    # Assuming you have a way to generate or retrieve encoded HTML table data
    html_table_encoded = "encoded_data_here"  # This should be dynamically generated based on your specific needs

    form_url="http://127.0.0.1:8000/emailProcessor/baobo/"
    user_email = "xu9449@gmail.com"

    sendInternalEmail.sendInternalEmail(user_email, form_url)

    return render(request, 'process_data_form.html', {
        'html_table_encoded': html_table_encoded
    })

def encodeHTMLTable(df):
    html_table = df.to_html(index=False)  # Convert DataFrame to HTML table
    html_table_encoded = html_table.encode('utf-8').hex()  # Encode HTML table
    return html_table_encoded