from pydantic import BaseModel


class SummarizeRequest(BaseModel):
    text:str

class SummarizeResponse(BaseModel):
    summaries:str


prompt_template= """Summarize the following text in 1–2 sentences.
    Do not repeat phrases from the original text.
    Return only the summary.
    
    Text:
    {TEXT}
    Summary:
    """
