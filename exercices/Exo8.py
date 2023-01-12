import turtle

def koch(n, l):
    if n == 0:
        turtle.forward(l)
    else:
        koch(n - 1, l / 3)
        turtle.left(60)
        koch(n - 1, l / 3)
        turtle.right(120)
        koch(n - 1, l / 3)
        turtle.left(60)
        koch(n - 1, l / 3)