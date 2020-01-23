class JsonParser(object):
    def __init__(self):
        self.reg_attrs = {}
        self.special_attrs = {}

    def get_attrs(self):
        raise NotImplementedError("Subclasses must override this method")

    def parse_json(self, json_data):
        """
        Parses all the provided attributes from the json into the class
        that called the functions.

        reg_attrs = Maps the key in the json to the attribute in the class.
                    A value of None means that the key is the same as the attr.

        special_attrs - Special attrs have functions to parse the data in
                        nested keys.
        """
        if self.reg_attrs:
            self.parse_regular_attrs(json_data)

        if self.special_attrs:
            self.parse_special_attrs(json_data)

        # We parsed everything, no need to keep the attrs around
        del self.reg_attrs
        del self.special_attrs

    def parse_regular_attrs(self, json_data):
        for json_key, class_attr in self.reg_attrs.items():
            value = json_data.get(json_key)
            setattr(self, class_attr if class_attr else json_key, value)

    def parse_special_attrs(self, json_data):
        for json_key, func in self.special_attrs.items():
            func(json_data[json_key])
