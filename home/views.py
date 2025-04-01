from django.shortcuts import render
from home.models import TodoList
from django.http import JsonResponse

# Create your views here.
def homePage(request):
    if request.method == 'POST':
        # Collect data from the form
        task_name = request.POST.get('task_name')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        priority = request.POST.get('priority')
        is_complete = 'is_complete' in request.POST
        
        # Create a new TodoList item
        new_task = TodoList(
            task_name=task_name,
            description=description,
            due_date=due_date,
            priority=priority,
            is_complete=is_complete
        )
        new_task.save()
    
    # Get all Todo items to display
    tasks = TodoList.objects.all()
    for each in tasks:
        print(each.description)
    # Render the page with the tasks and the form
    return render(request, 'index.html', {'tasks': tasks})
def update_task(request, task_id):
    if request.method == 'POST':
        task = TodoList.objects.get(id=task_id)
        task.is_complete = True
        task.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})