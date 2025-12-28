from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime, timedelta
import os
import functionality.trigger_job
from functionality.initializer import TriggerIntializer

app = Flask(__name__)
app.secret_key = 'your_secret_key'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        days = request.form.get('days')
        trigger_time = request.form.get('trigger_time')

        if 'schedule' in request.form:
            flash(f"Scheduled for {days} day(s) at {trigger_time}", "success")
            # Here you can add scheduling logic
        elif 'trigger_now' in request.form:
            flash("Triggered manually!", "info")
            trigger = TriggerIntializer(path=os.getenv("CSVFILE_PATH")+"/", file_name="test.csv")
            file_handler = trigger.init_trigger()
            df = file_handler.read_and_convert_content_to_dataframe()
            fp = functionality.trigger_job.TriggerJob()
            fp.send_message(df)

        return redirect(url_for('index'))

    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
