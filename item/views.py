from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Item, Category
from .forms import NewItemForm, EditItemForm

from django.db.models import Q


# Create your views here.
# so we are making a detail page for viewing the item when it is clicked on the index page
def detail(request, pk):  # here pk is the primary key which is going to be of item
    item = get_object_or_404(Item, pk=pk)
    # to get the related items when an item is selected is through a category similarity..
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'item/detail.html', {
        "item": item,
        "related_items": related_items,
    })


# since only logged in users can perform this add the login decorator
@login_required
def new(request):
    if request.method == "POST":
        # making the request.post and request.files to make the request post and also getting the files
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            # here in the item model we also need the user details so to get that do this before saving to the database
            # where commit false just saves it as an object rather than saving it to the database
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item:detail', pk=item.id)

    else:
        form = NewItemForm()

    return render(request, 'item/form.html', {
        "form": form,
        'title': "New Item"
    })


# to delete the item for the user
@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    return redirect('dashboard:index')


@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method == "POST":
        # making the request.post and request.files to make the request post and also getting the files
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item:detail', pk=item.id)

    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        "form": form,
        'title': "Edit Item"
    })


# This function is for the browse functionality so that the user can search for the item they want
def items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)

    if category_id:
        items = Item.objects.filter(category_id=category_id)
    if query:
        items = Item.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'item/items.html', {
        "items": items,
        "query": query,
        "categories": categories,
        "category_id": int(category_id)
    })