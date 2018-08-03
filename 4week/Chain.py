class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""


class Event:
    pass


class EventGet(Event):
    def __init__(self, type):
        self._type = type

    @property
    def type(self):
        return self._type


class EventSet(Event):
    def __init__(self, value):
        self._value = value
        self._type = type(value)

    @property
    def value(self):
        return self._value

    @property
    def type(self):
        return self._type


class NullHandler:
    _type = None
    _type_to_name = {
        int: 'integer_field',
        float: 'float_field',
        str: 'string_field'
    }

    def __init__(self, successor=None):
        self._successor = successor

    @property
    def type(self):
        return self._type

    @property
    def successor(self):
        return self._successor

    def get_value(self, object, type):
        attrname = self._type_to_name[type]
        return getattr(object, attrname)

    def set_value(self, object, value):
        attrname = self._type_to_name[type(value)]
        setattr(object, attrname, value)

    def handle(self, object, event):
        if event.type == self._type:
            if isinstance(event, EventGet):
                return self.get_value(object, event.type)
            elif isinstance(event, EventSet):
                return self.set_value(object, event.value)
            else:
                raise ValueError('Unknown event type')

        if self.successor:
            return self.successor.handle(object, event)
        else:
            print('I cannot handle this shit anymore...')


class IntHandler(NullHandler):
    _type = int


class FloatHandler(NullHandler):
    _type = float


class StrHandler(NullHandler):
    _type = str