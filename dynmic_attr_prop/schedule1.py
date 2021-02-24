from dynmic_attr_prop import osconfeed

DB_NAME = 'data/schedule1_db'
CONFERENCE = 'conference.115'


class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)  # this is a quick way to create a bunch of attributes in the instances


def load_db(db):
    raw_data = osconfeed.load()  # get a JSON object
    for collection, rec_list in raw_data['Schedule'].items():
        record_type = collection[:-1]  # get rid of the 's', e.g., 'events'
        for rec in rec_list:
            key = '{}.{}'.format(record_type, rec['serial'])
            rec['serial'] = key
            db[key] = Record(**rec)


if __name__ == '__main__':
    import shelve

    db = shelve.open(DB_NAME)
    if CONFERENCE not in db:
        load_db(db)
    speaker = db['speaker.3471']
    print(type(speaker))
    print(speaker.name, speaker.twitter)
    db.close()
