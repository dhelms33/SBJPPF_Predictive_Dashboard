from abc import ABC, abstractmethod

class SocialMediaParser(ABC):
    """ Abstract Base Class enforcing the Open Closed Principle, filtering data out of the CSV"""
    
    @abstractmethod
    def load_data(self, file_path: str) -> None:
        pass
    
    @abstractmethod
    def extract_engagement_metics(self) -> dict:
        pass
    
    class PredicitveModel(ABC):
        """ Abstract Base Class for plug and play ML models (strategy pattern)"""
        @abstractmethod
        def train_data(self, features: list, labels: list) -> None:
            pass
        @abstractmethod
        def predict_data(self, input_data: list) -> float:
            pass