from pydantic import BaseModel

class InputModel(BaseModel):
    message: str

class OutputModel(BaseModel):
    message: str
    

def ConvertModel(input: InputModel):
    #always check for None values
    if input is None: return None
    #example of conversion function
    return OutputModel(message=input.message.upper())