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

def createLoaders(asyncSessionMaker):
    @cache
    def createModelDict():
        result = {}
        for DBModel in BaseModel.registry.mappers:
            table = DBModel.class_
            result[table.__tablename__] = table
        return result

    def createLambda(loaderName, DBModel):
        return lambda self: createIdLoader(asyncSessionMaker, DBModel)

    modelDict = createModelDict()    
    attrs = {}

    for tableName, DBModel in modelDict.items():
        attrs[tableName] = property(cache(createLambda(asyncSessionMaker, DBModel)))
        # print(tableName, DBModel)

    
    # attrs["authorizations"] = property(cache(lambda self: AuthorizationLoader()))
    Loaders = type('Loaders', (), attrs)   
    return Loaders()

def createLoadersContext(asyncSessionMaker):
    return {
        "loaders": createLoaders(asyncSessionMaker)
    }

print(createLoaders(None))