from .models import Course


def get_all_course_child():
    cur_course = Course.objects.get(id=1)
    print(cur_course)
    cur_modules = cur_course.module_course.get(id=2)
    print(cur_modules)

    return 'ok'