from six import text_type
from typing import Any, Dict, List, Optional, Text, Tuple, Union

class Suite:
    attributes: Union[List[Text], Dict[Text, Any]] = ...
    doc: Text = ...
    end_time: Text = ...
    longname: Text = ...
    message: Text = ...
    metadata: Dict[Text, Text] = ...
    name: Text = ...
    robot_id: Text = ...
    rp_item_id: Optional[Text] = ...
    rp_parent_item_id: Optional[Text] = ...
    source: Text = ...
    start_time: Optional[Text] = ...
    statistics: Text = ...
    status: Text = ...
    suites: List[Text] = ...
    tests: List[Text] = ...
    total_tests: int = ...
    type: Text = 'SUITE'
    def __init__(self, name: Text, attributes: Dict[Text, Any]) -> None: ...
    def update(self, attributes: Dict[Text, Any]) -> Union[Launch, Suite]: ...

class Launch(Suite):
    type: Text = 'LAUNCH'
    def __init__(self, name: Text, attributes: Dict[Text, Any]) -> None: ...

class Test:
    attributes: Dict[Text, Any] = ...
    critical: Text = ...
    doc: Text = ...
    end_time: Text = ...
    longname: Text = ...
    message: Text = ...
    name: Text = ...
    robot_id: Text = ...
    rp_item_id: Optional[Text] = ...
    rp_parent_item_id: Optional[Text] = ...
    start_time: Text = ...
    status: Text = ...
    tags: List[Text] = ...
    template: Text = ...
    type: Text = 'TEST'
    def __init__(self, name: Text, attributes: Dict[Text, Any]) -> None: ...
    def update(self, attributes: Dict[Text, Any]) -> Test: ...

class Keyword:
    attributes: Dict[Text, Any] = ...
    args: List[Text] = ...
    assign: List[Text] = ...
    doc: Text = ...
    end_time: Text = ...
    keyword_name: Text = ...
    keyword_type: Text = ...
    libname: Text = ...
    name: Text = ...
    rp_item_id: Optional[Text] = ...
    rp_parent_item_id: Optional[Text] = ...
    parent_type: Text = ...
    start_time: Text = ...
    status: Text = ...
    tags: List[Text] = ...
    type: Text = 'KEYWORD'
    def __init__(self, name: Text, attributes: Dict[Text, Any], parent_type: Optional[Text] = None) -> None: ...
    def get_name(self) -> Text: ...
    def get_type(self) -> Text: ...
    def update(self, attributes: Dict[Text, Any]) -> Keyword: ...

class LogMessage(text_type):
    attachment: Optional[Dict[Text, Text]] = ...
    item_id: Optional[Text] = ...
    level: Text = ...
    message: Text = ...
    def __init__(self, *args: Tuple, **kwargs: Dict) -> None: ...