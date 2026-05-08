from turtle import Screen

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)

root = screen.getcanvas().winfo_toplevel()
root.call('wm','attributes','.','-topmost','1')

screen.exitonclick()