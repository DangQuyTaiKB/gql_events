# from typing import Coroutine, Callable, Awaitable, Union, List
import uuid
import datetime
import typing
import strawberry
from sqlalchemy import select
# from sqlalchemy.orm import selectinload, joinedload
# from sqlalchemy.ext.asyncio import AsyncSession

# from uoishelpers.resolvers import (
#     create1NGetter,
#     createEntityByIdGetter,
#     createEntityGetter,
#     createInsertResolver,
#     createUpdateResolver,
# )
# from uoishelpers.resolvers import putSingleEntityToDb

from src.DBDefinitions import BaseModel
from .GraphPermissions import OnlyForAuthentized
IDType = uuid.UUID

## Nasleduji funkce, ktere lze pouzit jako asynchronni resolvery


@classmethod
async def resolve_reference(cls, info: strawberry.types.Info, id: IDType):
    if id is None: return None
    if isinstance(id, str): id = IDType(id)
    loader = cls.getLoader(info)
    result = await loader.load(id)
    if result is not None:
        # result._type_definition = cls._type_definition  # little hack :)
        result.__strawberry_definition__ = cls.__strawberry_definition__  # little hack :)
    return result

@strawberry.field(
    description="""Entity primary key""",
    permission_classes=[
        OnlyForAuthentized
    ]
    )
def resolve_id(self) -> IDType:
    return self.id

@strawberry.field(
    description="""Name """,
    permission_classes=[
        OnlyForAuthentized
    ]
    )
def resolve_name(self) -> str:
    return self.name

@strawberry.field(
    description="""English name""",
    permission_classes=[
        OnlyForAuthentized
    ]
    )
def resolve_name_en(self) -> str:
    result = self.name_en if self.name_en else ""
    return result

@strawberry.field(
    description="""Time of last update""",
    permission_classes=[
        OnlyForAuthentized
    ]
    )
def resolve_lastchange(self) -> datetime.datetime:
    return self.lastchange

@strawberry.field(
    description="""Time of entity introduction""",
    permission_classes=[
        OnlyForAuthentized
    ]
    )
def resolve_created(self) -> typing.Optional[datetime.datetime]:
    return self.created

UserGQLModel = typing.Annotated["UserGQLModel", strawberry.lazy(".GraphTypeDefinitionsExt")]

async def resolve_user(user_id):
    from .GraphTypeDefinitionsExt import UserGQLModel
    result = None if user_id is None else await UserGQLModel.resolve_reference(id=user_id, info=None)
    return result
    
@strawberry.field(description="""Who created entity""",
    permission_classes=[
        OnlyForAuthentized
    ])
async def resolve_createdby(self) -> typing.Optional["UserGQLModel"]:
    return await resolve_user(self.createdby)

@strawberry.field(description="""Who made last change""",
    permission_classes=[
        OnlyForAuthentized
    ])
async def resolve_changedby(self) -> typing.Optional["UserGQLModel"]:
    return await resolve_user(self.changedby)


###########################################################################################################################
#
# zde si naimportujte sve SQLAlchemy modely
#
###########################################################################################################################

from src.DBDefinitions import (
    EventModel,
    EventGroupModel,
    EventTypeModel,
    PresenceModel,
    PresenceTypeModel,
    InvitationTypeModel
)


###########################################################################################################################
#
# zde definujte sve resolvery s pomoci funkci vyse
# tyto pouzijete v GraphTypeDefinitions
#
###########################################################################################################################

# resolveEventTypeById = createEntityByIdGetter(EventTypeModel)
# resolveEventTypePage = createEntityGetter(EventTypeModel)


# resolveEventById = createEntityByIdGetter(EventModel)
# resolveEventPage = createEntityGetter(EventModel)
# resolveGroupsForEvent = create1NGetter(EventGroupModel, foreignKeyName="event_id")

# resolveEventsForGroup_ = create1NGetter(
#     EventGroupModel,
#     foreignKeyName="group_id",
#     options=joinedload(EventGroupModel.event),
# )

# from sqlalchemy.future import select
from sqlalchemy import select


# async def resolveEventsForGroup(session, id, startdate=None, enddate=None):
#     statement = select(EventModel).join(EventGroupModel)
#     if startdate is not None:
#         statement = statement.filter(EventModel.startdate >= startdate)
#     if enddate is not None:
#         statement = statement.filter(EventModel.enddate <= enddate)
#     statement = statement.filter(EventGroupModel.group_id == id)

#     response = await session.execute(statement)
#     result = response.scalars()
#     return result


# async def resolveEventsForUser(session, id, startdate=None, enddate=None):
#     statement = select(EventModel).join(PresenceModel)
#     if startdate is not None:
#         statement = statement.filter(EventModel.startdate >= startdate)
#     if enddate is not None:
#         statement = statement.filter(EventModel.enddate <= enddate)
#     statement = statement.filter(PresenceModel.user_id == id)

#     response = await session.execute(statement)
#     result = response.scalars()
#     return result

# async def resolvePresencesForEvent(session, id, invitationtypelist=[]):
#     statement = select(PresenceModel)
#     if len(invitationtypelist) > 0:
#         statement = statement.filter(PresenceModel.invitation_id.in_(invitationtypelist))
#     response = await session.execute(statement)
#     result = response.scalars()
#     return result

# resolvePresenceTypeById = createEntityByIdGetter(PresenceTypeModel)
# resolveInvitationTypeById = createEntityByIdGetter(InvitationTypeModel)

from uoishelpers.dataloaders import prepareSelect
def create_statement_for_user_events2(id, where: dict= None):
    statement = select(EventModel) if where is None else prepareSelect(EventModel, where)
    statement = statement.join(PresenceModel)
    statement = statement.filter(PresenceModel.user_id == id)
    return statement

def create_statement_for_event_presences(id, where: dict= None):
    statement = select(PresenceModel) if where is None else prepareSelect(PresenceModel, where)
    statement = statement.join(EventModel)
    statement = statement.filter(EventModel.id == id)
    return statement

def create_statement_for_group_events2(id, where: dict= None):
    statement = select(EventModel) if where is None else prepareSelect(EventModel, where)
    statement = statement.join(EventGroupModel)
    statement = statement.filter(EventGroupModel.group_id == id)
    return statement