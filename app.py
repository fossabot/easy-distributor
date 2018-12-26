import os.path
import json
from flask import Flask, render_template, request, send_file
from postform import PostForm
from logging import getLogger
logger = getLogger(__name__)

app = Flask(__name__)
app.config['APPLICATION_ROOT'] = '/'


@app.route(app.config['APPLICATION_ROOT'], methods=['GET', 'POST'])
def download():
    logger.debug(request.method)
    form = PostForm(request.form)
    result = -1  # -1: not POST, 0: Success, >0: Failed

    if request.method == 'POST' and form.validate():
        input_str = form.input.data
        selected = form.file_selector.data
        logger.warning('input: ' + input_str)
        logger.warning('file: ' + selected)

        # check download key
        is_good_key = False
        _settings_file = os.path.dirname(os.path.abspath(__file__)) + '/data/' + 'files.json'
        with open(_settings_file, 'r') as f:
            json_data = json.loads(f.read())

        for each in json_data:
            if selected == each['file_name']:
                for each_key in each['keys']:
                    if input_str == each_key['key']:
                        # TODO: [feature] download counter
                        # TODO: [feature] duration checker
                        is_good_key = True
                        break

        if is_good_key:
            logger.warning('verified')
            file_path = os.path.dirname(os.path.abspath(__file__)) + '/data/' + selected
            logger.debug(file_path)
            return send_file(file_path, as_attachment=True)
        else:
            logger.warning('incorrect key')
            return render_template('error.html', err='INCORRECT DOWNLOAD KEY')

    return render_template('distributor.html', form=form, result=result)


if __name__ == '__main__':
    import logging

    LOG_LEVEL = logging.INFO  # DEBUG, INFO, WARNING, ERROR, CRITICAL
    LOG_FMT = "%(asctime)s - %(levelname)s - %(threadName)s - %(name)s - %(message)s"
    logging.basicConfig(format=LOG_FMT, level=LOG_LEVEL)

    app.run(debug=False, host='0.0.0.0', port=8080)
