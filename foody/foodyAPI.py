from flask import Flask
from flask_restful import Api, Resource, reqparse
from generate_menu import generate_json


app = Flask(__name__)
api = Api(app)

foody_args = reqparse.RequestParser()
foody_args.add_argument("min_calories", type=float)
foody_args.add_argument("max_calories", type=float)
foody_args.add_argument("min_protein", type=float)
foody_args.add_argument("max_protein", type=float)
foody_args.add_argument("min_fat", type=float)
foody_args.add_argument("max_fat", type=float)
foody_args.add_argument("min_sodium", type=float)
foody_args.add_argument("max_sodium", type=float)
foody_args.add_argument("number_of_breakfasts", type=int)
foody_args.add_argument("number_of_lunches", type=int)
foody_args.add_argument("number_of_dinners", type=int)


class foodyAPI(Resource):
    def post(self):
        args = foody_args.parse_args()
        message = generate_json(args.min_calories,
                                args.max_calories,
                                args.min_protein,
                                args.max_protein,
                                args.min_fat,
                                args.max_fat,
                                args.min_sodium,
                                args.max_sodium,
                                args.number_of_breakfasts,
                                args.number_of_lunches,
                                args.number_of_dinners)
        return message


api.add_resource(foodyAPI, "/foody")

if __name__ == "__main__":
    app.run(debug=True)
