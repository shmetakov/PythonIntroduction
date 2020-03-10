import time


class TrafficLight:
    __color = None
    __color_dict = {"Red": 31,
                    "Green": 32,
                    "Yellow": 33}

    def __print_color(self, s_sleep):
        print(f"\r\x1b[1;{self.__color_dict[self.__color]}m{self.__color}\x1b[0m", end='')
        time.sleep(s_sleep)

    def running(self):
        self.__color = "Red"
        self.__print_color(7)
        self.__color = "Yellow"
        self.__print_color(2)
        self.__color = "Green"
        self.__print_color(5)
        self.__color = "Red"
        self.__print_color(1)


traffic_light = TrafficLight()
traffic_light.running()
