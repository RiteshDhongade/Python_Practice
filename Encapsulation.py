class car:
    def __init__(self , year , make , model , speed ) :
        self.__year = year
        self.__make = make
        self.__model = model
        self.__speed = speed
    def set_speed(self , speed) :                      
        self.__speed = 0 if speed < 0 else speed  # -ve speed will be 0 