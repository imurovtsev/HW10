from flask import Flask
from utils import load_json, get_all_candidates, format_candidates, get_candidate_by_id, get_candidate_by_skill

app = Flask(__name__)


@app.route('/')
def page_index():
    """Глвная страница"""
    candidates: list[dict] = get_all_candidates()
    result: str = format_candidates(candidates)
    return result


@app.route('/candidate/<int:uid>')
def page_candidate(uid):
    """Поиск кандидата по id"""
    candidate: dict = get_candidate_by_id(uid)
    result = f'<img src="{candidate["picture"]}">'
    result += format_candidates([candidate])
    return result

@app.route('/skill/<skill>')
def page_skill(skill):
    """Поиск кандидата по навыку"""
    candidate: dict = get_candidate_by_skill(skill)
    result = format_candidates(candidate)
    return result

if __name__ == "__main__":
    app.run()
