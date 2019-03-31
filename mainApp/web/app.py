from flask import Flask, jsonify, request
import tensorflow as tf
app = Flask(__name__)

MODEL_PATH = 'mainApp/model/hbmodel/SAMPLE_HR_200_MODEL.pb'

with open(MODEL_PATH, 'rb') as f:
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

@app.route('/')
def hello_world():
    return 'Testing...'

@app.route('/predict/')
def predict():
    content = request.json
    return 'Testing...'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')