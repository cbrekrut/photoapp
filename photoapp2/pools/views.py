from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Photo, Comment

def index(request):
    # Отображение списка фотографий, доступных для просмотра
    photos = Photo.objects.filter(status='approved')
    return render(request, 'pools/index.html', {'photos': photos})

def photo_detail(request, photo_id):
    # Отображение деталей фотографии и комментариев к ней
    photo = Photo.objects.get(pk=photo_id)
    comments = Comment.objects.filter(photo=photo)
    
    if request.method == 'POST':
        # Обработка отправленного комментария
        text = request.POST.get('text')
        user = request.user
        Comment.objects.create(user=user, photo=photo, text=text)
    
    return render(request, 'pools/photo_detail.html', {'photo': photo, 'comments': comments})

@login_required
def upload_photo(request):
    # Загрузка новой фотографии
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        user = request.user
        Photo.objects.create(title=title, description=description, image=image, author=user, status='moderation')
        return redirect('index')
    return render(request, 'pools/upload_photo.html')

@login_required
def user_profile(request):
    # Отображение профиля пользователя и его фотографий
    user = request.user
    user_photos = Photo.objects.filter(author=user)
    return render(request, 'pools/user_profile.html', {'user': user, 'user_photos': user_photos})

# Другие представления для управления комментариями, уведомлениями и т. д.
