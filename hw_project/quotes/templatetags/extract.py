from bson.objectid import ObjectId
from django import template
from ..utils import get_mongodb

register = template.Library()

def get_author(id_):
    db = get_mongodb()
    author = db.authors.find_one({'_id': ObjectId(id_)})
    return author['fullname']

register.filter('author', get_author)

# @login_required
# def add_author(request):
#     if request.method == 'POST':
#         form = AuthorForm(request.POST)
#         if form.is_valid():
#             form.save()
#             fullname = form.cleaned_data['fullname']
#             messages.success(request, f'Author {fullname} added successfully.')
#             return  render(request, 'quotes/add_author.html', context={'form': AuthorForm()})
#         else:
#             messages.error(request, 'Author is not added.')
#             return render(request, 'quotes/add_author.html', context={'form': form})
#     return render(request, 'quotes/add_author.html', context={'form': AuthorForm()})