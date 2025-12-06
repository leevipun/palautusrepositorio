from flask import Flask, render_template, request, redirect, url_for, session
from tuomari import Tuomari
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly
import os

app = Flask(__name__)
app.secret_key = 'kivi-paperi-sakset-secret-key-2025'

def get_game_state():
    """Hae pelin tila istunnosta"""
    if 'game_state' not in session:
        session['game_state'] = {
            'tuomari': None,
            'tekoaly': None,
            'game_type': None,
            'player1_move': None,
            'player2_move': None,
            'player1_played': False,
            'last_result': None
        }
    return session['game_state']

def init_game(game_type):
    """Alusta uusi peli"""
    state = get_game_state()
    state['tuomari'] = Tuomari().__dict__  # Muunna dict:iksi istuntoon
    state['game_type'] = game_type
    state['player1_move'] = None
    state['player2_move'] = None
    state['player1_played'] = False
    state['last_result'] = None
    
    if game_type == 'ai_easy':
        state['tekoaly'] = 'easy'
    elif game_type == 'ai_hard':
        state['tekoaly'] = 'hard'
    elif game_type == 'two_players':
        state['tekoaly'] = None
    
    session.modified = True

def get_tuomari():
    """Hae Tuomari-olio istunnosta"""
    state = get_game_state()
    tuomari = Tuomari()
    if state['tuomari']:
        tuomari.ekan_pisteet = state['tuomari'].get('ekan_pisteet', 0)
        tuomari.tokan_pisteet = state['tuomari'].get('tokan_pisteet', 0)
        tuomari.tasapelit = state['tuomari'].get('tasapelit', 0)
    return tuomari

def save_tuomari(tuomari):
    """Tallenna Tuomari-olio istuntoon"""
    state = get_game_state()
    state['tuomari'] = tuomari.__dict__
    session.modified = True

def get_ai_move(player_move):
    """Hae tekoälyn siirto"""
    state = get_game_state()
    if state['tekoaly'] == 'easy':
        ai = KPSTekoaly()
    else:
        ai = KPSParempiTekoaly()
    return ai._toisen_siirto(player_move)

@app.route('/')
def index():
    """Pääsivu - valikkoon"""
    state = get_game_state()
    return render_template('index.html', 
                         game_type=None,
                         player_score=0,
                         opponent_score=0,
                         draws=0)

@app.route('/start-game', methods=['POST'])
def start_game():
    """Aloita uusi peli"""
    game_type = request.form.get('game_type')
    
    if game_type not in ['ai_easy', 'ai_hard', 'two_players']:
        return redirect(url_for('index'))
    
    init_game(game_type)
    return redirect(url_for('game'))

@app.route('/game')
def game():
    """Pelinäyttö"""
    state = get_game_state()
    
    if state['game_type'] is None:
        return redirect(url_for('index'))
    
    tuomari = get_tuomari()
    
    result_message = None
    result_class = None
    
    if state['last_result']:
        result = state['last_result']['result']
        if result == 'voitit':
            result_message = '🎉 Pelaaja 1 voitti!'
            result_class = 'result-win'
        elif result == 'hävisit':
            result_message = '😔 Pelaaja 1 hävisi!'
            result_class = 'result-lose'
        elif result == 'tasapeli':
            result_message = '🤝 Tasapeli!'
            result_class = 'result-draw'
    
    return render_template('index.html',
                         game_type=state['game_type'],
                         player_score=tuomari.ekan_pisteet,
                         opponent_score=tuomari.tokan_pisteet,
                         draws=tuomari.tasapelit,
                         result_message=result_message,
                         result_class=result_class,
                         last_result=state['last_result'],
                         player1_played=state['player1_played'])

@app.route('/play', methods=['POST'])
def play():
    """Pelaa kierros (AI vastaan)"""
    state = get_game_state()
    
    if state['game_type'] not in ['ai_easy', 'ai_hard']:
        return redirect(url_for('index'))
    
    player_move = request.form.get('move')
    
    if player_move not in ['k', 'p', 's']:
        return redirect(url_for('game'))
    
    # Hae tekoälyn siirto
    opponent_move = get_ai_move(player_move)
    
    # Kirjaa siirto tuomariin
    tuomari = get_tuomari()
    tuomari.kirjaa_siirto(player_move, opponent_move)
    save_tuomari(tuomari)
    
    # Määritä tulos
    if player_move == opponent_move:
        result = 'tasapeli'
    elif tuomari._eka_voittaa(player_move, opponent_move):
        result = 'voitit'
    else:
        result = 'hävisit'
    
    state['last_result'] = {
        'player_move': player_move,
        'opponent_move': opponent_move,
        'result': result
    }
    state['player1_played'] = False
    session.modified = True
    
    return redirect(url_for('game'))

@app.route('/play-player1', methods=['POST'])
def play_player1():
    """Kahden pelaajan peli - Pelaaja 1 valitsee"""
    state = get_game_state()
    
    if state['game_type'] != 'two_players':
        return redirect(url_for('index'))
    
    player_move = request.form.get('move')
    
    if player_move not in ['k', 'p', 's']:
        return redirect(url_for('game'))
    
    state['player1_move'] = player_move
    state['player1_played'] = True
    state['last_result'] = None
    session.modified = True
    
    return redirect(url_for('game'))

@app.route('/play-player2', methods=['POST'])
def play_player2():
    """Kahden pelaajan peli - Pelaaja 2 valitsee ja peli pelataan"""
    state = get_game_state()
    
    if state['game_type'] != 'two_players':
        return redirect(url_for('index'))
    
    if not state['player1_move']:
        return redirect(url_for('game'))
    
    player2_move = request.form.get('move')
    
    if player2_move not in ['k', 'p', 's']:
        return redirect(url_for('game'))
    
    # Kirjaa siirto tuomariin
    tuomari = get_tuomari()
    tuomari.kirjaa_siirto(state['player1_move'], player2_move)
    save_tuomari(tuomari)
    
    # Määritä tulos
    if state['player1_move'] == player2_move:
        result = 'tasapeli'
    elif tuomari._eka_voittaa(state['player1_move'], player2_move):
        result = 'voitit'
    else:
        result = 'hävisit'
    
    state['last_result'] = {
        'player_move': state['player1_move'],
        'opponent_move': player2_move,
        'result': result
    }
    state['player1_move'] = None
    state['player1_played'] = False
    session.modified = True
    
    return redirect(url_for('game'))

@app.route('/reset', methods=['POST'])
def reset():
    """Nollaa pelin"""
    state = get_game_state()
    game_type = state['game_type']
    
    if game_type:
        init_game(game_type)
    
    return redirect(url_for('game'))

@app.route('/back-to-menu', methods=['POST'])
def back_to_menu():
    """Palaa valikkoon"""
    state = get_game_state()
    state['game_type'] = None
    state['player1_move'] = None
    state['player2_move'] = None
    state['player1_played'] = False
    state['last_result'] = None
    session.modified = True
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
