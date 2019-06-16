import graphene
import requests
from graphene_django.types import DjangoObjectType, ObjectType
from .models import Users

# Create a GraphQL type for the users model


class UserType(DjangoObjectType):
    class Meta:
        model = Users


class Text(graphene.ObjectType):
    text = graphene.String()
# Create a Query type


class Query(ObjectType):
    user = graphene.Field(UserType, id=graphene.Int())
    users = graphene.List(UserType)

    def resolve_user(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Users.objects.get(pk=id)

        return None

    def resolve_users(self, info, **kwargs):
        return Users.objects.all()


# Create Input Object Types


class userInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()

# Create mutations for users


class SendText(graphene.Mutation):
    text = graphene.String()

    class Arguments:
        text = graphene.String()

    @staticmethod
    def mutate(root, info, text):
        r = requests.get(f'http://www.boredapi.com/api/activity?type={text}')
        print(r.text)
        return SendText(text=r.text)


class Createuser(graphene.Mutation):
    class Arguments:
        input = userInput(required=True)

    ok = graphene.Boolean()
    user = graphene.Field(UserType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        user_instance = user(name=input.name)
        user_instance.save()
        return Createuser(ok=ok, user=user_instance)


class Updateuser(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = userInput(required=True)

    ok = graphene.Boolean()
    user = graphene.Field(UserType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        user_instance = Users.objects.get(pk=id)
        if user_instance:
            ok = True
            user_instance.name = input.name
            user_instance.save()
            return Updateuser(ok=ok, user=user_instance)
        return Updateuser(ok=ok, user=None)


class Mutation(graphene.ObjectType):
    create_user = Createuser.Field()
    update_user = Updateuser.Field()
    send_text = SendText.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
