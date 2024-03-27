from django.core.paginator import Paginator

class ContactListView(ListView):
    paginate_by = 2
    model = Contact