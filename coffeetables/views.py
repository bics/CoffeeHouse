from django.shortcuts import render, redirect, get_object_or_404
from .models import CoffeeTable
from .forms import CoffeeTableForm, ReplyForm, UpdateReplyForm
from django.contrib import messages
# Snippet taken from ChatGPT
from django.contrib.auth.decorators import login_required
from django.utils import timezone


# Create your views here.

# view created following tutorial made by Codemy.com
def tables(request):
    tables_list = CoffeeTable.objects.all()
    images_list = [
        'static/assets/images/table_images/coffee_drank.jpg',
        'static/assets/images/table_images/coffee_mug_cartoony.jpg',
        'static/assets/images/table_images/coffee_mug_tilted.jpg',
    ]
    if request.method == "POST":
        form = CoffeeTableForm(request.POST)
        if form.is_valid():
            # Code snippet generated using ChatGPT
            obj = form.save(commit=False)
            obj.createdBy= request.user
            obj.save()
            form.save_m2m()
            return redirect('tables')    
        else:            
            messages.success(request, ("There were some errors with some fields"))
    else:
        form = CoffeeTableForm()
        return render(request, "tables.html", {'tables_list':tables_list, 'images_list': images_list, 'form': form})
    
@login_required
def conversation(request, pk):
    # Code snippet generated using ChatGPT
    table = CoffeeTable.objects.get(pk=pk)
    replies = table.replies.all()

    reply_form = ReplyForm()
    update_reply_form = UpdateReplyForm()

    if request.method == "POST":

        if "reply-submit" in request.POST:
            reply_form = ReplyForm(request.POST)
            if reply_form.is_valid():
                obj = reply_form.save(commit=False)
                obj.createdBy= request.user
                obj.save()
                table.replies.add(obj)
                return redirect('conversation', table.id) 
            else:            
                messages.success(request, ("There were some errors with some fields"))

        elif "update-reply-submit" in request.POST:
            reply_id = request.POST.get("reply_id")
            reply = get_object_or_404(table.replies, pk=reply_id)
            old_message = reply.message
            update_reply_form = UpdateReplyForm(request.POST, instance=reply)
            if update_reply_form.is_valid():
                new_message = update_reply_form.cleaned_data["message"]
                reply.history = reply.history +"\n" + old_message
                reply.isEdited = True
                reply.timeEdited = timezone.now()
                reply.message = new_message
                reply.save(update_fields=["message", "history", "isEdited", "timeEdited"])
                return redirect('conversation', table.id) 
            else:            
                messages.success(request, ("There were some errors with some fields"))
    else:
        return render(request, "conversation.html", {"table": table, "replies": replies, "reply_form": reply_form, "update_reply_form": update_reply_form})
    
    
def close_table(request, pk):    
    table = CoffeeTable.objects.get(pk=pk)
    table.active = False
    table.save()
    return redirect('tables')

