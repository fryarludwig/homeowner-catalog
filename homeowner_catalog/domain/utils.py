

def unwrap_lazy_object(lazy_object):
    if hasattr(lazy_object, '_wrapped') and hasattr(lazy_object, '_setup'):
        if lazy_object._wrapped.__class__ == object:
            lazy_object._setup()
        return lazy_object._wrapped
