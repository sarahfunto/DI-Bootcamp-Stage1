import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius:
            self._radius = radius
        elif diameter:
            self._radius = diameter / 2
        else:
            raise ValueError("You must provide either a radius or a diameter.")
    def radius(self):
        return self._radius
    def radius(self, value):
        self._radius = value
    def diameter(self):
        return self._radius * 2
    def diameter(self, value):
        self._radius = value / 2
    def area(self):
        return math.pi * self._radius ** 2
    def __str__(self):
        return f"Circle with radius {self._radius:.2f}"
    def __repr__(self):
        return f"Circle(radius={self._radius:.2f})"
    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        return NotImplemented
    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return NotImplemented
    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.radius > other.radius
        return NotImplemented
    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        return NotImplemented
c1 = Circle(radius = 5)
c2 = Circle(diameter = 10)
print(c1.area)           # Aire
print(c1 + c2)           # Nouveau cercle
print(c1 > c2)           # Comparaison
print(c1 == c2)          # Égalité

circles = [c1, c2, Circle(2), Circle(7)]
sorted_circles = sorted(circles)
print(sorted_circles) 