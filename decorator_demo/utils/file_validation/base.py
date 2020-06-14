from abc import ABCMeta, abstractstaticmethod


class FileValidator(metaclass=ABCMeta):
    @staticmethod
    @abstractstaticmethod
    def validate(file_full_path: str) -> None:
        pass
