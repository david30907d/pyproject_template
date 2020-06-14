"""
A decorator to check file validation when invoking FsAccess upload function
"""
from pathlib import Path
from functools import wraps

from utils.file_validation.factory import FileValidatorFactory


def file_validation_decorators(func):
    @wraps(func)
    def wrapper(self, file_pull_path, *args, **kwargs):
        file_pull_path_obj = Path(file_pull_path)
        filename_extension = file_pull_path_obj.suffix
        # It would raise exception if it's invalid file
        FileValidatorFactory.validate(filename_extension, file_pull_path)
        return func(self, file_pull_path, *args, **kwargs)

    return wrapper
