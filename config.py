import os


class Config:
    VERBOSE = bool(os.environ.get("VERBOSE_FLASK"))
