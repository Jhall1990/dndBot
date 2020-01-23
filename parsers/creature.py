from parsers.json_parser import JsonParser
from parsers.proficiencies import ProficienciesParser


class CreatureParser(JsonParser):
    def __init__(self):
        super(CreatureParser, self).__init__()
        self.name = ""
        self.size = ""
        self.type = ""
        self.subtype = ""
        self.alignment = ""
        self.ac = ""
        self.hp = ""
        self.hit_dice = ""
        self.str = 0
        self.dex = 0
        self.con = 0
        self.int = 0
        self.wis = 0
        self.chr = 0
        self.proficiencies = []
        self.get_attrs()

    def get_attrs(self):
        self.reg_attrs = {"name": None,
                          "size": None,
                          "type": None,
                          "subtype": None,
                          "alignment": None,
                          "armor_class": "ac",
                          "hit_points": "hp",
                          "hit_dice": None,
                          "strength": "str",
                          "dexterity": "dex",
                          "constitution": "con",
                          "intelligence": "int",
                          "wisdom": "wis",
                          "charisma": "chr"}

        self.special_attrs = {"proficiencies": self.parse_proficiencies}

    def parse_proficiencies(self, prof_json):
        self.proficiencies = ProficienciesParser()
        self.proficiencies.parse_proficiencies(prof_json)
