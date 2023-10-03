import graphene
from moovies.api.schema import Query as MovieQuery


class Query(MovieQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
