import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import Users
from twitter_scraperV2 import get_tweets
from personality import get_activities

# Create a GraphQL type for the users model


class UserType(DjangoObjectType):
    class Meta:
        model = Users


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


class ShowActivities(graphene.Mutation):
    activities = graphene.String()

    class Arguments:
        activities = graphene.String()

    @staticmethod
    def mutate(root, info, activities):
        retString = ""
        try:
            print(activities)
            tweets = get_tweets(activities)
            activities = get_activities(tweets)
            for i in range(len(activities)):
                if i == 2:
                    retString += activities[i]+"."
                else:
                    retString += activities[i]+"|"
        except:
            activities = "Wow, I liked @TheRock before, now I really SEE how special he is. The daughter story was IT for me. So great! #MasterClass @TheRock how did you Know to listen to your gut and Not go back to football? #Masterclass @TheRock moving back in with your parents so humbling. \” on the other side of your pain is something good if you can hold on\” #masterclass Wow aren’t you loving @TheRock and his candor? #Masterclass RT @patt_t: @TheRock @Oprah @RichOnOWN @OWNTV this interview makes me like you as a fellow human even more for being so real. \“Be You\“.. That’s the best advice ever @TheRock #MastersClass Supersoulers let’s lift our spirits pray and hold Paris in the Light\ud83d\ude4f\ud83c\udffe RT @DeepakChopra: What I learned in week 1: Become What You Believe 21-Day Meditation Experience - https:\/\/t.co\/kqaMaMqEUp #GoogleAlerts Watching Bryan Stevenson on #SuperSoulSunday! \“You are not the worst mistake you ever made\“.\nAren’t we glad  about that. @CherylStrayed  BRAVE ENOUGH my new favorite thing! Gonna buy a copy for all my girls. #Perfectgift https:\/\/t.co\/gz1tnv8t8K Stevie Wonder singing \“Happy Birthday to you!\” to my dear  mariashriver. A phenomenal woman and\u2026 https:\/\/t.co\/Ygm5eDIs4f It\u2019s my faaaaavorite time of the Year!  For the first time you can shop the list on @amazon! https:\/\/t.co\/a6GMvVrhjN https:\/\/t.co\/sJlQMROq5U Incredible story \“the spirit of the Lord is on you\” thanks for sharing @smokey_robinson #Masterclass Wasnt that incredible story about @smokey_robinson ’s dad leaving his family at 12. #MasterClass Gayle, Charlie, Nora @CBSThisMorning  Congratulations!  #1000thshow I believe your home should rise up to meet you. @TheEllenShow you nailed it with HOME.  Tweethearts, grab a copy! https:\/\/t.co\/iFMnpRAsno"
            print(activities)
            tweets = get_tweets(activities)
            activities = get_activities(tweets)
            for i in range(len(activities)):
                if i == 2:
                    retString += activities[i]+"."
                else:
                    retString += activities[i]+"|"
        return ShowActivities(activities=retString)


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
    show_activities = ShowActivities.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
