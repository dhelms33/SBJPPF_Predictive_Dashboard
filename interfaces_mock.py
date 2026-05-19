from abc import ABC, abstractmethod

class SocialMediaParser(ABC):
    """ Abstract Base Class enforcing the Open Closed Principle, gathering Social Media data to be fed into model"""
    
    @abstractmethod
    def load_data(self, file_path: str) -> None:
        pass