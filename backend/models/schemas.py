from pydantic import BaseModel, field_validator
from typing import List

class VESReading(BaseModel):
    ab: float
    mn: float
    voltage: float
    current: float

    @field_validator('ab')
    def ab_positive(cls, v):
        if v<=0:
            raise ValueError("Oops! AB/2 must me greater than 0")
        return v
    
    @field_validator('mn')
    def mn_positive(cls, v):
        if v<=0:
            raise ValueError("Oops! MN/2 must be greater than 0")
        return v
    
    @field_validator('voltage')
    def volt_not_negative(cls, v):
        if v<0:
            raise ValueError("Oops! Voltage must not be Negative")
        return v
    
    @field_validator('current')
    def current_not_zero(cls, v):
        if v==0:
            raise ValueError("Oops! Current must not be Zero")
        return v
    
    
class VESResult(BaseModel):
    ab: float
    mn: float
    voltage: float
    current: float
    k_factor: float
    app_resistivity: float
    

class VESManyResult(BaseModel):
    results: List[VESResult]
    curve_type: str