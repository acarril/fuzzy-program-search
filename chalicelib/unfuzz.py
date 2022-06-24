from thefuzz import process

class Choices(object):
    def __init__(self, df) -> None:
        self._df = df

    def create_choice_list(self):
        return self._df['institution_name']

    def fuzzy_search(self, query:str, limit:int=4):
        choices = self.create_choice_list()
        fuzzy_process = process.extract(query=query, choices=choices, limit=limit)
        return [{'name': tup[0], 'score': tup[1], 'idx': tup[2]} for tup in fuzzy_process]