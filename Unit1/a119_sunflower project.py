import turtle as trtl
my_turtle = []
turtle_shape = ["turtle"]
turtle_color = ["orange"]


for s in turtle_shape:
  t = trtl.Turtle(shape=s)
  my_turtle.append(t)






wn = trtl.Screen()
wn.mainloop()