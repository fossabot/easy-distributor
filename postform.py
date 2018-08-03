import os.path
import json
from wtforms import Form, validators, StringField, SelectField, SubmitField


class PostForm(Form):

    _settings_file = os.path.dirname(os.path.abspath(__file__)) + '/static/' + 'files.json'
    with open(_settings_file, 'r') as f:
        json_data = json.loads(f.read())

    _files_arr = [(each['file_name'], each['display_name']) for each in json_data]

    # generate fields
    input = StringField('Enter your download key', [validators.Length(min=1, max=32)], default='')
    file_selector = SelectField('Select a file', choices=_files_arr)

    btn = SubmitField('Download')
