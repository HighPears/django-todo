from .models import Todo
from .forms import AddForm, EditForm

from django.views import generic
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


# Create your views here.
class IndexView(generic.ListView):
    model = Todo
    context_object_name = "todo_list"
    template_name = "todo/index.html"
    form_class = AddForm

    def get_queryset(self):
        queryset = Todo.objects.all()
        if "visible" in self.request.GET:
            if self.request.GET["visible"] == "open":
                queryset = queryset.filter(todo_visible=True)
            elif self.request.GET["visible"] == "close":
                queryset = queryset.filter(todo_visible=False)
        else:
            queryset = queryset.filter(todo_visible=True)
        if "words" in self.request.GET:
            queryset = queryset.filter(
                todo_title__contains=self.request.GET["words"]
            )
        return queryset.order_by("-published_date")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class
        if "visible" in self.request.GET:
            context["visible"] = self.request.GET["visible"]
        if "words" in self.request.GET:
            context["words"] = self.request.GET["words"]
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse("todo:index"))
        else:
            return self.form_invalid(form)


class EditView(generic.UpdateView):
    model = Todo
    template_name = "todo/edit.html"
    form_class = EditForm
    success_url = reverse_lazy("todo:index")


class DeleteView(generic.DeleteView):
    model = Todo
    template_name = "todo/delete.html"
    success_url = reverse_lazy("todo:index")
