from django.shortcuts import render


def main(request):
    data = {}
    return render(request, 'main.html', data)
