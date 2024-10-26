from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError

from .models import Cat, Mission, Target
from .serializers import CatSerializer, MissionSerializer, TargetSerializer

class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

    @action(detail=True, methods=['post'])
    def assign_cat(self, request, pk=None):
        mission = self.get_object()
        cat_id = request.data.get('cat_id')
        try:
            cat = Cat.objects.get(id=cat_id)
            mission.cat = cat
            mission.save()
            return Response({'status': 'Cat assigned successfully'})
        except Cat.DoesNotExist:
            return Response({'error': 'Cat not found'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['post'])
    def complete_mission(self, request, pk=None):
        mission = self.get_object()
        mission.check_completion()
        mission.save()
        return Response({'status': 'Mission status updated to complete'})

    def destroy(self, request, *args, **kwargs):
        mission = self.get_object()

        if mission.cat is not None:
            return Response(
                {'error': 'Cannot delete mission because it is assigned to a cat.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        mission.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TargetViewSet(viewsets.ModelViewSet):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer

    def update(self, request, *args, **kwargs):
        target = self.get_object()
        if target.is_complete:
            return Response({'error': 'Cannot update notes on a completed target'}, status=status.HTTP_404_NOT_FOUND)
        return super().update(request, *args, **kwargs)
    
    def mark_complete(self, request, *args, **kwargs):
        target = self.get_object()
        
        if target.is_complete:
            return Response({'error': 'Target is already marked as complete.'}, status=status.HTTP_400_BAD_REQUEST)

        target.is_complete = True
        target.save()

        return Response({'status': 'Target marked as complete.'}, status=status.HTTP_200_OK)