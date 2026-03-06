from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.models import CustomUser
# from fedback.models import Feedback
# from course.models import Course

class ShowStatistic(APIView):
    def get(self, request):
        # teachers = Instructor.objects.count()
        # leaders = Leader.objects.count()
        # feedbacks = Feedback.objects.count()
        # courses = Course.objects.count()
        users = CustomUser.objects.count()

        data = {
            "Users": users
            # "teachers_count": teachers,
            # "leaders_count": leaders,
            # "feedback_count": feedbacks,
            # "courses_count": courses
        }


        return Response(data, status=status.HTTP_200_OK)