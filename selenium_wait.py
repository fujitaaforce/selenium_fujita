class element_has_text_value(object):

  def __init__(self, locator):
    self.locator = locator

  def __call__(self, driver):
    # 要素の取得
    element = driver.find_element(*self.locator)

    # 要素のvalueが空であればFalseを返す
    if element.get_attribute("value") != "":
        print(element.get_attribute("value"))
        return element

    else:
        print(element.get_attribute("value"))
        return False