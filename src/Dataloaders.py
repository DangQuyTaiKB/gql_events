import uuid
from uoishelpers.dataloaders import createIdLoader, createFkeyLoader
from functools import cache

from src.DBDefinitions import BaseModel
# from src.DBDefinitions import (
#     BaseModel,
#     EventModel, 
#     EventTypeModel, 
#     EventGroupModel, 
    
#     PresenceModel, 
#     InvitationTypeModel, 
#     PresenceTypeModel
#     )
# async def createLoaders_3(asyncSessionMaker):


#     class Loaders:
#         @property
#         @cache
#         def events(self):
#             return createIdLoader(asyncSessionMaker, EventModel)

#         @property
#         @cache
#         def eventtypes(self):
#             return createIdLoader(asyncSessionMaker, EventTypeModel)

#         @property
#         @cache
#         def presences(self):
#             return createIdLoader(asyncSessionMaker, PresenceModel)

#         @property
#         @cache
#         def invitationtypes(self):
#             return createIdLoader(asyncSessionMaker, InvitationTypeModel)

#         @property
#         @cache
#         def presencetypes(self):
#             return createIdLoader(asyncSessionMaker, PresenceTypeModel)

#         @property
#         @cache
#         def eventgroups_group_id(self):
#             return createFkeyLoader(
#                 asyncSessionMaker, EventGroupModel, foreignKeyName="group_id"
#             )

#         @property
#         @cache
#         def eventgroups_event_id(self):
#             return createFkeyLoader(
#                 asyncSessionMaker, EventGroupModel, foreignKeyName="event_id"
#             )

#         @property
#         @cache
#         def eventgroups(self):
#             return createIdLoader(
#                 asyncSessionMaker, EventGroupModel
#             )

#         @property
#         @cache
#         def eventusers_user_id(self):
#             return createFkeyLoader(
#                 asyncSessionMaker, PresenceModel, foreignKeyName="user_id"
#             )

#         @property
#         @cache
#         def event_eventtype_id(self):
#             return createFkeyLoader(
#                 asyncSessionMaker, EventModel, foreignKeyName="eventtype_id"
#             )



#     return Loaders()


def createLoadersAuto(asyncSessionMaker, BaseModel, extra={}):
    def createLambda(loaderName, DBModel):
        return lambda self: createIdLoader(asyncSessionMaker, DBModel)

    attrs = {}
    
    for DBModel in BaseModel.registry.mappers:
        cls = DBModel.class_
        attrs[cls.__tableName__] = property(cache(createLambda(asyncSessionMaker, cls)))

    for key, value in extra.items():
        attrs[key] = property(cache(lambda self: value()))
    Loaders = type('Loaders', (), attrs)   
    return Loaders()

def createLoaders(asyncSessionMaker):

    def createLambda(loaderName, DBModel):
        return lambda self: createIdLoader(asyncSessionMaker, DBModel)

    attrs = {}

    for DBModel in BaseModel.registry.mappers:
        cls = DBModel.class_
        attrs[cls.__tablename__] = property(cache(createLambda(asyncSessionMaker, cls)))
        attrs[cls.__name__] = attrs[cls.__tablename__]
    
    # attrs["authorizations"] = property(cache(lambda self: AuthorizationLoader()))
    Loaders = type('Loaders', (), attrs)   
    return Loaders()


def createLoadersContext(asyncSessionMaker):
    return {
        "loaders": createLoaders(asyncSessionMaker)
    }

def getUserFromInfo(info):
    context = info.context
    #print(list(context.keys()))
    result = context.get("user", None)
    if result is None:
        request = context.get("request", None)
        assert request is not None, context
        result = request.scope["user"]

    if result is None:
        result = {"id": None}
    else:
        result = {**result, "id": uuid.UUID(result["id"])}
    # logging.debug("getUserFromInfo", result)
    return result

print(createLoaders(None))