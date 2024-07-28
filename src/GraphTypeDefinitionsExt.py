import strawberry
import dataclasses
import datetime

from typing import List, Optional, Annotated
from .GraphResolvers import IDType
from uoishelpers.resolvers import createInputs, getLoadersFromInfo

@classmethod
async def resolve_reference(cls, info: strawberry.types.Info, id: IDType):
    return None if id is None else cls(id=id) 

from .GraphTypeDefinitions import EventGQLModel, PresenceGQLModel
from .GraphResolvers import (
    
    create_statement_for_user_events2, 
    create_statement_for_group_events2
    )

@createInputs
@dataclasses.dataclass
class UGEventInputFilter:
    name: str
    name_en: str

    valid: bool
    created: datetime.datetime
    createdby: IDType
    changedby: IDType
    startdate: datetime.datetime
    enddate: datetime.datetime
    masterevent_id: IDType
    eventtype_id: IDType

    # from .GraphTypeDefinitions import EventTypeWhereFilter
    # eventtype: EventTypeWhereFilter

PresenceInputFilter = Annotated["PresenceInputFilter", strawberry.lazy(".GraphTypeDefinitions")]

@strawberry.federation.type(extend=True, keys=["id"])
class UserGQLModel:
    id: IDType = strawberry.federation.field(external=True)
    resolve_reference = resolve_reference

    from .GraphTypeDefinitions import PresenceInputFilter

    @strawberry.field(description="""events of the user""")
    async def events(
        self,
        info: strawberry.types.Info,
        skip: Optional[int] = 0,
        limit: Optional[int] = 10,
        where: Optional[UGEventInputFilter] = None
    ) -> List["EventGQLModel"]:
        wheredict = None if where is None else strawberry.asdict(where)
        statement = create_statement_for_user_events2(self.id, where=wheredict)
        statement = statement.offset(skip).limit(limit)
        loader = getLoadersFromInfo(info).events
        result = await loader.execute_select(statement)
        return result
    
    @strawberry.field(description="""presences of the user""")
    async def presences(
        self,
        info: strawberry.types.Info,
        skip: Optional[int] = 0,
        limit: Optional[int] = 10,
        where: Optional[PresenceInputFilter] = None
    ) -> List["PresenceGQLModel"]:
        from .GraphTypeDefinitions import PresenceGQLModel
        loader = PresenceGQLModel.getLoader(info)

        wheredict = None if where is None else strawberry.asdict(where)
        rows = await loader.page(skip=skip, limit=limit, where=wheredict, extendedfilter={"user_id": self.id})
        return rows


@strawberry.federation.type(extend=True, keys=["id"])
class GroupGQLModel:
    id: IDType = strawberry.federation.field(external=True)
    resolve_reference = resolve_reference

    @strawberry.field(description="""events of the group""")
    async def events(
        self,
        info: strawberry.types.Info,
        skip: Optional[int] = 0,
        limit: Optional[int] = 10,
        where: Optional[UGEventInputFilter] = None
    ) -> List["EventGQLModel"]:
        wheredict = None if where is None else strawberry.asdict(where)
        statement = create_statement_for_group_events2(self.id, where=wheredict)
        statement = statement.offset(skip).limit(limit)
        loader = getLoadersFromInfo(info).events
        result = await loader.execute_select(statement)
        return result

from uoishelpers.gqlpermissions import RBACObjectGQLModel
