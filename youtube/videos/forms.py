from django import forms 

class VideoUploadForm(forms.Form):

    title = forms.CharField(max_length=100 , widget = forms.TextInput(attrs = {
        'class' : 'form-control',
        'placeholder' : 'Enter the title'
    }))

    description = forms.CharField(max_length=100 , widget = forms.Textarea(attrs = {
        'class' : 'form-control',
        'rows' : 4
    }))

    video_file = forms.FileField(max_length=100 , widget = forms.FileInput(attrs = {
        'class' : 'form-input' ,
        'accept' : 'video/*'
    }))


    def clean_video_file(self):
        video = self.cleaned_data.get('video_file')
        if video.size > 100 * 1024 * 1024:
            raise forms.ValidationError('video file should be less than 100 MB')
        return video
    
    def clean_thumbnail_file(self):
        thumbnail = self.cleaned_data.get('thumbnail_file')
        if thumbnail.size > 1 * 1024 * 1024:
            raise forms.ValidationError('thumnail file should be less than 1 MB')
        return thumbnail
    
