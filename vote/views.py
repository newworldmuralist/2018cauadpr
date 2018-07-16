from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Ad_tv, Ad_viral


# Create your views here.
def index(request):
	return render(request, 'vote/index.html')

#영상광고
def tv(request):
	tv_candidates = Ad_tv.objects.all()			# 모든 리스트를 받아온다.

	if request.POST:	# 요청이 들어왔을 때
		tv_id = request.POST.getlist('tv_id')	# vid_id는 선택된 영상의 이름

		for tv_id in tv_id:
			tv = Ad_tv.objects.get(id=tv_id)	# vid는 vid_id와 이름이 같은 영상
			
			tv.result += 1
			tv.save()
			
		return HttpResponseRedirect('/viral')

	context_dict = {
		'tv_candidates': tv_candidates
	}

	return render(request, 'vote/tv.html', context_dict)

#브랜디드엔터테인먼트
def viral(request):
	viral_candidates = Ad_viral.objects.all()

	if request.POST:
		viral_id = request.POST.get('viral_id')

		viral = Ad_viral.objects.get(id=viral_id)
		
		viral.result += 1
		viral.save()

		return HttpResponseRedirect('/exit')

	context_dict = {
		'viral_candidates': viral_candidates
	}

	return render(request, 'vote/viral.html', context_dict)


def exit(request):
	return render(request, 'vote/exit.html')



def result(request):
	tv_candidates = Ad_tv.objects.all()
	viral_candidates = Ad_viral.objects.all()

	context_dict = {
		'tv_candidates': tv_candidates,
		'viral_candidates': viral_candidates,
	}

	return render(request, 'vote/result.html', context_dict)











