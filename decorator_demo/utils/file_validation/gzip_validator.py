"""
Gzip Validator
"""
import io
import gzip

from utils.file_validation.base import FileValidator


class GzipValidator(FileValidator):
    """
    need to implement validate
    """

    @staticmethod
    def validate(file_full_path: str) -> None:
        """
        this validate function is dedicated for python3.7
        """
        with gzip.open(file_full_path, "r") as fh:
            # fh.read would check the beginning
            fh.read(1)
            # seek_end would seek the end of course
            fh.seek(offset=0, whence=io.SEEK_END)
