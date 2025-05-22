from flask import Flask, render_template
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# Static information as metric
metrics.info('app_info', 'Application info', version='1.0.0')

@app.route('/')
@metrics.do_not_track()
def index():
    return render_template('t_rex_game.html')

# Add a health check endpoint
@app.route('/health')
@metrics.do_not_track()
def health():
    return {'status': 'healthy'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
