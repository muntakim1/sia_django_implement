import aiml
from django.shortcuts import render, redirect

kernel = aiml.Kernel()
kernel.learn("./botbrains/*.aiml")
kernel.saveBrain("siabrain.brn")


def index(request):
    text = ""
    textreply = ""

    text = chat.text
    textreply = kernel.respond(str(text))
    if textreply is not None:
        return render(request, "chat.html", {'message': textreply, 'send': text, })
    else :
        textreply = "I don't understand"
        return render(request, "chat.html", {'message': textreply, 'send': text, })


def chat(request):
    chat.text = request.POST.get('text')
    print(chat.text)
    return redirect("index")
