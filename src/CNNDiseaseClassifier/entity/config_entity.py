from pathlib import Path
from dataclasses import dataclass

@dataclass(frozen=True)
class DataIngestionConfiguration:
   root_dir: Path
   source_URL: str
   local_data_file: Path
   unzip_dir: Path