from parsers.json_parser import JsonParser


class ProficienciesParser(object):
    def __init__(self):
        self.proficiencies = []

    def parse_proficiencies(self, json_data):
        prof_map = {"saving": SaveProficiencyParser,
                    "skill": SkillProficiencyParser}

        for prof in json_data:
            prof_type = prof["name"].split()[0].strip(":").lower()

            if prof_type in prof_map:
                proficiency = prof_map[prof_type]()
                proficiency.parse_json(prof)
                self.proficiencies.append(proficiency)
            else:
                print("Did not recognize proficiency type: {}, ignoring".format(prof["name"]))


class ProficiencyParser(JsonParser):
    def __init__(self):
        super(ProficiencyParser, self).__init__()
        self.value = 0
        self.type = None
        self.get_attrs()

    def get_attrs(self):
        self.reg_attrs = {"value": None}

    @staticmethod
    def get_prof_type(name):
        return name.split(":")[1].strip()


class SaveProficiencyParser(ProficiencyParser):
    def __init__(self):
        super(SaveProficiencyParser, self).__init__()
        self.type = "save"
        self.ability = None
        self.get_attrs()

    def get_attrs(self):
        super(SaveProficiencyParser, self).get_attrs()
        special_attrs = {"name": self.get_ability}
        self.special_attrs.update(special_attrs)

    def get_ability(self, json_data):
        self.ability = self.get_prof_type(json_data)


class SkillProficiencyParser(ProficiencyParser):
    def __init__(self):
        super(SkillProficiencyParser, self).__init__()
        self.type = "skill"
        self.skill = None
        self.get_attrs()

    def get_attrs(self):
        super(SkillProficiencyParser, self).get_attrs()
        special_attrs = {"name": self.get_skill}
        self.special_attrs.update(special_attrs)

    def get_skill(self, json_data):
        self.skill = self.get_prof_type(json_data)
