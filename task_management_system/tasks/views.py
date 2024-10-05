from django.shortcuts import render, redirect
from firebase_admin import auth
from .forms import TaskForm, RegisterForm, LoginForm, EditTaskForm
from datetime import datetime, date, timedelta
from django.utils.timezone import make_naive
from firebase_admin import firestore
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

db = firestore.client()

def task_list(request):
    user_id = request.session.get('user_id')
    
    if not user_id:
        return redirect('login_user')  # Nếu chưa đăng nhập, chuyển hướng về login
    
    # Truy vấn danh sách công việc từ Firestore
    tasks_ref = db.collection('users').document(user_id).collection('tasks')
    tasks = tasks_ref.stream()

    task_list = []
    for task in tasks:
        task_dict = task.to_dict()
        task_list.append({'id': task.id, **task_dict})

    # Tính thời gian còn lại
    for task in task_list:
        if task.get('deadline'):
            deadline = task['deadline']
            now = datetime.now()

            # Chuyển đổi deadline thành dạng naive để có thể trừ
            deadline_naive = make_naive(deadline)

            # Kiểm tra thời gian còn lại
            time_remaining = deadline_naive - now
            
            if time_remaining.total_seconds() <= 0:
                task['is_expired'] = True
                task['remaining_months'] = 0
                task['remaining_days'] = 0
                task['remaining_hours'] = 0
                task['remaining_minutes'] = 0
            else:
                task['is_expired'] = False

                # Tính số tháng, ngày, giờ và phút còn lại
                remaining_months = (deadline_naive.year - now.year) * 12 + (deadline_naive.month - now.month)
                remaining_days = (deadline_naive - now.replace(hour=0, minute=0, second=0, microsecond=0)).days
                remaining_hours = (time_remaining.total_seconds() % 86400) // 3600  # 86400 = 24 * 3600
                remaining_minutes = (time_remaining.total_seconds() % 3600) // 60

                task['remaining_months'] = remaining_months
                task['remaining_days'] = remaining_days
                task['remaining_hours'] = int(remaining_hours)
                task['remaining_minutes'] = int(remaining_minutes)

        else:
            task['is_expired'] = True
            task['remaining_months'] = 0
            task['remaining_days'] = 0
            task['remaining_hours'] = 0
            task['remaining_minutes'] = 0

            
            
    
    return render(request, 'task_list.html', {'tasks': task_list})

@csrf_exempt
def update_task_completion(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        completed = request.POST.get('completed') == 'true'

        user_id = request.session.get('user_id')
        task_ref = db.collection('users').document(user_id).collection('tasks').document(task_id)

        task_ref.update({'completed': completed})

        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task_data = form.cleaned_data

            # Chuyển đổi ngày từ `datetime.date` thành `datetime.datetime` nếu cần
            deadline = task_data['deadline']
            if isinstance(deadline, date):  # Kiểm tra nếu deadline là đối tượng `date`
                deadline = datetime.combine(deadline, datetime.min.time())  # Chuyển đổi thành `datetime`

            # Lưu công việc vào Firestore
            user_id = request.session.get('user_id')
            task_ref = db.collection('users').document(user_id).collection('tasks').document()
            task_ref.set({
                'name': task_data['task_name'],
                'description': task_data['description'],
                'deadline': deadline,
                'priority': task_data['priority'],
                'completed': task_data['completed'],
            })
            return redirect('task_list')
    else:
        form = TaskForm()

    return render(request, 'add_task.html', {'form': form})


def delete_task(request, task_id):
    user_id = request.session.get('user_id')
    task_ref = db.collection('users').document(user_id).collection('tasks').document(task_id)
    task = task_ref.get()

    if task.exists:  # Kiểm tra nếu tài liệu tồn tại trước khi xóa
        task_ref.delete()
        return redirect('task_list')
    else:
        return HttpResponse("Công việc không tồn tại.", status=404)

def edit_task(request, task_id):
    user_id = request.session.get('user_id')
    task_ref = db.collection('users').document(user_id).collection('tasks').document(task_id)
    task = task_ref.get().to_dict()

    if request.method == 'POST':
        form = EditTaskForm(request.POST)
        if form.is_valid():
            updated_data = form.cleaned_data
            deadline = updated_data['deadline']

            if isinstance(deadline, date):
                deadline = datetime.combine(deadline, datetime.min.time())

            # Đánh dấu hoàn thành
            if 'completed' in request.POST:
                task_ref.update({'completed': request.POST.get('completed', False)})
            
            task_ref.update(updated_data)
            return redirect('task_list')
    else:
        form = EditTaskForm(initial=task)

    return render(request, 'edit_task.html', {'form': form, 'task_id': task_id})



def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                # Firebase xác thực
                user = auth.get_user_by_email(email)
                request.session['user_id'] = user.uid
                return redirect('task_list')
            except auth.AuthError as e:
                return HttpResponse("Đăng nhập thất bại: " + str(e))
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                # Tạo người dùng mới trong Firebase
                user = auth.create_user(email=email, password=password)
                return redirect('login_user')
            except auth.EmailAlreadyExistsError:
                return HttpResponse("Email đã tồn tại.")
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
def logout_user(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return redirect('login_user')
