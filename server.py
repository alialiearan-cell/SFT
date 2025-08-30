from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

# روت برای سرو کردن فایل HTML
@app.route('/', methods=['GET'])
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
    <title>Page Title</title>
    </head>
    <body>

    <h1>Hi</h1>
    <a href="#" onclick="runPythonScript()">
    <p style="font-size:1px";>
        don't click me
    </p>
    </a>
        <pre id="output"></pre>

    <script>
    function runPythonScript() {
                // ارسال درخواست به API
                fetch('/main.py')
                    .then(response => response.json())  // پارس کردن پاسخ به JSON
                    .then(data => {
                        // نمایش خروجی در عنصر <pre>
                        document.getElementById('output').textContent = data.output;
                    })
                    .catch(error => {
                        console.error('خطا در اجرای اسکریپت:', error);
                        document.getElementById('output').textContent = 'خطا در اجرای اسکریپت.';
                    });
            }
    </script>

    </body>
    </html>
    '''

# API برای اجرای اسکریپت Python
@app.route('/main.py', methods=['GET'])
def run_script():
    try:
        # اجرای فایل Python و دریافت خروجی
        result = subprocess.run(['python', 'main.py'], capture_output=True, text=True, check=True)
        return jsonify({"output": result.stdout})
    except subprocess.CalledProcessError as e:
        return jsonify({"output": f"خطا در اجرای اسکریپت: {e.stderr}"}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)