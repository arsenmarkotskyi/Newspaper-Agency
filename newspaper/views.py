from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from newspaper.forms import NewspaperForm, RedactorForm, NewspaperSearchForm, RedactorSearchForm, TopicSearchForm
from newspaper.mixans import SearchMixin
from newspaper.models import Topic, Newspaper, Redactor


def index(request: HttpRequest) -> HttpResponse:
    topics = Topic.objects.all()
    newspapers = Newspaper.objects.all()
    return render(request, "newspaper/index.html", {'topics': topics, 'newspapers': newspapers})


class TopicListView(LoginRequiredMixin, SearchMixin, generic.ListView):
    model = Topic
    template_name = "newspaper/topic_list.html"
    paginate_by = 5
    search_form_class = TopicSearchForm
    search_fields = ["name"]


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("newspaper:topic-list")
    template_name = "newspaper/topic_form.html"


class NewspaperByTopicView(LoginRequiredMixin, generic.ListView):
    model = Newspaper
    template_name = "newspaper/newspaper_by_topic.html"
    context_object_name = "newspapers"
    paginate_by = 5

    def get_queryset(self):
        pk = self.kwargs["pk"]
        return Newspaper.objects.filter(topics__id=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["topic"] = Topic.objects.get(pk=self.kwargs["pk"])
        return context


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("newspaper:topic-list")


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("newspaper:topic-list")


class NewspaperListView(LoginRequiredMixin, SearchMixin, generic.ListView):
    model = Newspaper
    template_name = "newspaper/newspaper_list.html"
    paginate_by = 5
    search_form_class = NewspaperSearchForm
    search_fields = ["title"]
    queryset = Newspaper.objects.prefetch_related("topics", "publishers")


class NewspaperDetailView(LoginRequiredMixin, generic.DetailView):
    model = Newspaper
    template_name = "newspaper/newspaper_detail.html"


class NewspaperCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    form_class = NewspaperForm
    template_name = "newspaper/newspaper_form.html"
    success_url = reverse_lazy("newspaper:newspaper-list")


class NewspaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    form_class = NewspaperForm

    def get_success_url(self):
        return reverse_lazy("newspaper:newspaper-detail", kwargs={"pk": self.object.pk})


class NewspaperDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("newspaper:newspaper-list")


class RedactorListView(LoginRequiredMixin, SearchMixin, generic.ListView):
    model = Redactor
    template_name = "newspaper/redactor_list.html"
    paginate_by = 5
    search_form_class = RedactorSearchForm
    search_fields = ["username"]


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor
    template_name = "newspaper/redactor_detail.html"


class RedactorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Redactor
    form_class = RedactorForm
    success_url = reverse_lazy("newspaper:redactor-list")


class RedactorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Redactor
    form_class = RedactorForm

    def get_success_url(self):
        return reverse_lazy("newspaper:redactor-detail", kwargs={"pk": self.object.pk})


class RedactorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Redactor
    success_url = reverse_lazy("newspaper:redactor-list")
