from django.shortcuts import render

# Create your views here.
# from . import infix
from Converter.infixAlgo import *


def findResult(request):
    data = dict(request.POST)  # convert data into dictionary
    infix = InfixConverter()  # create instance
    expr = data['exp']  # take expression list
    s1 = ""
    ans = list(expr)

    for i in expr:  # convert expression into string
        s1 += i

    postFix = infix.toPostfix(s1)  # find postfix expression
    preFix = infix.toPrefix(s1)  # find prefix expression

    # check if type is selected
    if 'type' in data:
        if data['type'] == ['postfix']:  # postfix
            ans.append(postFix)
        elif data['type'] == ['prefix']:  # prefix
            ans.append(preFix)
        elif data['type'] == ['evalprefix']:  # evaluate prefix expression
            result = infix.evaluatePrefix(s1)
            ans.append(result)
        elif data['type'] == ['evalpostfix']:  # evaluate postfix expression
            r1 = infix.evaluatePostfix(s1)
            ans.append(r1)

    else:  # if type is not present
        ans.append(preFix)
        ans.append(postFix)

    return ans


def index(request):
    answer = []
    resultLen = 0
    ln = 0
    conversion = findConversion(request)
    # check if results session is not present then create new one
    if "results" not in request.session:
        request.session["results"] = []
        ln = len(request.session["results"])

    # check if submit button is clicked
    if 'submit' in request.POST:
        result = findResult(request)
        request.session["results"] += [result]
        resultLen = len(result)
        ln = len(result)
        answer = request.session["results"][len(
            request.session["results"]) - 1]

    return render(request, "Converter/index.html", {
        'Result': request.session["results"],
        'finalAnswer': answer,
        'length': ln,
        'choice': conversion
    })


def findConversion(request):
    s2 = ""

    data = dict(request.POST)
    if 'type' in data:
        choice = data['type']
    else:
        choice = 'two'

    for c in choice:
        s2 += c
    return s2
