from ctypes import cast
from pathlib import Path
from typing import cast

from nbconvert import NotebookExporter
from nbconvert.preprocessors import (ClearMetadataPreprocessor,
                                     ClearOutputPreprocessor)

"""Clear the metadata from all notebooks in the same directory as the script."""
def main()-> None:
    exporter = NotebookExporter()
    exporter.register_preprocessor(ClearOutputPreprocessor(), enabled=True)
    exporter.register_preprocessor(ClearMetadataPreprocessor(), enabled=True)
    own_path = Path(__file__)

    for path in own_path.parent.glob('*.ipynb'):
        print(f"Start processing {path}")
        clean_notebook, _ = exporter.from_filename(cast(str, path))

        with open(path, "w", encoding="utf-8") as f:
            f.write(cast(str, clean_notebook))

if __name__ == "__main__":
    main()
