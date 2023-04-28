from django.http import HttpResponse, JsonResponse, FileResponse
from django.db.models import ObjectDoesNotExist
from .models import ScholarBasicInfo, TeacherStudents, Papers, ByAuthorPaper

import os

avatar_path = "/home/data/SmartCampus/Campus/src/main/webapp/teacher_img"
name_set = set(fname.split('.')[0] for fname in os.listdir(avatar_path))


def err_response(code, msg):
    response = HttpResponse(msg)
    response.status_code = code
    return response


def basic_info(request):
    sid = int(request.GET.get('scholar_id', -1))
    name = request.GET.get('name', "")

    if sid != -1:
        try:
            scholar = ScholarBasicInfo.objects.get(pk=int(sid))
            return JsonResponse(scholar.get_dict())
        except ObjectDoesNotExist:
            return err_response(404, "Scholar id {} doesn't exist.".format(sid))
    elif name != "":
        try:
            scholar = ScholarBasicInfo.objects.get(chinese_name=name)
            return JsonResponse(scholar.get_dict())
        except ObjectDoesNotExist:
            return err_response(404, "Scholar {} doesn't exist.".format(name))
    else:
        return err_response(404, "No argument provided")


def get_avatar_by_name(name):
    if name not in name_set:
        return err_response(404, "{} doesn't exist".format(name))
    else:
        f = open(os.path.join(avatar_path, name + ".jpg"), "rb")
        response = FileResponse(f)
        return response


def avatar(request):
    sid = int(request.GET.get('scholar_id', -1))
    name = request.GET.get('name', "")

    if name != '':
        return get_avatar_by_name(name)
    elif sid != -1:
        try:
            scholar = ScholarBasicInfo.objects.get(pk=sid)
            name = scholar.chinese_name
            return get_avatar_by_name(name)
        except ObjectDoesNotExist:
            return err_response(404, "Scholar {} doesn't exist.".format(name))
    else:
        return err_response(404, "No argument provided")


def teacher_students(request):
    if 'name' not in request.GET:
        return err_response(404, "No argument provided")

    name = request.GET['name']
    try:
        students = TeacherStudents.objects.get(name=name).students
        students = students.split('|')
        return JsonResponse({"teacher": name, "students": students})
    except ObjectDoesNotExist:
        return err_response(404, "{} doesn't exists.".format(name))


def papers(request):
    if 'name' not in request.GET:
        return err_response(404, "No argument provided")

    name = request.GET['name']
    try:
        papers = ByAuthorPaper.objects.filter(by_author=name)
        papers = [Papers.objects.get(id=paper.paper_id) for paper in papers]
        papers = [paper.get_dict() for paper in papers]
        return JsonResponse({"scholar": name, "papers": papers})
    except ObjectDoesNotExist:
        return err_response(404, "{} doesn't exists.".format(name))
