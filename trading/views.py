from django.shortcuts import render,redirect
from django.contrib import messages


def foxtrading(request):
    if request.user.is_authenticated:
        import requests
        headers = {
            'Content-Type': 'application/json'
        }
        requestResponse = requests.get(
            "https://api.tiingo.com/tiingo/daily/aapl/prices?startDate=2019-01-01&endDate=2019-02-01&token=f346c6b9df4f517090b3a878b66e239e51f0a4e8", headers=headers)
        data = requestResponse.json()
        return render(request, 'components/graph.html', {'data': data, 'sbar': 'trading', })
    else:
        messages.error(request, 'Please Login To Continue')
        return redirect("/")
