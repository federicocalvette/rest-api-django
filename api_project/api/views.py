from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Course
import json

# Create your views here.


class CourseView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            courses = list(Course.objects.filter(id=id).values())
            if len(courses) > 0:
                course = courses[0]
                datos = {
                    'status': 'success',
                    'message': 'Success',
                    'course': course
                }
            else:
                datos = {
                    'status': 'error',
                    'message': 'course not found'
                }
            return JsonResponse(datos)
        else:
            courses = list(Course.objects.values())

            if len(courses) > 0:
                datos = {
                    'status': 'success',
                    'message': 'Success',
                    'courses': courses
                }
            else:
                datos = {
                    'status': 'error',
                    'message': 'courses not found'
                }
            return JsonResponse(datos)

    def post(self, request):

        jd = json.loads(request.body)

        Course.objects.create(
            name=jd['name'],
            category=jd['category'],
            company=jd['company'],
            url=jd['url']
        )

        datos = {
            'status': 'success',
            'message': 'Course added',
        }

        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)

        courses = list(Course.objects.filter(id=id).values())

        if len(courses) > 0:
            course = Course.objects.get(id=id)
            course.name = jd['name']
            course.category = jd['category']
            course.company = jd['company']
            course.url = jd['url']

            course.save()  # Save changes

            datos = {
                'status': 'success',
                'message': 'Couse updated'
            }
        else:
            datos = {
                'status': 'error',
                'message': 'course not found'
            }
        return JsonResponse(datos)

    def delete(self, request, id):
        
        courses = list(Course.objects.filter(id=id).values())

        if len(courses) > 0:
            Course.objects.filter(id=id).delete()
            datos = {
                'status': 'success',
                'message': 'Course deleted'
            }
        else:
            datos = {
                'status': 'error',
                'message': 'course not found'
            }
        return JsonResponse(datos)