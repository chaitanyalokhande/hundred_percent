from django.shortcuts import render
import numpy as np
from sklearn.linear_model import LinearRegression


# Create your views here.


def index(request):
    return render(request, 'index.html')


def calculate(request):
    if request.method == 'POST':
        x = int(request.POST.get('hours'))
        if x <= 40:

            print(x)
            time_studied = np.array([18, 20, 25, 30, 35, 40]).reshape(-1, 1)
            score = np.array([60, 70, 80, 85, 90, 95]).reshape(-1, 1)

            model = LinearRegression()
            model.fit(time_studied, score)
            pr = model.predict(np.array(x).reshape(-1, 1))
            for n in pr:
                xx = int(n)
                round(xx, 2)
                print("you can score:{}".format(xx))

                context = {'hour': xx}

            return render(request, 'index.html', context)
        else:
            context_error = {'error': "enter below 40 hours"}
            return render(request, 'index.html', context_error)
