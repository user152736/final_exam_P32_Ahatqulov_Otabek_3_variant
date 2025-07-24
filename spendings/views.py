from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .form import CustomSpendingForm
from .models import SpendingesModel
@login_required
def home(request):
    spendinges = SpendingesModel.objects.all()
    return  render(request, 'spendings/home.html', context={'spendinges':spendinges})

def create(request):

    if request.method == 'POST':
        form = CustomSpendingForm(request.POST)

        if form.is_valid():
            hold = form.save(commit=False)
            hold.author = request.user
            hold.save()
            return redirect('home')

    else:
        form = CustomSpendingForm()

    return render(request, 'spendings/create.html', context={'form':form})


def view(request, card_id):

    card = get_object_or_404(SpendingesModel, id=card_id)

    return render(request, 'spendings/view.html', context={'card':card})


def update(request, card_id):
    card = get_object_or_404(SpendingesModel, id=card_id)
    if request.method == 'POST':
        form = CustomSpendingForm(request.POST, instance=card)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomSpendingForm(instance=card)
    return render(request, 'spendings/update.html', context={'form':form, 'card':card})


def delete(request, card_id):
    card = get_object_or_404(SpendingesModel, id=card_id)
    card.delete()
    return redirect('home')

