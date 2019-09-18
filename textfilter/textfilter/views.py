# created by AaRoN

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(reuqest):
    return render(reuqest, 'about.html')


def contact(reuqest):
    return render(reuqest, 'contact.html')


def error(request):
    return render(request, 'error.html')


def analyse(request):
    djtext = request.GET.get('text', 'default')
    remove = request.GET.get('remove', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    smallcaps = request.GET.get('smallcaps', 'off')
    newlineremove = request.GET.get('newlineremove', 'off')
    extraspaceremove = request.GET.get('extraspaceremove', 'off')
    charactercount = request.GET.get('charactercount', 'off')

    punctuations = ''' !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '''
    analysed = " "
    if remove == 'on':
        for char in djtext:
            if char not in punctuations:
                analysed = analysed + char

        params = {'purpose': 'Punctuated', 'analysed_text': analysed}
        return render(request, 'analyse.html', params)

    elif (fullcaps == 'on'):
        analysed = ''
        for char in djtext:
            analysed = analysed + char.upper()

        params = {'purpose': 'Capitalized Text', 'analysed_text': analysed}
        return render(request, 'analyse.html', params)

    elif (smallcaps == 'on'):
        analysed = ''
        for char in djtext:
            analysed = analysed + char.lower()

        params = {'purpose': 'LowerCase Text', 'analysed_text': analysed}
        return render(request, 'analyse.html', params)

    elif (newlineremove == 'on'):
        analysed = ''
        for char in djtext:
            if (char != "/n"):
                analysed = analysed + char

        params = {'purpose': 'REMOVED NEW LINES', 'analysed_text': analysed}
        return render(request, 'analyse.html', params)

    elif (extraspaceremove == 'on'):
        analysed = ''
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analysed = analysed + char

        params = {'purpose': 'REMOVED SPACE', 'analysed_text': analysed}
        return render(request, 'analyse.html', params)


    elif (charactercount == 'on'):
        count = 0
        current = ""
        for i in djtext:
            count += 1

        write = "THE COUNT IS {}".format(count)

        params = {'purpose': 'CHARACTER COUNT', 'analysed_text': write}
        return render(request, 'analyse.html', params)

    else:
        return render(request, 'error.html')
