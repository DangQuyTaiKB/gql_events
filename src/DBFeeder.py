import os

from functools import cache
from uoishelpers.feeders import ImportModels
from uoishelpers.dataloaders import readJsonFile

from src.DBDefinitions import (
    EventModel, 
    EventTypeModel, 
    EventGroupModel, 
    PresenceModel, 
    PresenceTypeModel, 
    InvitationTypeModel
    )

get_demodata = lambda :readJsonFile(jsonFileName="./systemdata.json")
async def initDB(asyncSessionMaker):

    isDemo = os.environ.get("DEMODATA", None)
    if isDemo:
        print("Demo mode", flush=True)
        dbModels = [
            EventTypeModel, 
            PresenceTypeModel, 
            InvitationTypeModel,
            EventModel, 
            EventGroupModel, 
            PresenceModel, 
        ]
    else:

        print("No Demo mode", flush=True)
        dbModels = [
            EventTypeModel,           
            PresenceTypeModel, 
            InvitationTypeModel        
        ]

    jsonData = get_demodata()
    await ImportModels(asyncSessionMaker, dbModels, jsonData)
    
    print("Data initialized", flush=True)