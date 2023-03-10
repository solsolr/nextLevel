from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
#from django.http import HttpResponse #삭제
from .models import Question, Answer
from django.utils import timezone
from .form import QuestionForm, AnswerForm
from django.http import HttpResponseNotAllowed


def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)

    # return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")


def detail(request, question_id):
    question =get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)


def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # 첫 번째 방식
    # question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    # 두 번째 방식
    # answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    # answer.save()
    # 세 번째 방식
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)


def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():                         # 폼이 유효하다면
            question = form.save(commit=False)      # 임시 저장하여 question 객체를 리턴받는다.
            question.create_date = timezone.now()   # 실제 저장을 위해 작성일시를 설정한다.
            question.save()                         # 데이터를 실제로 저장한다.
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)