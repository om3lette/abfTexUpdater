from pathlib import Path
from enum import IntEnum
import sys
import os

TMP_FOLDER_NAME: str = "rpm_package_upgrade_tmp"

WORK_DIR_PATH: Path = (
    Path.joinpath(Path(os.path.dirname(sys.executable)), TMP_FOLDER_NAME))\
    if getattr(sys, 'frozen', False)\
    else Path.joinpath(Path(__file__).resolve().parents[1], TMP_FOLDER_NAME
)

FILES_CACHE_PATH: Path = Path.joinpath(WORK_DIR_PATH, 'mirror_cache.json')

SPEC_FILE_SUFFIXES: list[str] = ["spec"]
HASH_FILE_SUFFIXES: list[str] = ["yml", "yaml"]
ARCHITECTURES_SPECIFIC_PREFIXES: list[str] = ["armhf", "aarch64", "i386", "universal-darwin", "win", "amd64", "freebsd", "x86_64"]
TARBALL_SUFFIX: str = "tar.xz"

MIRROR_BASE_URL: str = "https://mirror.truenetwork.ru/CTAN/systems/texlive/tlnet/archive/"
ABF_UPLOAD_URI: str = "http://file-store.rosalinux.ru/api/v1/upload"

DECLINE_VALUES: list[str] = ['n', 'no']
ACCEPT_VALUES: list[str] = ['y', 'yes']
BOOLEAN_INPUT_ANSWERS: list[str] = ACCEPT_VALUES + DECLINE_VALUES


class ExitStatus(IntEnum):
    ERROR = 1
    EARLY_RETURN = 2


class PackageTypes(IntEnum):
    MAIN = 1
    SOURCE = 2
    DOC = 3
