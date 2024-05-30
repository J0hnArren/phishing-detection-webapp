from typing import Any, List, Optional

from pydantic import BaseModel
from phishing_detection_model.processing.validation import PhishingDetectionInputSchema


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    preds: Optional[List[str]]
    probs: Optional[List[float]]


class MultiplePhishingDetectionInputs(BaseModel):
    inputs: List[PhishingDetectionInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        "URL": "https://github.com/J0hnArren/phishing-detection-webapp"
                    }
                ]
            }
        }
