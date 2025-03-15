
class Entity:
    class_var1 = 5
    class_var2 = 6
    def __init__(self):
        print("hey")
        self.class_var1 = 8
        self.class_var2 = 9
    def print(self):
        t=self.class_var1 + 2
       # print(f"class var1 {self.class_var1}, class var 2 {self.class_var2}")
        print("value here in print", t)


if __name__ == '__main__':
    obj = Entity()
    print(Entity.class_var1)
    print(Entity.class_var2)
    obj.print()
    print(f"class var from obj  {Entity.class_var1}     class var1 from obj1 {obj.class_var1}")


    obj1 = Entity()
    obj1.class_var1 = 100
    Entity.class_var1 = 22

    x = [5,4]
    for i in range

    print(f"class var from obj  {Entity.class_var1}     class var1 from obj1 {obj1.class_var1}")
    obj1.print()

    for i in range(2):
        print(i)