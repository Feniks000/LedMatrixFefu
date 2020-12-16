from django.shortcuts import render


# Create your views here.


def index(request):
    class Cell:
        def __init__(self, id, x, y):
            self.id = id
            self.x, self.y = x, y

    data = {"cells": []}
    id = 0
    for x in range(1, 17):
        for y in range(1, 17):
            data["cells"].append(Cell(id, (x - 1), (y - 1)))
            id += 1

    return render(request, 'main/index.html', data)
