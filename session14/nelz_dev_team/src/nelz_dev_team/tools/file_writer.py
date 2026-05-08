from crewai.tools import BaseTool
import os

class FileWriterTool(BaseTool):
    name: str = "file_writer"
    description: str = "Writes content to a file in the project"

    def _run(self, file_path: str, content: str) -> str:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

        return f"File written to {file_path}"