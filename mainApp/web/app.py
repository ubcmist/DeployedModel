import logging
import random
import time

from flask import Flask, jsonify, request
import tensorflow as tf
import numpy as np

app = Flask(__name__)

TENSORFLOW_MODEL_PATH = 'mainApp/model/hbmodel/SAMPLE_HR_200_MODEL.pb'

with open(TENSORFLOW_MODEL_PATH, 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())

graph = tf.Graph() 
with graph.as_default():
    tf.import_graph_def(graph_def, name='')

graph.finalize()

sess_config = tf.ConfigProto(
    log_device_placement=False,
    allow_soft_placement = True,
    gpu_options = tf.GPUOptions(
        per_process_gpu_memory_fraction=1
    )
)
sess = tf.Session(graph=graph, config=sess_config)

input_op = graph.get_operation_by_name('input_HR')
input_tensor = input_op.outputs[0]

operations = graph.get_operations()

@app.route('/predict/tensorflow/')
def predict():
    content = request.json
    app.logger.info("Predicting...")
    t = time.time()
    preds = sess.run(output_tensor, {input_tensor : input_HR})
    dt = time.time() - t
    app.logger.info("Execution time: %0.2f" % (dt * 1000.))
    return jsonify(preds)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')