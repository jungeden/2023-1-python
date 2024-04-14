#ex9_12
'''
TV 클래스 구현하기
'''
class TV:
    MIN_VOLUME = 0
    MAX_VOLUME = 20
    MIN_CHANNEL = 0
    MAX_CHANNEL = 200
    def __init__(self):
        self.__volume = 5
        self.__channel = 0
        self.__is_on = False
       
    def __str__(self):
        if self.__is_on:
            return f'볼륨 : {self.__volume}, 채널 : {self.__channel}'
        else:
            return f'TV가 꺼짐 상태입니다.'
    def toggle_power(self):
        self.__is_on = not self.__is_on
    def get_channel(self):
        return self.__channel
    def set_channel(self,channel):
        if self.MIN_CHANNEL <= channel <= self.MAX_CHANNEL:
            self.__channel = channel
        else:
            print('채널 오류')
    def get_volume(self):
        return self.__volume   
    def set_volume(self,volume):
        if self.MIN_VOLUME <= volume <= self.MAX_VOLUME:
            self.__volume = volume
        else:
            print('볼륨 오류')
    def volume_up(self,volume):
        if self.__volume < self.MAX_VOLUME:
            self.__volume += 1
    def volume_down(self,volume):
        if self.__volume > self.MIN_VOLUME:
            self.__volume -= 1
    def channel_up(self,channel):
        if self.__channel < self.MAX_CHANNEL:
            self.__channel += 1
        elif self.__channel == self.MAX_CHANNEL:
            self.__channel = self.MIN_CHANNEL
    def channel_down(self,channel):
        if self.__channel > self.MIN_CHANNEL:
            self.__channel -= 1
        elif self.__channel == self.MIN_CHANNEL:
            self.__channel = self.MAX_CHANNEL
my_tv = TV()
print(my_tv)
my_tv.toggle_power()
print(my_tv)
my_tv.set_channel(45)
print(my_tv)
my_tv.volume_up()
my_tv.volume_down()
print(my_tv)



