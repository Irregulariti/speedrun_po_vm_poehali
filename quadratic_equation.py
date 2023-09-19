class QuadEquation:
    equation: str
    kft: list

    def __init__(self, equation: str, kft: list):
        self.equation = equation
        self.kft = kft

    def disc(self):
        a, b, c = self.kft
        return b ** 2 - (4 * a * c)

    def solve(self):
        a, b, c = self.kft
        D = self.disc()
        x1, x2 = (-b + D ** 0.5) / (2 * a), (-b - D ** 0.5) / (2 * a)
        return (x1, x2)
