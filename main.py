from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime, timedelta
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
            trigger = TriggerIntializer(path="/Users/akhilmatta/PycharmProjects/job_reminder/", file_name="test.xlsx")
            file_handler = trigger.init_trigger()
            file_handler.read_and_convert_content_to_dataframe()

            # Add immediate trigger logic here

        return redirect(url_for('index'))

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
