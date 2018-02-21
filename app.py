from flask import Flask
from flask import render_template
from flask import request
from flask_bootstrap import Bootstrap
import random


app = Flask(__name__)


Bootstrap(app)


def win_count(u, pc):
    if u == pc:
        return 1, 'You win!'
    else:
        return 0, 'You lose -_-'


@app.route('/')
def powerlessball():
    counter = request.args.get('counter')
    if counter is None or counter == '':
        counter = 0
    else:
        counter = int(counter) + 1

    wins = request.args.get('wins')
    if wins is None or wins == '':
        wins = 0
    else:
        wins = int(wins)

    pick = request.args.get('pick')
    if pick is None:
        pick = 0
    elif pick == '':
        return render_template('index.html', empty_message='Pick a number...', counter=counter-1, wins=wins, show=1,
                               pick=0)
    elif int(pick) < 1:
        return render_template('index.html', empty_message='Pick a number greater than 0', counter=counter-1, wins=wins,
                               show=1, pick=int(pick))
    elif int(pick) > 99:
        return render_template('index.html', empty_message='Pick a number less than 100', counter=counter-1, wins=wins,
                               show=1, pick=int(pick))
    else:
        pick = int(pick)

    lotto_pick = random.randint(1, 99)
    result, result_message = win_count(pick, lotto_pick)

    alert_type = 'info'

    if result:
        wins = wins + 1
        alert_type = 'success'
    else:
        alert_type = 'danger'

    return render_template('index.html', pick=pick, lotto_pick=lotto_pick, result_message=result_message,
                           counter=counter, wins=wins, alert_type = alert_type)

if __name__ == '__main__':
    app.run()