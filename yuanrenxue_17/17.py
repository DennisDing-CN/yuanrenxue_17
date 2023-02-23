import httpx

total = 0
for i in range(1, 6):
    params = {
        'page': i,
    }
    headers = {
        'user-agent': 'yuanrenxue.project',
        'cookie': 'sessionid=q1axbzfiaiofuonfslwm0p88z3c159fo;',
    }
    client = httpx.Client(http2=True,headers=headers)
    response = client.get('https://match.yuanrenxue.com/api/match/17', params=params)
    print(response.text)
    data = response.json()["data"]
    for d in data:
        total += d["value"]

print(int(total))