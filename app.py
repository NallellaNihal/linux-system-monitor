from flask import Flask, render_template, jsonify
import psutil
import platform
import time

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/stats")
def stats():
    net = psutil.net_io_counters()

    data = {
        "cpu": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage("/").percent,
        "network_sent": round(net.bytes_sent / (1024 * 1024), 2),
        "network_recv": round(net.bytes_recv / (1024 * 1024), 2),
        "system": platform.system(),
        "node": platform.node(),
        "release": platform.release(),
        "uptime": round((time.time() - psutil.boot_time()) / 3600, 2)
    }

    return jsonify(data)

@app.route("/api/processes")
def processes():
    process_list = []

    for proc in psutil.process_iter(["pid", "name", "cpu_percent", "memory_percent"]):
        try:
            process_list.append(proc.info)
        except:
            pass

    process_list = sorted(
        process_list,
        key=lambda x: x["memory_percent"] or 0,
        reverse=True
    )[:10]

    return jsonify(process_list)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
