class DataBase:
    __instance = None
    def __new__(cls,*args,**kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance
    def __del__(self):
        DataBase.__instance = None
    def __init__(self,user,psw,port):
        self.user = user
        self.psw = psw
        self.port = port
    #     паттерн singelton
    def connect(self):
        print("connect ",self.user,self.psw,self.port)
    def close(self):
        print("close ")
    def read(self):
        print("read ")
    def write(self,data):
        print(f"write {data}")

db = DataBase("user","psw","port")
db1 = DataBase("user2","psw2","port2 ")
print(id(db),id(db1))