"""Read this first."""

from typing import Dict, List, NamedTuple, Optional, Set

TRANSFER_PENALTY: int = 5


class Connection(NamedTuple):
    destination: str
    travel_time: int
    line: str
    one_way: bool


class Network:
    def __init__(self) -> None:
        self._stations: Dict[str, List[Connection]] = {}

    def add_station(self, name: str) -> None:
        if name not in self._stations:
            self._stations[name] = []

    def add_connection(
        self, from_station: str, to_station: str,
        travel_time: int, line: str, one_way: bool = False
    ) -> None:
        self.add_station(from_station)
        self.add_station(to_station)

        self._stations[from_station].append(
            Connection(to_station, travel_time, line, one_way)
        )
        
        # Only add reverse connection if it's not one-way
        if not one_way:
            self._stations[to_station].append(
                Connection(from_station, travel_time, line, one_way)
            )

    def get_travel_cost(
        self, connection: Connection, current_line: Optional[str]
    ) -> int:
        base_cost = connection.travel_time
        # Only add transfer penalty if switching from one line to a different line
        if current_line is not None and current_line != connection.line:
            base_cost += TRANSFER_PENALTY
        return base_cost

    def get_neighbors(self, station: str) -> List[Connection]:
        return self._stations.get(station, [])

    def get_all_stations(self) -> Set[str]:
        return set(self._stations.keys())

    def has_station(self, name: str) -> bool:
        return name in self._stations