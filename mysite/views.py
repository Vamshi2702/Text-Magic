from django.http import HttpResponse, response
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    wordcount = request.GET.get('wordcount','off')
    charcount = request.GET.get('charcount','off')
    upperCase = request.GET.get('uppercase','off')
    lowerCase = request.GET.get('lowercase','off')
    newlines = request.GET.get('newline','off')     
    extraspace = request.GET.get('extraspace','off')
    _extraspace = request.GET.get('_extraspace','off')
    char_count = 0
    original_text = djtext
    params = {'analyzed_count': "#", 'analyzed_charcount': "#", 'original_text': original_text}
    
    
    if wordcount == 'on':
        analyzed_count = len(djtext.strip().split(" "))
        params = {'analyzed_count': analyzed_count,'analyzed_text': djtext, 'original_text': original_text}
        
    if charcount == 'on':
        for char in djtext:
            if char != ' ' or char != '  ' or char != '   ':
                char_count += 1
        analyzed_charcount = char_count
        params = {'analyzed_count': analyzed_count, 'analyzed_charcount': analyzed_charcount,'analyzed_text': djtext, 'original_text': original_text}
        
    if removepunc == 'on':
        punctuations = '''’'`+"=()[]\{\}<>:,‒–—―…!.«»-‐?‘’“”;/⁄␠·&@*\•^¤¢$€£¥₩₪†‡°¡¿¬#№%‰‱¶′§~¨_|¦⁂☞∴‽※'''
        analyzed_text = ''
        for char in djtext:
            if char not in punctuations:
                analyzed_text += char
        djtext = analyzed_text
        params = {'analyzed_count': analyzed_count, 'analyzed_charcount': analyzed_charcount,'analyzed_text': djtext, 'original_text': original_text}
        
    if upperCase == 'on':
        analyzed_text = ''
        for char in djtext:
                analyzed_text += char.upper()
        djtext = analyzed_text
        params = {'analyzed_count': analyzed_count, 'analyzed_charcount': analyzed_charcount,'analyzed_text': djtext, 'original_text': original_text}
    
    if lowerCase == 'on':
        analyzed_text = ''
        for char in djtext:
                analyzed_text += char.lower()
        djtext = analyzed_text
        params = {'analyzed_count': analyzed_count, 'analyzed_charcount': analyzed_charcount,'analyzed_text': djtext, 'original_text': original_text}
    
    if newlines == 'on':
        analyzed_text = ''
        for char in djtext:
            if char != '\n' and char != "\r":
                analyzed_text += char
        djtext = analyzed_text
        params = {'analyzed_count': analyzed_count, 'analyzed_charcount': analyzed_charcount,'analyzed_text': djtext, 'original_text': original_text}
        
    if extraspace == 'on':
        analyzed_text = djtext.replace(" ","")
        djtext = analyzed_text
        params = {'analyzed_count': analyzed_count, 'analyzed_charcount': analyzed_charcount,'analyzed_text': djtext, 'original_text': original_text}
        
    if _extraspace == 'on':
        analyzed_text = ''
        for char in djtext:
            if char!='  ' and char!='   ' and char!='    ' and char!='     ' and char!='      ' and char!='       ':
                analyzed_text += char
        djtext = analyzed_text
        params = {'analyzed_count': analyzed_count, 'analyzed_charcount': analyzed_charcount,'analyzed_text': djtext, 'original_text': original_text}
        
    if wordcount != 'on' and extraspace != 'on' and newlines != 'on' and upperCase != 'on' and removepunc != 'on' and charcount != 'on':
        return render(request, 'index.html')
    
    return render(request,'analyze.html',params)