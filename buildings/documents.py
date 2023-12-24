from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry


from buildings.models import House


@registry.register_document
class HouseDocument(Document):
    class Index:
        name = "houses"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = House

        fields = [
            "name",
            "floor",
            "window",
            "door",
            "roof",
        ]
