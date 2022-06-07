import json


def load_json():
    """Берет данные из json Возвращает список со словарями"""
    with open("candidates.json", "rt", encoding="utf8") as file:
        return json.load(file)


def format_candidates(candidates: list[dict]) -> str:
    """возвращает данные в нужном формате"""
    result = '<pre>'

    for candidate in candidates:
        result += f"""
            {candidate["name"]}\n
            {candidate["position"]}\n
            {candidate["skills"]}\n
        """
    result += '</pre>'
    return result


def get_all_candidates() -> list[dict]:
    """Возвращает список всех кандидатов"""
    return load_json()


def get_candidate_by_id(uid: int) -> dict | None:
    """Возвращает одного кандидата по ID или None"""
    candidates = get_all_candidates()
    for candidate in candidates:
        if candidate['id'] == uid:
            return candidate
    return None


def get_candidate_by_skill(skill: str) -> dict | None:
    """Возвращает одного кандидата по наличию навыка или None"""
    candidates = get_all_candidates()
    list_of_candidates = []
    for candidate in candidates:
        #print(candidate['skills'])
        skills = candidate['skills'].split(", ")
        for i in skills:
            if i.lower() == skill.lower():
                list_of_candidates.append(candidate)
    return list_of_candidates

#print(get_candidate_by_skill('python'))