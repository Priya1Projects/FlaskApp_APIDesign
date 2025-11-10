from pydantic import BaseModel, ValidationError, validator
from typing import Optional

class SummarizeRequestModel(BaseModel):
    text: constr(min_length=1,max_length=5000)
    max_length: Optional[int] = 350

    @validator('text')
    def text_must_not_be_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('Text must not be empty')
        return v

    
    def validate(**data):
        try:
            model = SummarizeRequestModel(data)
            return model, None
        except ValidationError as e:
            return None, e.errors()