from app.db import org, database
from app.api.models import OrgSchema

async def post(payload: OrgSchema):
    query = org.insert().values(name=payload.name, 
                                 description=payload.description, 
                                 street=payload.street, 
                                 city=payload.city, 
                                 state=payload.state, 
                                 zip=payload.zip)
    return await database.execute(query=query)


