import graphene
from moovies.api.schema import Query as MovieQuery
from moovies.api.schema import Mutation as MovieMutation


class Query(MovieQuery, graphene.ObjectType):
    pass


class Mutation(MovieMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
