from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from .models import Student
from django.urls import reverse_lazy

# Create your views here.

from django.views.generic import TemplateView






class StudentListView(ListView):
    model = Student
    template_name = "students.html"
    context_object_name = "students"
    paginate_by = 5
    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Student.objects.filter(name__icontains=query)
        return Student.objects.all()

class StudentDetailView(DetailView):
    model = Student
    template_name = "student_detail.html"


class StudentCreateView(CreateView):
    model=Student
    fields=["name","age","email","roll_no","profile_pic"]
    template_name="student_form.html"
    success_url=reverse_lazy("student_list")

class StudentUpdateView(UpdateView):
    model = Student
    fields=["name","age","email","roll_no","profile_pic"]
    template_name = "student_form.html"
    success_url = reverse_lazy('student_list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = "student_confirm_delete.html"
    success_url = reverse_lazy('student_list')