class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        length = len(position)
        cars = []
        for i in range(length):
            cars.append((position[i],speed[i]))
        cars.sort(reverse=True)
        fleet_times = []
        for car in cars:
            time = (target-car[0])/car[1]
            if len(fleet_times) >= 1:
                if time <= fleet_times[-1]:
                    continue
            fleet_times.append(time)
        return len(fleet_times)
            