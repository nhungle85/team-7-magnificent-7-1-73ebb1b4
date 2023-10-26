class Position:

    def getPosition( x, y):
        if 0 <= x <= 9 and 0 <= y <= 9:
            return (x, y)
        else:
            return None