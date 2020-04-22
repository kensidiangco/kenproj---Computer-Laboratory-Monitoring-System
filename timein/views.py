from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Student
from .forms import StudentForm, lout
    
def user_list(request):
    students = Student.objects.filter(date__lte=timezone.now()).order_by('date')
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.timeout = None
            student.date = timezone.now()
            student.admin = request.user
            student.save()
            return redirect('user_detail', pk=student.pk)
    else:
        form = StudentForm()
        return render(request, 'user_list.html', {'form': form, 'students': students})
     
def user_form(request):
	if request.method == "POST":
		form = StudentForm(request.POST)
		if form.is_valid():
			student = form.save(commit=False)
			student.timeout = None
			student.date = timezone.now()
			student.admin = request.user
			student.save()
			return redirect('user_detail', pk=student.pk)
	else:
		form = StudentForm()
		return render(request, 'user_form.html', {'form': form})

def user_detail(request, pk):
	student = get_object_or_404(Student, pk=pk)
	if request.method == "POST":
	    form = lout(request.POST, instance=student)
	    if form.is_valid():
	        student = form.save(commit=False)
	        student.admin = request.user
	        student.timeout = timezone.now()
	        student.save()
	        return redirect('user_detail',pk=student.pk)
	else:
	    form = lout(instance=student)
	    return render(request, 'user_detail.html', {'student': student, 'form': form})
	   
def update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
	    form = StudentForm(request.POST, instance=student)
	    if form.is_valid():
	        student = form.save(commit=False)
	        student.admin = request.user
	        student.save()
	        return redirect('user_detail',pk=student.pk)
    else:
	    form = StudentForm(instance=student)
	    return render(request, 'update.html', {'student': student, 'form': form})