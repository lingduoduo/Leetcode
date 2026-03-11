"""You'll implement this."""

from typing import List, Optional
import heapq

from network import Network


class Route:
    def __init__(self, stations: List[str], total_time: int, transfers: int):
        self.stations = stations
        self.total_time = total_time
        self.transfers = transfers


class Planner:
    """Finds optimal routes through a transit network."""

    def __init__(self, network: Network):
        self.network = network

    def find_route(self, start: str, end: str) -> Optional[Route]:
        if not self.network.has_station(start) or not self.network.has_station(end):
            return None
        
        if start == end:
            return Route([start], 0, 0)
        
        # Priority queue: (total_cost, current_station, current_line, path, transfers)
        pq = [(0, start, None, [start], 0)]
        # Track best cost to reach each (station, line) pair
        visited = {}
        
        while pq:
            current_cost, current_station, current_line, path, transfers = heapq.heappop(pq)
            
            # Skip if we've already found a better path to this (station, line) combination
            state_key = (current_station, current_line)
            if state_key in visited and visited[state_key] <= current_cost:
                continue
            visited[state_key] = current_cost
            
            # Check if we've reached the destination
            if current_station == end:
                return Route(path, current_cost, transfers)
            
            # Explore neighbors
            for connection in self.network.get_neighbors(current_station):
                next_station = connection.destination
                
                # Skip if we've already visited this station in this path (avoid cycles)
                if next_station in path:
                    continue
                
                # Calculate cost including potential transfer penalty
                travel_cost = self.network.get_travel_cost(connection, current_line)
                new_cost = current_cost + travel_cost
                new_transfers = transfers
                
                # Count transfer if switching lines
                if current_line is not None and current_line != connection.line:
                    new_transfers += 1
                
                new_path = path + [next_station]
                
                # Add to priority queue
                heapq.heappush(pq, (new_cost, next_station, connection.line, new_path, new_transfers))
        
        return None

    def find_route_with_max_transfers(
        self, start: str, end: str, max_transfers: int
    ) -> Optional[Route]:
        if not self.network.has_station(start) or not self.network.has_station(end):
            return None
        
        if start == end:
            return Route([start], 0, 0)
        
        # Priority queue: (total_cost, current_station, current_line, path, transfers)
        pq = [(0, start, None, [start], 0)]
        # Track best cost to reach each (station, line) pair
        visited = {}
        
        while pq:
            current_cost, current_station, current_line, path, transfers = heapq.heappop(pq)
            
            # Skip if we've exceeded the transfer limit
            if transfers > max_transfers:
                continue
            
            # Skip if we've already found a better path to this (station, line) combination
            state_key = (current_station, current_line)
            if state_key in visited and visited[state_key] <= current_cost:
                continue
            visited[state_key] = current_cost
            
            # Check if we've reached the destination
            if current_station == end:
                return Route(path, current_cost, transfers)
            
            # Explore neighbors
            for connection in self.network.get_neighbors(current_station):
                next_station = connection.destination
                
                # Skip if we've already visited this station in this path (avoid cycles)
                if next_station in path:
                    continue
                
                # Calculate cost including potential transfer penalty
                travel_cost = self.network.get_travel_cost(connection, current_line)
                new_cost = current_cost + travel_cost
                new_transfers = transfers
                
                # Count transfer if switching lines
                if current_line is not None and current_line != connection.line:
                    new_transfers += 1
                
                # Skip if this would exceed the transfer limit
                if new_transfers > max_transfers:
                    continue
                
                new_path = path + [next_station]
                
                # Add to priority queue
                heapq.heappush(pq, (new_cost, next_station, connection.line, new_path, new_transfers))
        
        return None