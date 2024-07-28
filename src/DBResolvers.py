from uoishelpers.resolvers import DBResolver
from src.DBDefinitions import (
    EventModel,
    EventTypeModel,
    EventCategoryModel,
    EventGroupModel,
    PresenceModel,
    PresenceTypeModel,
    InvitationTypeModel
)
EventModelResolvers = DBResolver(EventModel)
EventTypeModelResolvers = DBResolver(EventTypeModel)
EventCategoryModelResolvers = DBResolver(EventCategoryModel)
EventGroupModelResolvers = DBResolver(EventGroupModel)
PresenceModelResolvers = DBResolver(PresenceModel)
PresenceTypeModelResolvers = DBResolver(PresenceTypeModel)
InvitationTypeModelResolvers = DBResolver(InvitationTypeModel)

