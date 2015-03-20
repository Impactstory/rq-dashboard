from rq_dashboard.app import app
app.run(debug=True, threaded=True, port=5005)


