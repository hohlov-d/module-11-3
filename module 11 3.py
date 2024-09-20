


def introspection_info(obj):
    type_obj = type(obj).__name__
    attributes_obj = dir(obj)
    module = obj.__class__.__module__
    address_obj = id(obj)
    doc_obj = obj.__doc__

    return {'Тип': type_obj, 'Атрибуты': attributes_obj, 'Модуль': module,
            'Индификатор': address_obj, 'Документационная строка': doc_obj}


number_info = introspection_info(42)


print(number_info)
