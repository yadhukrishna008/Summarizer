from pydantic import BaseModel


class SummarizeRequest(BaseModel):
    text:str

class SummarizeResponse(BaseModel):
    text:str


prompt_template= """Summarize the following text in one concise paragraph. 
    Do not include any extra details or commentary. Only return the summary.

    Text:
    {TEXT}
    Summary:
    """
