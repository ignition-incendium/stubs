from typing import Dict, Optional, Tuple, Union

from incendium.helper.types import AnyStr, Number
from incendium.user import IncendiumUser
from java.util import Date

def get_function_name() -> AnyStr: ...
def get_timer(date: Union[Date, long]) -> AnyStr: ...
def get_timestamp(value: int) -> AnyStr: ...
def set_locale(user: IncendiumUser) -> None: ...
def validate_form(
    strings: Optional[Dict[AnyStr, AnyStr]] = ...,
    numbers: Optional[Dict[AnyStr, Number]] = ...,
    collections: Optional[Dict[AnyStr, Number]] = ...,
) -> Tuple[bool, AnyStr]: ...
