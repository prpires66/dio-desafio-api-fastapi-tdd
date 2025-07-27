from datetime import datetime
import uuid
from typing import Annotated
from pydantic import UUID4, BaseModel, Field


class BaseSchemaMixin(BaseModel):
    id: Annotated[UUID4, Field(default_factory=uuid.uuid4)]
    create_at: Annotated[datetime, Field(default_factory=datetime.utcnow)]
    update_at: Annotated[datetime, Field(default_factory=datetime.utcnow)]
