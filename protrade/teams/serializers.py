from shared.serializers import BaseSerializer


class TeamSerializer(BaseSerializer):
    def __init__(self, to_serialize, *, fields=[], request=None):
        super().__init__(to_serialize, fields=fields, request=request)

    def serialize_instance(self, instance) -> dict:
        return {
            'id': instance.pk,
            'name': instance.name,
            'slug': instance.slug,
            'shield': self.build_url(instance.shield.url),
            'league': instance.get_league_display(),
        }
