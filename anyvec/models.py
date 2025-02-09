from dataclasses import dataclass
from typing import Optional

@dataclass
class VectorizationPayload:
    text_content: Optional[str] = None
    file_content: Optional[bytes] = None
    file_url: Optional[str] = None
    file_name: Optional[str] = None

    def validate(self):
        """Ensures that at least one valid input is provided."""
        if not any([self.text_content, self.file_content, self.file_url]):
            raise ValueError("Provide at least one of text_content, file_content, or file_url.")

        if self.text_content and self.file_name:
            raise ValueError("file_name is not required when passing text_content and file_name.")
        
        if self.text_content and (self.file_content or self.file_url):
            raise ValueError("Provide either text_content or file_content/file_url, not both.")
        
        if self.file_content and self.file_url:
            raise ValueError("Provide either file_content or file_url, not both.")