from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404

from .forms import VideoUploadForm
from .models import Video, VideoLike

from django.views.decorators.http import require_POST
from django.http import JsonResponse 
from .imagekit_client import get_streaming_url

from .imagekit_client import (
    upload_video,
    upload_thumbnail,
    delete_video as ik_delete_video,
)

# Create your views here.

def video_detail(request, video_id):
    video = Video.objects.get(id=video_id)
    # exprensive operation
    video.views += 1
    video.save(update_fields=["views"])
    return render(request, 'videos/detail.html', {'video': video})

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'videos/list.html', {'videos': videos})


# video upload
# Backend - API (JSON)
# Frontend
@login_required
@require_POST
def video_upload(request):
    form = VideoUploadForm(request.POST, request.FILES)
    if form.is_valid():
        video_file = form.cleaned_data['video_file']
        custom_thumbnail = request.POST.get('thumbnail_data', '')
        # Upload video to ImageKit
        try:
            try:
                video_result = upload_video(
                    file_data=video_file.read(),
                    file_name=video_file.name
                )



                base_name = video_file.name.split('.', 1)[0]
                thumbnail_file_id = ""
                thumbnail_url = ""

                try: 
                    thumbnail_result = upload_thumbnail(
                        file_data = custom_thumbnail,
                        file_name = base_name + '_thumbnail.jpg'
                    )
                    thumbnail_file_id = thumbnail_result['file_id']
                    thumbnail_url = thumbnail_result['url']
                except Exception as e:
                    print(f"Error uploading thumbnail: {e}")
                    pass

            except Exception as e:
                print(f"Error uploading video: {e}")
                return JsonResponse({
                    "success": False,
                    "error": str(e),
                })

            video = Video.objects.create(
                user=request.user,
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                file_id=video_result['file_id'],
                video_url=video_result['url'],
                streaming_url=get_streaming_url(video_result['url']),
                thumbnail_file_id=thumbnail_file_id,
                thumbnail_url=thumbnail_url,
            )

            return JsonResponse({
                "success": True,
                "video_id": video.id,
                "message": "Video uploaded successfully",
            })
        except Exception as e:
            print(f"Error creating video object: {e}")
            return JsonResponse({
                "success": False,
                "error": str(e),
            })
    #Name: Name is empty, Title: Title is required
    errors = []
    for field, field_errors in form.errors.items():
        for error in field_errors:
            errors.append(f"{field}: {error}")
    
    return JsonResponse({
        "success": False,
        "errors": ", ".join(errors),
    })

@login_required
@require_POST
def delete_video(request, video_id):
    video = get_object_or_404(Video, id=video_id, user=request.user)
    
    try:
        ik_delete_video(video.file_id)
        # # If a custom thumbnail was uploaded and stored, delete it as well
        # if getattr(video, "thumbnail_file_id", ""):
        #     ik_delete_thumbnail(video.thumbnail_file_id)
    except Exception as e:
        print("delete video error",e)
        pass
    video.delete()
    return JsonResponse({"success": True, "message": "Video deleted"})


    


@login_required
def video_upload_page(request):
    form = VideoUploadForm()
    context = {
        'form': form,
    }
    return render(request, 'videos/upload.html', context)

@login_required
@require_POST
def video_vote(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    vote_type = request.POST.get('vote')
    # like or dislike
    if vote_type not in ['like', 'dislike']:
        print('invalid vote type', vote_type)
        return JsonResponse({
            "success": False,
            "error": "Invalid vote type",
        }, status=400)

    existing_vote = VideoLike.objects.filter(user=request.user, video=video).first()
    value = VideoLike.LIKE if vote_type == "like" else VideoLike.DISLIKE


    # agr exiting choice hai to
    # do this
    # else
    # create new choice

    if existing_vote:
        print('existing_vote', existing_vote)
        if existing_vote.value == value:
            # ya to like kia ha ya dislike
            if value == VideoLike.LIKE:
                video.likes -= 1
            else:
                video.dislikes -= 1
            existing_vote.delete()
            user_vote = value
        else:
            if value == VideoLike.LIKE:
                video.like += 1
                video.dislike -= 1
            else:
                video.likes -= 1
                video.dislikes += 1
            existing_vote.value = value
            existing_vote.save()
            user_vote = value
    else:
        print('no existing vote', value)
        VideoLike.objects.create(user=request.user, video=video, value=value)

        if value == VideoLike.LIKE:
            video.likes += 1
        else:
            video.dislikes +=1

        user_vote = value

        video.save(update_fields=['likes', 'dislikes'])

    return JsonResponse({
        "success": True,
        "likes": video.likes,
        "dislikes": video.dislikes,
        "user_vote": user_vote
    })






    




