import turtle

class DrawTree:

    def __init__(self):
        self.t = turtle.Turtle()

    def draw(self, lineLength, angle):
        if lineLength > 0:
            self.t.forward(lineLength)
            self.t.left(angle)
            self.draw(lineLength-10,angle)

            self.t.right(angle)
            self.t.right(angle)
            self.draw(lineLength-10,angle)

            self.t.left(angle)
            self.t.backward(lineLength)


def main():
    lineLength = int(input(">> 기준이 되는 선의 길이를 입력해 주세요:"))
    angle = int(input(">> Angle 값을 입력해 주세요:"))

    s = turtle.Screen()
    Draw = DrawTree()
    Draw.t.left(90)
    Draw.t.up()
    Draw.t.goto(0,-200)
    Draw.t.down()

    Draw.draw(lineLength,angle)
    
main()
