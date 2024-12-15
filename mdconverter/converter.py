import os
from markitdown import MarkItDown
from typing import Optional, Dict, Any, List

class FileConverter:
    def __init__(self, mlm_config: Optional[Dict[str, Any]] = None, 
                 input_folder: str = "input", 
                 output_folder: str = "output"):
        if mlm_config:
            self.md = MarkItDown(
                mlm_client=mlm_config.get('client'),
                mlm_model=mlm_config.get('model')
            )
        else:
            self.md = MarkItDown()
        
        self.input_folder = input_folder
        self.output_folder = output_folder
        os.makedirs(self.output_folder, exist_ok=True)

    def convert_file(self, file_path: str) -> str:
        """Convert a file to markdown format."""
        try:
            result = self.md.convert(file_path)
            return result.text_content
        except Exception as e:
            raise RuntimeError(f"Error converting file: {str(e)}")

    def convert_folder(self) -> List[str]:
        """Convert all compatible files in input folder to markdown format."""
        converted_files = []
        
        if not os.path.exists(self.input_folder):
            raise RuntimeError(f"Input folder '{self.input_folder}' does not exist")

        for filename in os.listdir(self.input_folder):
            input_path = os.path.join(self.input_folder, filename)
            if os.path.isfile(input_path):
                try:
                    content = self.convert_file(input_path)
                    output_filename = os.path.splitext(filename)[0] + '.md'
                    output_path = os.path.join(self.output_folder, output_filename)
                    
                    with open(output_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    converted_files.append(output_path)
                except Exception as e:
                    print(f"Failed to convert {filename}: {str(e)}")
                    
        return converted_files
