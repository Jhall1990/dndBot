from parsers.creature import CreatureParser


class MonsterParser(CreatureParser):
    def __init__(self):
        super(MonsterParser, self).__init__()
        self.walk_speed = None
        self.fly_speed = None
        self.swim_speed = None
        self.get_attrs()

    def get_attrs(self):
        super(MonsterParser, self).get_attrs()
        special_attrs = {"speed": self.parse_speed}
        self.special_attrs.update(special_attrs)

    def parse_speed(self, speed_json):
        """
        Checks the speed_json for the keys walk, fly, and swim. For all
        the keys present it sets the corresponding walk_speed, fly_speed,
        and swim_speed attributes
        """
        speed_keys = ["walk", "fly", "swim"]

        for key in speed_keys:
            value = speed_json.get(key)

            if value:
                class_attr = "{}_speed".format(key)
                setattr(self, class_attr, value)
