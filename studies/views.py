from rest_framework import viewsets
from .models import Study, Subject
from .serializers import StudySerializer, SubjectSerializer
from django.views.decorators.csrf import csrf_exempt
from studies import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger('frontend_logger')

class LogFrontendMessages(APIView):
    def post(self, request):
        try:
            log_message = request.data.get('message', '')
            log_level = request.data.get('level', '').upper()
            
            # Log the message based on the level
            if log_level == 'ERROR':
                logger.error(log_message)
            elif log_level == 'WARNING':
                logger.warning(log_message)
            elif log_level == 'DEBUG':
                logger.debug(log_message)
            else:
                logger.info(log_message)
                
            return Response({'status': 'Logged successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f'Error logging frontend message: {e}')
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class StudyViewSet(viewsets.ModelViewSet):
    queryset = Study.objects.all()
    serializer_class = StudySerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    def perform_create(self, serializer):
        # Fetch the study using the ID from the request data
        study_id = self.request.data.get('study')
        try:
            study = Study.objects.get(id=study_id)  # Retrieve the study based on the ID
        except Study.DoesNotExist:
            raise serializers.ValidationError("Study with the given ID does not exist.")
        
        # Now save the subject with the associated study
        serializer.save(study=study)


