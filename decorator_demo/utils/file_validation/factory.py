from utils.file_validation.gzip_validator import GzipValidator


class FileValidatorFactory(object):
    @staticmethod
    def validate(filename_extension: str, file_full_path: str) -> None:
        if filename_extension == ".gz":
            GzipValidator().validate(file_full_path=file_full_path)
        else:
            print(f"Validator for {filename_extension} is not implemented yet!")
