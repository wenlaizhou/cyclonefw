#!/usr/bin/env python3

import cyclonefw
from cyclonefw.core import MAX_API, PredictAPI
from flask_restplus import fields

model_input = MAX_API.model('ModelInput', {
    'a': fields.Integer(required=True, description='The first integer for addition', example=1),
    'b': fields.Integer(required=True, description='The second integer for addition', example=2)
})

## Define Output of API

# Creating a JSON response model: https://flask-restx.readthedocs.io/en/stable/marshalling.html#the-api-model-factory

predict_response = MAX_API.model('ModelPredictResponse', {
    'status': fields.String(required=True, description='Response status message'),
    'result': fields.Integer(required=True, description='result of sum')
})


class ModelPredictAPI(PredictAPI):

    @MAX_API.doc('predict')
    @MAX_API.marshal_with(predict_response)
    @MAX_API.add_model("param", "111")
    def post(self):
        """Make a prediction given input data"""
        result = {'status': 'error'}

        input_data = MAX_API.payload
        print(input_data)

        # Modify this code if the schema is changed
        # label_preds = [{'label_id': p[0], 'label': p[1], 'probability': p[2]} for p in [x for x in preds]]
        result['status'] = 'OK'
        print('result : ' + str(result))
        return result


app = cyclonefw.MAXApp()

app.add_api(ModelPredictAPI, "/metadata")

app.run()
