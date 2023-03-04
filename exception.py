class ElementNotFoundException(Exception):
    def __init__(self, item, cause=None):
        super(ElementNotFoundException, self).__init__()
        self.item = item
        self.cause = cause

    def __str__(self):
        return "The element with {0} '{1}' was not found".format(*self.item)


class TextNotFoundException(Exception):
    def __init__(self, item, text, cause=None):
        super().__init__(self)
        self.item = item
        self.text = text
        self.cause = cause

    def __str__(self):
        return "No text '{0}' in element '{1}'".format(self.text, self.item)


class ValueNotFoundException(Exception):
    def __init__(self, item, value, cause=None):
        super().__init__(self)
        self.item = item
        self.value = value
        self.cause = cause

    def __str__(self):
        return "No value '{0}' in element '{1}'".format(self.value, self.item)


class ElementVisibleException(Exception):
    def __init__(self, item, cause=None):
        super().__init__(self)
        self.item = item
        self.cause = cause

    def __str__(self):
        return "The element '{0}' a visible".format(self.item[1])


class ElementNotInteractableException(Exception):
    def __init__(self, item, cause=None):
        super(ElementNotInteractableException, self).__init__()
        self.item = item
        self.cause = cause

    def __str__(self):
        return "The element with {0} '{1}' not interactable, has no size and location".format(*self.item)


class AlertNotFoundException(Exception):
    def __init__(self, item, cause=None):
        super(AlertNotFoundException, self).__init__()
        self.item = item
        self.cause = cause

    def __str__(self):
        return "The element with {0} was not found".format(self.item)


class InvisibleCountElementsException(Exception):
    def __init__(self, count, cause=None):
        super().__init__(self)
        self.cause = cause
        self.count = count

    def __str__(self):
        return "Elements != {count}".format(count=self.count)

class NotDownloadNewPdfException(Exception):
    def __init__(self, cause=None):
        super().__init__(self)
        self.cause = cause

    def __str__(self):
        return "Not found download new pdf"

class NotElementsDropdownListException(Exception):
    def __init__(self, cause=None):
        super().__init__(self)
        self.cause = cause

    def __str__(self):
        return "Not elements dropdown list"

class NotFoundElementException(Exception):
    def __init__(self, text, cause=None):
        super().__init__(self)
        self.text = text
        self.cause = cause

    def __str__(self):
        return "No element {}".format(self.text)


