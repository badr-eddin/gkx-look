import pandas as pd


class ResultsManager(pd.DataFrame):
    @property
    def _constructor(self):
        return ResultsManager

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_data(self, obj: list):
        self.loc[len(self.index)] = obj

    def remove(self, index: int):
        if index < len(self):
            self.drop(index, inplace=True)
            self.reset_index(drop=True, inplace=True)

    def sort_by(self, filter_s):
        data = self

        if isinstance(filter_s, (list, tuple)):
            for flt in filter_s:
                if flt in data.columns:
                    data = data.sort_values(by=flt)
        else:
            if filter_s in data.columns:
                data = data.sort_values(by=filter_s)

        return data

    def filter_by_word(self, words: str, case_sens=False, field="title"):
        words = (words if case_sens else words.lower()).split(";")
        data = self

        def contains_words(text, ws):
            return any(w in (text if case_sens else text.lower()) for w in ws)
        
        data = data[data[field].apply(lambda x: contains_words(x, words))]
        return data

    def filter_by_category(self, cats):
        return self.filter_by_word(cats, False, "category")

    def filter_by_time(self, t1, t2):
        """
        time of: Year-Month-Day
        """
        if pd.api.types.is_datetime64_any_dtype(self['datetime']):
            return self[(self['datetime'] >= t1) & (self['datetime'] <= t2)]
        else:
            return self

    def filter_by_score(self, s1, s2):
        if not isinstance(s1, (float, int)) or not isinstance(s2, (float, int)):
            return self

        return self[(self["score"] >= s1) & (self["score"] <= s2)]

    def export(self, to="csv", file_name="export.csv"):
        if to == "csv":
            self.to_csv(file_name, index=False)
        elif to == "json":
            self.to_json(file_name, orient='records')
        elif to == "excel":
            self.to_excel(file_name, index=False)
        else:
            raise ValueError("Unsupported export format. Use 'csv', 'json', or 'excel'.")
