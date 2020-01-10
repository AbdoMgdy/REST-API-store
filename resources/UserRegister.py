
from models.user import UserModel
from flask_restful import Resource, reqparse



class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
    type=str,
    required=True,
    help="Need Username."
    )
    parser.add_argument("password",
                         type=str,
                         required=True,
                         help="Need Password.")
                        
    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {'message': 'User Exists'}, 400
        user = UserModel(**data)
        user.save_to_db()
        return {'message':'user was created'}
