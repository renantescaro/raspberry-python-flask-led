from flask import Flask, jsonify
import RPi.GPIO as GPIO
import time

# config Flask
app = Flask('led_rotas')

# config GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

@app.route('/ligar', methods=['GET'])
def ligar():
    GPIO.output(18,GPIO.HIGH)
    return jsonify({'led':'ligado'})

@app.route('/desligar', methods=['GET'])
def desligar():
    GPIO.output(18,GPIO.LOW)
    return jsonify({'led':'desligado'})

if __name__ == "__main__":
    app.run(port=5000, debug=True, host='0.0.0.0')
