from django.shortcuts import render
from django.http import HttpResponse
from .models import Question,Marks,Student,currentuser
# Create your views here.

def register_admin(request):
    return HttpResponse("Register Admin")

def register(request):
    register_no = request.POST.get('register_no')
    print("\n\n"+str(register_no)+"\n\n")
    try:
        s = Student.objects.create(register_no = register_no)
        s.student_name = request.POST.get('student_name','')
        print("\n\n"+s.student_name+"\n\n")
        sname=s.student_name
        s.student_email = request.POST.get('student_email','')
        print("\n\n"+s.student_email+"\n\n")
        s.password = request.POST.get('password','')
        print("\n\n"+s.password+"\n\n")
        s.save()
        m = Marks.objects.create(register_no=register_no,student_name = sname,marks_value=0)
        print("\n\n"+m.register_no+"\n\n")
        print("\n\n"+m.student_name+"\n\n")
        print("\n\n"+m.marks_value+"\n\n")
        m.save()
        for i in currentuser.objects.all():
            i.register_no=register_no
            i.save()
        return render(request, 'demoapp/register.html', {})
    except:
        return render(request, 'demoapp/register.html', {})

def login(request):
    try:
        reg = request.POST.get('register_no')
        print("\n\n"+str(reg)+"\n\n")
        s = Student.objects.get(register_no = reg)
        print("\n\n"+str(register_no)+"\n\n")
        for i in currentuser.objects.all():
            i.register_no=reg
            i.save()
        print("\n\n"+str(register_no)+"\n\n")
        if(s.password==request.POST.get('password','')):
            return HttpResponse("Student logged in")
        print("\n\n"+s.student_email+"\n\n")
        print("\n\n"+s.password+"\n\n")
        return render(request, 'demoapp/login.html', {})
    except:
        return render(request, 'demoapp/login.html', {"error_message":"error_occured"})

def index(request):
    question_list = Question.objects.all()
    context = {}
    context['question_list']=question_list
    return render(request, 'demoapp/index.html',context)

def generate_results(request):
    for i in currentuser.objects.all():
        register_no=i.register_no
    m = Marks.objects.get(register_no = register_no)
    marks = m.marks_value
    response = "Your result is generated :D"
    return render(request, 'demoapp/result_page.html', {
        'results':marks
    })

def answer(request, question_no):
    new_marks = 0
    for i in currentuser.objects.all():
        register_no=i.register_no
    m = Marks.objects.get(register_no=register_no)
    try:
        q = Question.objects.get(pk=question_no)
        print("\n\n"+"question_no "+str(question_no)+"\n\n")
        ans = request.POST['choice']
        print("\n\n"+request.POST['choice']+"\n\n")
        if int(ans)==1:
            print("\n\n"+"Yaaay!"+"\n\n")
            if q.answer==q.answer_choice_one:
                print("\n\n"+"Yaaay!"+"\n\n")
                new_marks+=1
                m.marks_value = new_marks
                print("\n\n"+str(m.marks_value)+"\n\n")
                m.save()
        elif int(ans)==2:
            if q.answer==q.answer_choice_two:
                new_marks+=1
                m.marks_value = new_marks
                print("\n\n"+str(m.marks_value)+"\n\n")
                m.save()
        elif int(ans)==3:
            if q.answer==q.answer_choice_three:
                new_marks+=1
                m.marks_value = new_marks
                print("\n\n"+str(m.marks_value)+"\n\n")
                m.save()
        elif int(ans)==4:
            if q.answer==q.answer_choice_four:
                new_marks+=1
                m.marks_value = new_marks
                print("\n\n"+str(m.marks_value)+"\n\n")
                m.save()
        else:
            pass
        marks = str(new_marks)
        print("\n\n"+marks+"\n\n")
        return render(request, 'demoapp/answer.html', {
            'new_marks':marks
        })
    except:
        return HttpResponse("Some Error occured")


def exam(request, question_no):
    context = {}
    choice_list = []
    q = Question.objects.get(question_no = question_no)
    choice_list.append(q.answer_choice_one)
    choice_list.append(q.answer_choice_two)
    choice_list.append(q.answer_choice_three)
    choice_list.append(q.answer_choice_four)
    context['question']=q
    context['choice_list']=choice_list
    return render(request, 'demoapp/exam_page.html', context)
