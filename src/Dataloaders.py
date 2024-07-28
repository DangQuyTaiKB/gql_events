from uoishelpers.dataloaders import createLoadersAuto
from src.DBDefinitions import BaseModel

def createLoadersContext(asyncSessionMaker):
    return {
        # "loaders": createLoaders(asyncSessionMaker)
        "loaders": createLoadersAuto(asyncSessionMaker, BaseModel=BaseModel)
    }