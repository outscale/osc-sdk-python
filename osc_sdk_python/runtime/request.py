from dataclasses import dataclass, field
from urllib.parse import quote


@dataclass
class RequestSpec:
    service: str
    method: str
    path: str
    json_body: dict | list | None = None
    query_params: dict = field(default_factory=dict)

    def resolved_path(self, path_params: dict | None = None) -> str:
        path = self.path
        for name, value in (path_params or {}).items():
            path = path.replace("{" + name + "}", quote(str(value), safe=""))
        return path
