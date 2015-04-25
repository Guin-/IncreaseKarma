from django.shortcuts import render, render_to_response
#import templates

def main_page(request):
    return render(request, 'index.html')



