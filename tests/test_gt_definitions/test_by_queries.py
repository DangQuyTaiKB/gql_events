from .gt_utils import (
    createByIdTest2,
    createUpdateTest2,
    createTest2
)


test_event_by_id = createByIdTest2(tableName="events")
test_event_page = createTest2(tableName="events", queryName="readp")
test_event_insert = createTest2(
    tableName="events", 
    queryName="create", 
    variables={
        "id": "aae16f75-e76e-43a7-b0bc-556f0f6dd29d",
        "name": "new event",
        "type_id": "c0a12392-ae0e-11ed-9bd8-0242ac110002"
    })
test_event_coverage = createTest2(
    tableName="events", 
    queryName="coverage")

test_event_update = createUpdateTest2(
    tableName="events", 
    variables={
        "id": "9b642606-1551-4945-bc7d-ebb53cf513a7",
        "name": "new event renamed"
    })
test_event_delete = createTest2(
    tableName="events",
    queryName="delete",
    variables={
        "id": "9b642606-1551-4945-bc7d-ebb53cf513a7"
    }
)

test_event_type_by_id = createByIdTest2(tableName="eventtypes")
test_event_type_page = createTest2(tableName="eventtypes", queryName="readp")
test_event_type_insert = createTest2(
    tableName="eventtypes", 
    queryName="create",
    variables={
        "id": "cdaf3926-1962-437c-8cb9-2167aa9e5a7d",
        "name": "new event type",
        "name_en": "new event type"
    }
)
test_event_type_update = createUpdateTest2(
    tableName="eventtypes",
    variables={
        "id": "69ec2b0b-a39d-40df-9cea-e295b36749c9",
        "name": "renamed"
    }
)
test_event_type_delete = createTest2(
    tableName="eventtypes",
    queryName="delete",
    variables={
        "id": "69ec2b0b-a39d-40df-9cea-e295b36749c9"
    }
)


test_presence_by_id = createByIdTest2(tableName="events_users")
test_presence_page = createTest2(tableName="events_users", queryName="readp")
test_presence_insert = createTest2(
    tableName="events_users", 
    queryName="create",
    variables={
        "id": "181bf3b7-8a6d-4338-983c-14b1062d536a",
        "user_id": "89d1f638-ae0f-11ed-9bd8-0242ac110002",
        "event_id": "0945ad17-3a36-4d33-b849-ad88144415ba", 
        "invitationtype_id": "e871403c-a79c-11ed-b76e-0242ac110002", 
        "presencetype_id": "466398c6-a79c-11ed-b76e-0242ac110002"
    }
    )
# test_presence_update = createUpdateTest2(
#     tableName="events_users",
#     # queryName="update",
#     variables={
#         "id": "89d1f624-ae0f-11ed-9bd8-0242ac110002", 
#         # "user_id": "89d1f638-ae0f-11ed-9bd8-0242ac110002", 
#         # "event_id": "45b2df80-ae0f-11ed-9bd8-0242ac110002", 
#         "invitationtype_id": "e871403c-a79c-11ed-b76e-0242ac110002", 
#         "presencetype_id": "4663984e-a79c-11ed-b76e-0242ac110002"
#     }
#     )

test_presence_insert2 = createTest2(
    tableName="presences", 
    queryName="create",
    variables={
        "id": "181bf3b7-8a6d-4338-983c-14b1062d536a",
        "user_id": "89d1f638-ae0f-11ed-9bd8-0242ac110002",
        "event_id": "0945ad17-3a36-4d33-b849-ad88144415ba", 
        "invitationtype_id": "e871403c-a79c-11ed-b76e-0242ac110002", 
        "presencetype_id": "466398c6-a79c-11ed-b76e-0242ac110002"
    }

)
test_presence_update2 = createUpdateTest2(
    tableName="presences",
    # queryName="update",
    variables={
        "id": "89d1f624-ae0f-11ed-9bd8-0242ac110002", 
        "user_id": "89d1f638-ae0f-11ed-9bd8-0242ac110002", 
        "event_id": "45b2df80-ae0f-11ed-9bd8-0242ac110002", 
        "invitationtype_id": "e871403c-a79c-11ed-b76e-0242ac110002", 
        "presencetype_id": "4663984e-a79c-11ed-b76e-0242ac110002"
    }
    )
test_presence_delete = createTest2(
    tableName="presences",
    queryName="delete",
    variables={
        "id": "89d1e684-ae0f-11ed-9bd8-0242ac110002"
    }
)


test_event_presence_type_by_id = createByIdTest2(tableName="eventpresencetypes")
test_event_presence_type_page = createTest2(tableName="eventpresencetypes", queryName="readp")
test_event_presence_type_insert = createTest2(
    tableName="eventpresencetypes",
    queryName="create",
    variables={
        "id": "094e70ad-9008-463b-8a01-04dd05a0e48c",
        "name": "new type",
        "name_en": "new type"
    }
)
test_event_presence_type_update = createUpdateTest2(
    tableName="eventpresencetypes",
    variables={
        "id": "466397d6-a79c-11ed-b76e-0242ac110002",
        "name": "updated type name"
    }
)
test_event_presence_type_delete = createTest2(
    tableName="eventpresencetypes",
    queryName="delete",
    variables={
        "id": "094e70ad-9008-463b-8a01-04dd05a0e48c",        
    }
)

test_event_invitation_type_by_id = createByIdTest2(tableName="eventinvitationtypes")
test_event_invitation_type_page = createTest2(tableName="eventinvitationtypes", queryName="readp")
test_event_invitation_type_insert = createTest2(
    tableName="eventinvitationtypes", 
    queryName="create",
    variables={
        "id": "032ce568-1a73-410d-b1d7-c852aa6c1741",
        "name": "new invitation type",
        "name_en": "new invitation type"
    }
)
test_event_invitation_type_update = createUpdateTest2(
    tableName="eventinvitationtypes",
    variables={
        "id": "e8714104-a79c-11ed-b76e-0242ac110002",
        "name": "renamed invitation type",
        "name_en": "renamed invitation type"
    }
)
test_event_invitation_type_delete = createTest2(
    tableName="eventinvitationtypes", 
    queryName="delete",
    variables={
        "id": "e8714104-a79c-11ed-b76e-0242ac110002"
    }
)

test_event_group_insert = createTest2(
    tableName="events_groups",
    queryName="create",
    variables={
        "group_id": "9baf3b54-ae0f-11ed-9bd8-0242ac110002",
        "event_id": "a64871f8-2308-48ff-adb2-33fb0b0741f1"
    }    
)
test_event_group_delete = createTest2(
    tableName="events_groups",
    queryName="delete",
    variables={
        "group_id": "9baf3b54-ae0f-11ed-9bd8-0242ac110002", 
        "event_id": "45b2df80-ae0f-11ed-9bd8-0242ac110002"
    }
)

test_event_user_insert = createTest2(
    tableName="events_users",
    queryName="create",
    variables={
        "user_id": "89d1e724-ae0f-11ed-9bd8-0242ac110002", 
        "event_id": "a64871f8-2308-48ff-adb2-33fb0b0741f1",
        "invitationtype_id": "e871403c-a79c-11ed-b76e-0242ac110002"
    }    
)
test_event_user_update = createUpdateTest2(
    tableName="events_users",
    variables={
        "id": "89d1e684-ae0f-11ed-9bd8-0242ac110002",
        "invitationtype_id": "e8714104-a79c-11ed-b76e-0242ac110002"
    }    
)
test_event_user_delete = createTest2(
    tableName="events_users",
    queryName="delete",
    variables={
        "user_id": "89d1e724-ae0f-11ed-9bd8-0242ac110002", 
        "event_id": "45b2df80-ae0f-11ed-9bd8-0242ac110002"
    }
)


test_user_ = createTest2(tableName="users", queryName="resolve_reference.event", variables={"id": "89d1e724-ae0f-11ed-9bd8-0242ac110002"})
test_group_ = createTest2(tableName="groups", queryName="resolve_reference.event", variables={"id": "9baf3b54-ae0f-11ed-9bd8-0242ac110002"})