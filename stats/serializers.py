from django.core.serializers import json

class PlayerSerializer(json.Serializer):
	# def end_object(self, obj):
	# 	self._current['id'] = obj._get_pk_val()
	# 	self.objects.append(self._current)
	def get_dump_object(self, obj):
		self._current['id'] = obj._get_pk_val()
		return self._current

Serializer = PlayerSerializer()
